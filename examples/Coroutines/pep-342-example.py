#!# =================
#!#  PEP 342 Example
#!# =================

#!# This article provides a full Python 3 example illustrating the use of coroutines via enhanced
#!# generators as described in the `PEP 342 document <https://www.python.org/dev/peps/pep-0342>`_.
#!#
#!# The PEP 342 proposes some enhancements to the API and syntax of generators, to make them usable
#!# as simple coroutines. This PEP proposal was implemented in Python 2.5. The code given as example
#!# in this document is not working as is. You will find here two real implementations of the PEP
#!# 342's example for Python 3, the first one is implemented without coroutines to serve as
#!# reference and the second one makes use of coroutines. This example implements a thumbnail pager.

####################################################################################################

import os
import tempfile

#!# Basic Implementation
#!# --------------------

####################################################################################################

class PageSize(object):

    ##############################################

    def __init__(self, x, y):
        self.x = x
        self.y = y

    ##############################################

    def __truediv__(self, other):
        return int(self.x / other.x), int(self.y / other.y)

    ##############################################

    def __repr__(self):
        return "PageSize {}x{}".format(self.x, self.y)

####################################################################################################

class Image(object):

    ##############################################

    def __init__(self, name, page_size):
        self.name = name
        self.page_size = page_size

    ##############################################

    def __repr__(self):
        return 'Image {}'.format(self.name)

    ##############################################

    def paste(self, image, x, y):
        print("paste {} in {} at ({}, {})".format(image.name, self.name, x, y))

    ##############################################

    def create_thumbnail(self, thumb_size):
        print('create_thumbnail', self.name)
        return self.__class__('thumb_' + self.name, thumb_size)

    ##############################################

    def write_image(self, filename):
        print('write_image', self.name, filename, '\n')

####################################################################################################

class JpegWriter(object):

    ##############################################

    def  __init__(self, dirname):
        self.dirname = dirname
        self.file_number = 1

    ##############################################

    def send(self, image):
        filename = os.path.join(self.dirname, "page%04d.jpg" % self.file_number)
        Image.write_image(image, filename)
        self.file_number += 1

####################################################################################################

class ThumbnailPager(object):

    ##############################################

    def __init__(self, page_size, thumb_size, destination):

        self.thumb_size = thumb_size
        self.destination = destination

        self.page = Image('page', page_size)
        self.rows, self.columns = page_size / thumb_size
        self.current_row, self.current_column = 0, 0
        self.pending = False

    ##############################################

    def send(self, image):

        thumb = image.create_thumbnail(self.thumb_size)
        self.page.paste(thumb, self.current_column*self.thumb_size.x, self.current_row*self.thumb_size.y)

        self.pending = True
        self.current_column += 1
        if self.current_column == self.columns:
            self.current_row += 1
            if self.current_row == self.rows:
                self.destination.send(self.page)
                self.current_row, self.current_column = 0, 0
                self.pending = False
            else:
                self.current_column = 0

    ##############################################

    def close(self):

        if self.pending:
            self.destination.send(self.page)

####################################################################################################

def write_thumbnails(page_size, thumb_size, images, output_dir):
    pipeline = ThumbnailPager(page_size, thumb_size, JpegWriter(output_dir))
    for image in images:
        print("pipeline.send", image.name)
        pipeline.send(image)
    print("pipeline.close")
    pipeline.close()

####################################################################################################

with tempfile.TemporaryDirectory() as output_dir:
    write_thumbnails(page_size=PageSize(200, 300),
                     thumb_size=PageSize(100, 100),
                     images=[Image("image{}".format(i), None) for i in range(10)],
                     output_dir=output_dir)
#o#

####################################################################################################

#!# Implementation using coroutines
#!# -------------------------------

####################################################################################################

def consumer(func):
    def wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        next(generator)
        return generator
    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__  = func.__doc__
    return wrapper

####################################################################################################

class PageSize(object):

    ##############################################

    def __init__(self, x, y):

        self.x = x
        self.y = y

    ##############################################

    def __truediv__(self, other):
        return int(self.x / other.x), int(self.y / other.y)

    ##############################################

    def __repr__(self):
        return "PageSize {}x{}".format(self.x, self.y)

####################################################################################################

class Image(object):

    ##############################################

    def __init__(self, name, page_size):
        self.name = name
        self.page_size = page_size

    ##############################################

    def __repr__(self):
        return 'Image {}'.format(self.name)

    ##############################################

    def paste(self, image, x, y):
        print("paste {} in {} at ({}, {})".format(image.name, self.name, x, y))

    ##############################################

    def create_thumbnail(self, thumb_size):
        print('create thumbnail of', self.name)
        return self.__class__('thumb_' + self.name, thumb_size)

    ##############################################

    def write_image(self, filename):
        print('write image', self.name, filename, '\n')

####################################################################################################

@consumer
def jpeg_writer(dirname):
    file_number = 1
    while True:
        filename = os.path.join(dirname, "page%04d.jpg" % file_number)
        (yield).write_image(filename)
        file_number += 1

####################################################################################################

@consumer
def thumbnail_pager(page_size, thumb_size, destination):
    while True:
        page = Image('page', page_size)
        rows, columns = page_size / thumb_size
        pending = False
        try:
            for row in range(rows):
                for column in range(columns):
                    thumb = (yield).create_thumbnail(thumb_size)
                    page.paste(thumb, column*thumb_size.x, row*thumb_size.y)
                    pending = True
        except GeneratorExit:
            # close() was called, so flush any pending output
            if pending:
                destination.send(page)
            # then close the downstream consumer, and exit
            destination.close()
            return
        else:
            # we finished a page full of thumbnails, so send it downstream and keep on looping
            destination.send(page)

####################################################################################################

def write_thumbnails(page_size, thumb_size, images, output_dir):
    pipeline = thumbnail_pager(page_size, thumb_size, jpeg_writer(output_dir))
    for image in images:
        print("send", image.name)
        pipeline.send(image)
    print("close")
    pipeline.close()

####################################################################################################

with tempfile.TemporaryDirectory() as output_dir:
    write_thumbnails(page_size=PageSize(200, 300),
                     thumb_size=PageSize(100, 100),
                     images=[Image("image{}".format(i), None) for i in range(10)],
                     output_dir=output_dir)
#o#

#r# ============
#r#  Singletons
#r# ============
#r#
#r# This page contains several singleton implementations.

####################################################################################################

#r# This implementation, based on metaclass, supports subclassing and is thread safe. Best
#r# implementation if we need subclassing.

class SingletonMetaclass(type):

    """A singleton metaclass.

    This implementation supports subclassing and is thread safe.

    """

    ##############################################

    def __init__(cls, class_name, base_classes, namespace):

        # Called just after cls creation in order to complete cls

        type.__init__(cls, class_name, base_classes, namespace)

        cls._instance = None

        # A factory function that returns a new reentrant lock object.
        import threading # SHOULD BE PLACED AT TOP OF THE FILE
        cls._rlock = threading.RLock()

    ##############################################

    def __call__(cls, *args, **kwargs):

        # Called when cls is instantiated: cls(...)
        # type.__call__ dispatches to the cls.__new__ and cls.__init__ methods

        with cls._rlock:
            if cls._instance is None:
                cls._instance = type.__call__(cls, *args, **kwargs)

        return cls._instance

####################################################################################################

#r# This implementation, based on decorator and a class wrapper, doesn't support subclassing.  With
#r# a decorator, each class and its subclasses must be decorated in order to be a singleton.

class singleton:

    """A singleton class decorator.

    This implementation doesn't support subclassing.

    """

    ##############################################

    def __init__(self, cls):

        self._cls = cls
        self._instance = None

    ##############################################

    def __call__(self, *args, **kwargs):

        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)

        return self._instance

####################################################################################################

#r# Another implementation based on decorator but using a closure to wrap the class:

def singleton(cls):

    """A singleton function decorator.

    This implementation doesn't support subclassing.

    """

    instances = {}

    # Return a closure
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

####################################################################################################

def match_modulo(i: int) -> int:   # invalid-return-type
    match i % 2:
        case 0:
            return 0
        case 1:
            return 1
        # case _:
        #     return 2

mactch_modulo(1)

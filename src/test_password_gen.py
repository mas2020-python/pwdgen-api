import pytest
import re
from password_gen import PwdGenerator

gen = PwdGenerator()

# list of list of tuples: first element are the params passed to the generate func: length, numbers, lowercase, uppercase, special
# second element when present is the regexp we expect to match with the password
# third element is the expected length of the password
test_cases = [
    [(1, True, False, False, False), '', 1],
    [(2, True, False, False, False), '', 2],
    [(3, True, False, False, False), '', 3],
    [(4, True, False, False, False), '', 4],
    [(5, True, False, False, False), '', 5],
    [(10, True, False, False, False), '', 10],
    # check numbers only with regexp
    [(10, True, False, False, False), r'^\d{10}$', 10],
    # check lowercases only with regexp
    [(15, False, True, False, False), r'^[a-z]{15}$', 15],
    # check uppercases only with regexp
    [(12, False, False, True, False), r'^[A-Z]{12}$', 12],
    # check specialflags only with regexp
    [(50, False, False, False, True),
     r"^[|!\$#%&'\(\)\*\+,-\./:;<=>\?@\[\]\^_`\{\}~\\]{50}$", 50],
    [(12, False, True, False, True), r'[^A-Z][^0-9]', 12],
    [(3, True, True, True, False), r"^[^|!\$#%&'\(\)\*\+,-\./:;<=>\?@\[\]\^_`\{\}~\\]{3}$", 3],
    [(3, True, True, False, True), r"^[^A-Z]{3}$", 3],
    [(3, True, False, True, True), r"^[^a-z]{3}$", 3],
    [(3, False, True, True, True), r"^[^0-9]{3}$", 3],
]

test_ex_cases = [
    {
        'params': (-1, True, False, False, False),
        'exception': "the password length must be greater than 0"
    },
    {
        'params': (-1, False, False, False, False),
        'exception': "all the arguments passed to the API are False, it is not possible to generate a pwd. Set at least one parameter to True."
    },
    {
        'params': (0, True, False, False, False),
        'exception': ""
    },
    {
        'params': (201, True, False, False, False),
        'exception': ""
    }
]


def test_pwd_generation():
    for tc in test_cases:
        pwd = gen.generate(*tc[0])
        assert len(pwd) == tc[2]
        if tc[1]:
            # test the regexp
            assert re.search(tc[1], pwd)


def test_pwd_exceptions():
    for tc in test_ex_cases:
        if tc['exception'] != "":
            with pytest.raises(Exception, match=tc['exception']):
                gen.generate(*tc['params'])
        else:
            with pytest.raises(Exception):
                gen.generate(*tc['params'])

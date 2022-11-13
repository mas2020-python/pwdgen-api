import pytest
import re
from password_gen import PwdGenerator

gen = PwdGenerator()

# list of list of tuples: first element are the params passed to the generate func, second element when present is the regexp we expect to match with the password, third element is the expected length of the password
test_cases = [
    [(10, True, False, False, False), '', 10],
    # check numbers only with regexp
    [(10, True, False, False, False), r'^\d{10}$', 10],
    # check lowercases only with regexp
    [(15, False, True, False, False), r'^[a-z]{15}$', 15],
    # check uppercases only with regexp
    [(12, False, False, True, False), r'^[A-Z]{12}$', 12],
    # check specialflags only with regexp
    # TODO: try a way to insert the " into the regexp pattern below
    [(50, False, False, False, True), r"^[|!\$#%&'\(\)\*\+,-\./:;<=>\?@\[\]\^_`\{\}~\\]{50}$", 50],
    [(12, False, True, False, True), r'[^A-Z][^0-9]', 12]
]

test_ex_cases = [
    {
        'params': (-1, True, False, False, False),
        'exception': "the password length cannot be a negative number"
    },
    {
        'params': (-1, False, False, False, False),
        'exception': "the numbers of flags is 0, it is not possible to generate a pwd"
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
        with pytest.raises(Exception, match=tc['exception']):
            gen.generate(*tc['params'])

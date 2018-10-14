import pytest
from switchcase import switch

def test_normal_switching():

    with switch(3) as case:

        with case(1):
            assert False

        with case(2):
            assert False

        with case(3):
            assert True

        with case.default:
            assert False

def test_thrown_exception():
    exception = None
    try:
        with switch(10) as case:

            with case(1):
                assert False

            with case(10):
                raise Exception()
    except Exception as e:
        exception = e

    assert type(exception) is Exception


def test_switch_strings():

    value = None

    with switch("Hello") as case:

        with case("Test"):
            assert False

        with case("Hello"):
            value = "Hello"

        with case("4"):
            assert False

        with case.default:
            assert False

    assert value == "Hello"


def test_default_case():

    default = False

    with switch("Not found") as case:

        with case(7):
            assert False

        with case.default:
            default = True

    assert default is True


def test_enter_default_case_if_first():

    default = False

    with switch(1) as case:

        with case.default:
            default = True

        with case(1):
            assert False

    assert default == True



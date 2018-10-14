# Switchcase
Switch cases in python that aren't too weird.

# Usage
```py
from switchcase import switch

with switch(value) as case:

    with case("foo"):
        assert False

    with case("bar"):
        assert False

    # default case must be last
    with case.default:
        print(":^)")
```

# Installation
py-switchcase is available on pypi.

`pip install py-switchcase`
import re

import pyproj


def test_matches_regex():
    assert re.match("[0-9]+\\.[0-9]\\.[0-9]", pyproj.__version__)

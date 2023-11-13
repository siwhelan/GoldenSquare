from lib.report_length import *

# test returned data is correct


def test_report():
    result = report_length("python")
    assert result == "This string was 6 characters long."

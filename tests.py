from main import parse_recurrence


def test_parse_recurrence():
    assert parse_recurrence('1y') == 365
    assert parse_recurrence('2y') == 2 * 365
    assert parse_recurrence('0') == None

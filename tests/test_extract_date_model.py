from extract_date_model import extract_dates


def test_extract_dates():
    text = "The policy provides cover from 31st June 2019"
    dates = extract_dates(text)
    assert dates == ["31st June 2019"]

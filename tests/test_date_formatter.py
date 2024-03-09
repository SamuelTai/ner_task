from date_formatter import standardize_dates


def test_format_dates():
    dates = ["30/Jun/2019", "01/07/2022"]
    formatted_dates = standardize_dates(dates)
    assert formatted_dates == ["30/06/2019", "01/07/2022"]

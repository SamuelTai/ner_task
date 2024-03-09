from preprocess import preprocess_text


def test_preprocess_text():
    text = "The policy provides cover from 31st June 2019"
    cleaned_text = preprocess_text(text)
    assert (
        cleaned_text
        == "The policy provides cover from 31 June 2019"
    )

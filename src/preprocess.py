import re


# Precompile the regular expression to remove special characters
SPECIAL_CHAR_REGEX = re.compile(r"[^a-zA-Z0-9\s/]")

# Precompile the regular expression to improve efficiency
DATE_REGEX = re.compile(r"\b(\d+)(st|nd|rd|th)\b")


def preprocess_text(text: str) -> str:
    """
    Preprocesses the input text by removing special characters and normalizing cardinality from dates.

    Args:
        text (str): Input text to be preprocessed.

    Returns:
        str: Preprocessed text.
    """
    # Remove special characters
    cleaned_text = SPECIAL_CHAR_REGEX.sub("", text)

    # Use the precompiled regex object to normalize cardinality from dates
    cleaned_text = DATE_REGEX.sub(r"\1", cleaned_text)

    return cleaned_text

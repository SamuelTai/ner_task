from typing import List

import spacy

nlp = spacy.load("en_core_web_sm")


def extract_dates(text: str) -> List[str]:
    """
    Extracts dates from the input text using SpaCy's English model.

    Args:
        text (str): Input text from which dates are to be extracted.

    Returns:
        list[str]: List of extracted dates.
    """
    doc = nlp(text)
    dates = []
    for ent in doc.ents:
        if ent.label_ == "DATE":
            dates.append(ent.text)
    return dates

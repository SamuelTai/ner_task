from fastapi import FastAPI
from pydantic import BaseModel
from preprocess import preprocess_text
from extract_date_model import extract_dates
from date_formatter import standardize_dates

app = FastAPI()


class InputText(BaseModel):
    text: str


class OutputResult(BaseModel):
    dates: list[str]
    message: str


@app.post("/extract_dates/")
def extract_dates_from_text(input_text: InputText) -> OutputResult:
    """
    Endpoint to extract dates from input text.

    Args:
        input_text (InputText): Input text provided by the user.

    Returns:
        OutputResult: Output containing extracted dates and message.
    """
    cleaned_text = preprocess_text(input_text.text)
    extracted_dates = extract_dates(cleaned_text)

    if extracted_dates:
        standardized_dates = standardize_dates(extracted_dates)
        message = "Success"
    else:
        standardized_dates = []
        message = "Warning, dates not extracted correctly"

    return {"dates": standardized_dates, "message": message}

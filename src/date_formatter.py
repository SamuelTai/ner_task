from datetime import datetime
from typing import List


def standardize_dates(dates: List[str]) -> List[str]:
    """
    Standardizes the extracted dates to the dd/mm/yyyy format.

    Args:
        dates (list[str]): List of extracted dates.

    Returns:
        list[str]: List of standardized dates.
    """
    standardized_dates = []
    for date in dates:
        try:
            # Attempt to parse the date using various formats
            date_obj = None
            for fmt in ("%d/%m/%Y", "%d %b %Y", "%d %B %Y", "%d/%b/%Y", "%d/%B/%Y"):
                try:
                    date_obj = datetime.strptime(date, fmt)
                    break
                except ValueError:
                    continue

            # If date is successfully parsed, format it to dd/mm/yyyy
            if date_obj:
                standardized_dates.append(date_obj.strftime("%d/%m/%Y"))
        except ValueError:
            pass
    return standardized_dates
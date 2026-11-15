"""Validate the BERT arXiv page for Abdellah Boudlal, 2026-11."""

import logging

from bs4 import BeautifulSoup

from nlp.config_abdellah import SUBJECTS_SELECTOR
from nlp.stage02_validate import run_validate as run_example_validation


def run_validate(html_content: str, LOG: logging.Logger) -> BeautifulSoup:
    """Validate the standard arXiv fields and the detailed subject cell."""
    soup = run_example_validation(html_content, LOG)

    subjects = soup.select_one(SUBJECTS_SELECTOR)
    if subjects is None or not subjects.get_text(strip=True):
        raise ValueError(f"Missing arXiv subject data in {SUBJECTS_SELECTOR!r}.")

    LOG.info("Detailed arXiv subject cell validated.")
    return soup

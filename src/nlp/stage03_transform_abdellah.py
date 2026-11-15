"""Extract arXiv metadata for Abdellah Boudlal, 2026-11."""

import logging
import re

from bs4 import BeautifulSoup
import pandas as pd

from nlp.config_abdellah import SUBJECTS_SELECTOR
from nlp.stage03_transform import run_transform as run_example_transform


def run_transform(
    soup: BeautifulSoup, LOG: logging.Logger, *, detailed_subjects: bool = False
) -> pd.DataFrame:
    """Extract metadata and add an estimated abstract sentence count."""
    df = run_example_transform(soup, LOG)

    if detailed_subjects:
        subjects = soup.select_one(SUBJECTS_SELECTOR)
        if subjects is not None:
            df["subjects"] = subjects.get_text(" ", strip=True)

    abstract = str(df.at[0, "abstract"])
    fragments = re.split(r"[.!?]+(?=\s|$)", abstract)
    sentence_count = sum(bool(fragment.strip()) for fragment in fragments)

    df["abstract_sentence_count"] = sentence_count if abstract != "unknown" else 0
    LOG.info("Abstract sentence count: %s", df.at[0, "abstract_sentence_count"])
    return df

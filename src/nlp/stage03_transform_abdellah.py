"""Add an abstract sentence count to the EVTL pipeline.

Customized by Abdellah Boudlal, 2026-11.
"""

import logging
import re

from bs4 import BeautifulSoup
import pandas as pd

from nlp.stage03_transform import run_transform as run_example_transform


def run_transform(soup: BeautifulSoup, LOG: logging.Logger) -> pd.DataFrame:
    """Add an estimated sentence count to the extracted paper metadata."""
    df = run_example_transform(soup, LOG)
    abstract = str(df.at[0, "abstract"])

    fragments = re.split(r"[.!?]+(?=\s|$)", abstract)
    sentence_count = sum(bool(fragment.strip()) for fragment in fragments)

    df["abstract_sentence_count"] = sentence_count if abstract != "unknown" else 0
    LOG.info("Abstract sentence count: %s", df.at[0, "abstract_sentence_count"])
    return df

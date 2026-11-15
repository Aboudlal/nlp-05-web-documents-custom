"""Configure the BERT arXiv source for Abdellah Boudlal, 2026-11."""

from nlp.config import PROCESSED_PATH, RAW_PATH

PAGE_URL = "https://arxiv.org/abs/1810.04805"
RAW_HTML_PATH = RAW_PATH / "abdellah_bert_raw.html"
PROCESSED_CSV_PATH = PROCESSED_PATH / "abdellah_bert.csv"
SUBJECTS_SELECTOR = "td.subjects"

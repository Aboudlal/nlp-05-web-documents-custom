"""Run the Phase 4 pipeline for Abdellah Boudlal, 2026-11."""

from datafun_toolkit.logger import get_logger

from nlp.config import HTTP_REQUEST_HEADERS, PAGE_URL, PROCESSED_PATH, RAW_PATH
from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform_abdellah import run_transform
from nlp.stage04_load import run_load


def main() -> None:
    """Process the example paper and save the Phase 4 results."""
    log = get_logger("NLP05", level="INFO")
    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    raw_path = RAW_PATH / "abdellah_phase4_raw.html"
    csv_path = PROCESSED_PATH / "abdellah_phase4.csv"

    html = run_extract(PAGE_URL, HTTP_REQUEST_HEADERS, raw_path, log)
    soup = run_validate(html, log)
    df = run_transform(soup, log)
    run_load(df, csv_path, log)


if __name__ == "__main__":
    main()

"""Run the custom EVTL pipeline for Abdellah Boudlal, 2026-11."""

import argparse

from datafun_toolkit.logger import get_logger

from nlp import config, config_abdellah
from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate as run_example_validation
from nlp.stage02_validate_abdellah import run_validate
from nlp.stage03_transform_abdellah import run_transform
from nlp.stage04_load import run_load


def main() -> None:
    """Process BERT by default or run the example for Phase 4."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--example", action="store_true", help="Run Phase 4 on Agents of Chaos."
    )
    args = parser.parse_args()

    if args.example:
        page_url = config.PAGE_URL
        raw_path = config.RAW_PATH / "abdellah_phase4_raw.html"
        csv_path = config.PROCESSED_PATH / "abdellah_phase4.csv"
        validate = run_example_validation
    else:
        page_url = config_abdellah.PAGE_URL
        raw_path = config_abdellah.RAW_HTML_PATH
        csv_path = config_abdellah.PROCESSED_CSV_PATH
        validate = run_validate

    log = get_logger("NLP05", level="INFO")
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    html = run_extract(page_url, config.HTTP_REQUEST_HEADERS, raw_path, log)
    soup = validate(html, log)
    df = run_transform(soup, log, detailed_subjects=not args.example)
    run_load(df, csv_path, log)


if __name__ == "__main__":
    main()

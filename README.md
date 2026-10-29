# V4Career — Clean Deployment Package

## Included scope

- Existing Flask UI and frontend assets are preserved as supplied.
- Portal catalog contains only the 16 requested portals: Cutshort, Foundit, Glassdoor, Shine.com, Wellfound, Hirist, iimjobs, TimesJobs, Freshersworld, Jooble, National Career Service (NCS), Indeed, Naukri, Internshala, PlacementIndia, and QuikrJobs.
- Company career catalog contains only Amazon, Infosys, and Deloitte.
- `scripts/run_source_apify.py` and `scripts/run_jobspy.py` are preserved byte-for-byte from the uploaded package.
- Production database schemas/indexes and required collector modules are retained.
- Scraping output CSVs, logs, cached bytecode, old backups, experimental inspection files, duplicate setup notes, and unrelated legacy runner scripts are excluded.

## Setup

1. Create a virtual environment and install dependencies: `pip install -r requirements.txt`.
2. Copy `.env.example` to `.env` and fill in your own database, Flask login, and required Actor settings. The actual `.env` was deliberately excluded to protect credentials.
3. Apply the PostgreSQL schema and performance indexes to the intended Neon database only if they have not already been applied. Do not rerun schema-changing SQL blindly on production.
4. Start locally with `python app.py` or host using `gunicorn wsgi:app`.

## Collection entry points

- Portal collectors: `python scripts/run_source_apify.py --help`
- JobSpy: `python scripts/run_jobspy.py --help`
- Official company careers: `python scripts/run_company_career_structured.py --source AMAZON` (also `INFOSYS`, `DELOITTE`)
- Batch company run: `python scripts/run_company_careers_structured_batch.py --help`

## Notes

Portal visibility does not guarantee that an Actor is configured or permitted to run. Keep `APIFY_ACCESS_APPROVED_<KEY>` false until the Actor input, current pricing, terms, and authorization are reviewed. JobSpy only collects from the sources supported by that library.

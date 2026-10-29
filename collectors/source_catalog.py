"""V4Career's intentionally scoped job-portal catalog.

Only portals approved for display in this deployment are listed here. Actor
configuration and approval are separate from UI visibility.
"""

JOB_PORTALS = [{'name': 'Cutshort', 'base_url': 'https://cutshort.io/', 'key': 'CUTSHORT', 'popular': False}, {'name': 'Foundit', 'base_url': 'https://www.foundit.in', 'key': 'FOUNDIT', 'popular': True}, {'name': 'Glassdoor', 'base_url': 'https://www.glassdoor.co.in/Job', 'key': 'GLASSDOOR', 'popular': False}, {'name': 'Shine.com', 'base_url': 'https://www.shine.com/', 'key': 'SHINE_COM', 'popular': False}, {'name': 'Wellfound', 'base_url': 'https://wellfound.com', 'key': 'WELLFOUND', 'popular': False}, {'name': 'Hirist', 'base_url': 'https://www.hirist.tech/', 'key': 'HIRIST', 'popular': False}, {'name': 'iimjobs', 'base_url': 'https://www.iimjobs.com/', 'key': 'IIMJOBS', 'popular': False}, {'name': 'TimesJobs', 'base_url': 'https://www.timesjobs.com', 'key': 'TIMESJOBS', 'popular': True}, {'name': 'Freshersworld', 'base_url': 'https://www.freshersworld.com/', 'key': 'FRESHERSWORLD', 'popular': False}, {'name': 'Jooble', 'base_url': 'https://in.jooble.org/', 'key': 'JOOBLE', 'popular': False}, {'name': 'National Career Service (NCS)', 'base_url': 'https://www.ncs.gov.in/', 'key': 'NATIONAL_CAREER_SERVICE_NCS', 'popular': False}, {'name': 'Indeed', 'base_url': 'https://in.indeed.com', 'key': 'INDEED', 'popular': True}, {'name': 'Naukri', 'base_url': 'https://www.naukri.com', 'key': 'NAUKRI', 'popular': True}, {'name': 'Internshala', 'base_url': 'https://internshala.com', 'key': 'INTERNSHALA', 'popular': False}, {'name': 'PlacementIndia', 'base_url': 'https://www.placementindia.com/', 'key': 'PLACEMENTINDIA', 'popular': False}, {'name': 'QuikrJobs', 'base_url': 'https://www.quikr.com/jobs', 'key': 'QUIKRJOBS', 'popular': False}]

UI_PORTAL_KEYS = {p["key"] for p in JOB_PORTALS}
PORTAL_BY_KEY = {item["key"].lower(): item for item in JOB_PORTALS}
PORTAL_BY_NAME = {item["name"].strip().lower(): item for item in JOB_PORTALS}

# Candidate Actor IDs retained only for the configured portal scope.
# Approval flags and input schemas must still be verified in .env / Apify.
DEFAULT_APIFY_ACTORS = {'NAUKRI': 'automation-lab~naukri-scraper', 'INDEED': 'unfenced-group~indeed-in-scraper', 'FOUNDIT': 'deriverge~foundit-jobs-scraper', 'INTERNSHALA': 'automation-lab~internshala-scraper', 'TIMESJOBS': 'unfenced-group~timesjobs-scraper', 'WELLFOUND': 'cprussin~wellfound-jobs', 'CUTSHORT': 'silentflow~cutshort-jobs-scraper', 'HIRIST': 's_actors~hirist-jobs-scraper', 'SHINE_COM': 'bovi~shine-scraper', 'IIMJOBS': 'silentflow~iimjobs-scraper', 'GLASSDOOR': 'hgservices~glassdoor-jobs-scraper', 'FRESHERSWORLD': 'shahidirfan~freshersworld-jobs-scraper', 'NATIONAL_CAREER_SERVICE_NCS': 'jobsapi~ncs-jobs-search-scraper', 'JOOBLE': 'ahmed_jasarevic~jooble-scraper', 'QUIKRJOBS': 'jobsapi~quikr-jobs-search-scraper', 'PLACEMENTINDIA': 'fervent_bus~placementindia-scraper'}

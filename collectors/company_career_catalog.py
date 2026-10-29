"""Official career-page sources enabled for this V4Career deployment."""

COMPANY_CAREER_SOURCES = [{'name': 'Amazon Jobs', 'company': 'Amazon', 'base_url': 'https://www.amazon.jobs/en/search?country=IND&loc_query=India', 'key': 'AMAZON', 'allowed_hosts': ['www.amazon.jobs', 'amazon.jobs'], 'discovery_urls': ['https://www.amazon.jobs/en/search?country=IND&loc_query=India'], 'verified_collector': True}, {'name': 'Infosys Careers', 'company': 'Infosys', 'base_url': 'https://career.infosys.com/jobs?countrycode=IN', 'key': 'INFOSYS', 'allowed_hosts': ['career.infosys.com'], 'discovery_urls': ['https://career.infosys.com/joblist?companyhiringtype=&countrycode=IN'], 'verified_collector': True}, {'name': 'Deloitte India Careers', 'company': 'Deloitte', 'base_url': 'https://southasiacareers.deloitte.com/', 'key': 'DELOITTE', 'allowed_hosts': ['southasiacareers.deloitte.com'], 'discovery_urls': ['https://southasiacareers.deloitte.com/'], 'verified_collector': True}]

COMPANY_CAREER_BY_KEY = {item["key"]: item for item in COMPANY_CAREER_SOURCES}
COMPANY_CAREER_BY_NAME = {item["name"].casefold(): item for item in COMPANY_CAREER_SOURCES}
COMPANY_CAREER_BY_COMPANY = {item["company"].casefold(): item for item in COMPANY_CAREER_SOURCES}

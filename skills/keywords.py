import re

# Define skills
SKILL_KEYWORDS = [
    "SQL", "VBA", "Snowflake", "Python", "Databricks", "ELT", "ETL", "governance", "data modeling", "scalability", "ingestion", 
    "ELK", "JSON", "Kubernetes", "Bash", "ingestion pipelines", "Prometheus", "ML", "alerting", "architect", 
    "AWS", "GCP", "Tableau", "MSSQL", "Node.js", "react", "managed", "manager", "predictive ML", "Grafana", "OCI", "metric governance", "devsecops", "MLOps", "Agile",
    "docker", "Azure", "data analysis", "data scientist", "data engineer", "linux","forecasting", "data modeling", "scalability", "JSON"
]

def extract_skills(text):
    """
    Extract defined skills found in a given block of text.
    Returns:
        list: Skills found in the text.
    """
    found_skills = []
    text_lower = text.lower()

    for skill in SKILL_KEYWORDS:
        # Escape special characters
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    return found_skills

from skills.keywords import extract_skills

sample_job_text = """
We are looking for a data engineer experienced in Databricks, Snowflake, AWS, GCP, ELT pipelines, and scalable architectures.
Familiarity with ML, governance, and working as an architect or data scientist is a plus. Scalability and efficient data modeling are critical.
"""

resume_text = """
Experienced in AWS, GCP, Databricks, ML, and governance frameworks. 
Strong leadership as a manager and architect with experience in data engineering.
"""

job_skills = set(extract_skills(sample_job_text))
resume_skills = set(extract_skills(resume_text))
shared_skills = resume_skills & job_skills
missing_skills = job_skills - resume_skills

print("✅ Extracted Job Skills:", job_skills)
print("✅ Extracted Resume Skills:", resume_skills)
print("✅ Shared Skills:", shared_skills)
print("❌ Missing Skills:", missing_skills)

import streamlit as st
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.text_processing import clean_text, load_and_clean_folder
from pipeline.compare import compare_resume_to_jobs
from skills.keywords import extract_skills

# Title
st.title("Job Match Dashboard")

# Upload resume
resume_file = st.file_uploader("Upload your resume (.txt)", type=["txt"])
job_files = st.file_uploader("Upload job descriptions (.txt)", type=["txt"], accept_multiple_files=True)

if resume_file and job_files:
    resume_text = clean_text(resume_file.read().decode("utf-8"))
    resume_skills = set(extract_skills(resume_text))

    results = []
    for job_file in job_files:
        job_text = clean_text(job_file.read().decode("utf-8"))
        job_skills = set(extract_skills(job_text))
        comparison = compare_resume_to_jobs(resume_text, job_text)
        shared_skills = resume_skills.intersection(job_skills)
        missing_skills = job_skills.difference(resume_skills)

        results.append({
            "job_name": job_file.name,
            "similarity": comparison["overall_score"],
            "text_similarity": comparison["text_similarity"],
            "skill_match": comparison["skill_match"],
            "shared_skills": shared_skills,
            "missing_skills": missing_skills,
            "job_skills": job_skills
        })


    # Sort and display results
    sorted_results = sorted(results, key=lambda x: x["similarity"], reverse=True)

    for result in sorted_results:
        st.subheader(result["job_name"])
        st.write(f"**Overall Match**: {result['similarity']:.2f}%")
        st.write(f"**Text Similarity**: {result['text_similarity']:.2f}%")
        st.write(f"**Skill Match**: {result['skill_match']:.2f}%")
        st.write(f"**Shared Skills**: {', '.join(result['shared_skills']) or 'None'}")
        st.write(f"**Missing Skills**: {', '.join(result['missing_skills']) or 'None'}")
        st.write(f"**All Job Skills**: {', '.join(result['job_skills'])}")

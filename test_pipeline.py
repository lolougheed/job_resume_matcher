from pipeline.text_processing import load_and_clean_folder, clean_text
from pipeline.compare import compare_resume_to_jobs

# Set paths
job_folder = "data/jobs/"
resume_path = "data/resume/resume.txt"

# Load and clean resume
with open(resume_path, 'r', encoding='utf-8') as f:
    raw_resume = f.read()
resume_text = clean_text(raw_resume)

# Load and clean job descriptions
jobs = load_and_clean_folder(job_folder)

# Compare each job to the resume
results = []
for job_title, job_text in jobs.items():
    comparison = compare_resume_to_jobs(resume_text, job_text)
    results.append((job_title, comparison))

# Sort results by overall score
results.sort(key=lambda x: x[1]["overall_score"], reverse=True)

# Print detailed results
print("\nMatch Results:\n" + "-" * 40)
for job_title, comparison in results:
    print(f"Job: {job_title}")
    print(f"  Overall Match:   {comparison['overall_score']}%")
    print(f"  Text Similarity: {comparison['text_similarity']}%")
    print(f"  Skill Match:     {comparison['skill_match']}%\n")

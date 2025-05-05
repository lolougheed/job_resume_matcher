from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills.keywords import extract_skills

def compare_resume_to_jobs(resume_text, job_text, weight_text=0.6, weight_skills=0.4):
    """
    Compare a resume and job description using text similarity and skill overlap.

    Args:
        resume_text (str): The text of the resume.
        job_text (str): The text of the job description.
        weight_text (float): Weight for textual similarity.
        weight_skills (float): Weight for skill overlap.

    Returns:
        dict: A dictionary containing text similarity, skill match, and overall score.
    """
    # Textual similarity with TF-IDF
    documents = [resume_text, job_text]
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)
    text_similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

    # Skill overlap
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))
    if job_skills:
        skill_match = (len(resume_skills & job_skills) / len(job_skills)) * 100
    else:
        skill_match = 0.0

    # Final score
    overall_score = (weight_text * text_similarity) + (weight_skills * skill_match)

    return {
        "text_similarity": round(text_similarity, 2),
        "skill_match": round(skill_match, 2),
        "overall_score": round(overall_score, 2)
    }

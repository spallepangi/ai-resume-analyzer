from utils.nlp_analysis import extract_skills_with_bert

def get_missing_skills_with_bert(preprocessed_resume, preprocessed_job_desc):
    """
    Identifies the skills mentioned in the job description but missing from the resume, using BERT.

    Args:
        preprocessed_resume (str): The preprocessed text of the resume.
        preprocessed_job_desc (str): The preprocessed text of the job description.

    Returns:
        missing_skills (list): A list of skills present in the job description but missing in the resume.
    """
    resume_skills = set(extract_skills_with_bert(preprocessed_resume))
    job_desc_skills = set(extract_skills_with_bert(preprocessed_job_desc))
    
    # Identify skills that are in the job description but missing from the resume
    missing_skills = list(job_desc_skills - resume_skills)
    
    return missing_skills

def generate_feedback(missing_skills):
    """
    Generates feedback based on the missing skills.
    
    Args:
        missing_skills (list): A list of missing skills.
        
    Returns:
        feedback (str): Custom feedback to the user.
    """
    if missing_skills:
        num_missing = len(missing_skills)
        feedback = f"The following key skills are missing from your resume: {', '.join(missing_skills)}."
        
        if num_missing > 5:
            feedback += " Consider updating your resume to reflect the essential skills listed in the job description."
        elif num_missing > 2:
            feedback += " These missing skills are important for the role, and adding relevant experience or highlighting them in your resume could increase your chances."
        else:
            feedback += " It seems your resume is closely aligned with the job description, but adding these few skills may further improve it."
    else:
        feedback = "Great! Your resume closely matches the key skills mentioned in the job description."
    
    return feedback

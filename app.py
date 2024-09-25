import streamlit as st
from utils.text_extraction import extract_text_from_pdf, extract_text_from_word
from utils.feedback import get_missing_skills_with_bert, generate_feedback
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Analyzer Tool")

# File uploader for resume
uploaded_file = st.file_uploader("Upload Resume (PDF/Word)", type=["pdf", "docx"], key="resume_uploader")

# Text input for job description
job_desc_text = st.text_area("Paste Job Description Text Here", height=250)

# Add the "Analyze" button, always visible
analyze_button = st.button("Analyze")

# Check if both resume and job description are present and if the button was clicked
if analyze_button:
    if uploaded_file is None:
        st.error("Please upload a resume.")
    elif not job_desc_text:
        st.error("Please paste the job description.")
    else:
        # Handle Resume File
        file_type = uploaded_file.name.split('.')[-1]
        
        # Extract text from resume based on file type
        if file_type == "pdf":
            try:
                resume_text = extract_text_from_pdf(uploaded_file)  # Use file-like object
            except Exception as e:
                st.error(f"Error extracting text from PDF: {e}")
                resume_text = ""
        elif file_type == "docx":
            try:
                resume_text = extract_text_from_word(uploaded_file)
            except Exception as e:
                st.error(f"Error extracting text from Word document: {e}")
                resume_text = ""

        # Proceed only if resume text is extracted successfully
        if resume_text:
            try:
                # Get missing skills using BERT
                missing_skills = get_missing_skills_with_bert(resume_text, job_desc_text)

                # Generate feedback
                feedback = generate_feedback(missing_skills)
                
                # Display feedback only (no extracted text)
                st.subheader("Feedback and Recommendations")
                st.write(feedback)
            except Exception as e:
                st.error(f"Error during BERT skill extraction or feedback generation: {e}")

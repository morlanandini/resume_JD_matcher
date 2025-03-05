import streamlit as st
import pymupdf
from scripts.llm import ask_llm, validate_json

st.title("Resume Matching Analysis")
st.write("Upload a resume in PDF format and provide a job description to analyze the match percentage and get improvement suggestions.")

uploaded_file = st.file_uploader("Choose a resume (PDF format)")
job_description = st.text_area("Paste the job description")

if uploaded_file is not None and job_description:
    if st.button("Analyze Match"):
        bytearray = uploaded_file.read()
        pdf = pymupdf.open(stream=bytearray, filetype="pdf")

        resume_text = ""
        for page in pdf:
            resume_text += "\n\n" + page.get_text()
        pdf.close()

        analysis_prompt = f"""
        You are an AI job resume analyzer. Compare the following resume with the job description.
        Calculate the match percentage and provide suggestions for improvement.
        
        Resume:
        {resume_text}
        
        Job Description:
        {job_description}
        
        Provide a valid JSON output with the following format:
        {{
            "match_percentage": "<calculated percentage>",
            "improvement_suggestions": ["<suggestion 1>", "<suggestion 2>", ...]
        }}
        """

        with st.spinner("Analyzing Resume..."):
            response = ask_llm(context=resume_text, question=analysis_prompt)
        
        with st.spinner("Validating JSON..."):
            response = validate_json(response)
        
        st.write("**Match Percentage:**", response.get("match_percentage", "N/A"))
        st.write("**Suggestions for Improvement:**")
        st.write(response.get("improvement_suggestions", []))
        
        st.balloons()

# Resume Matching Analysis Tool  

The **Resume Matching Analysis Tool** is a Streamlit-based application designed to help job seekers optimize their resumes for specific job descriptions. By leveraging **Natural Language Processing (NLP)** and **Large Language Models (LLMs)**, the tool analyzes resumes and compares them to job descriptions, providing a **match percentage** and actionable suggestions for improvement.  

## 🚀 Features  

- **📄 Resume Upload:** Upload your resume in **PDF** format.  
- **📝 Job Description Input:** Paste the job description you’re targeting.  
- **📊 Match Percentage:** Get a score indicating how well your resume aligns with the job description.  
- **🔍 Improvement Suggestions:** Receive actionable recommendations to enhance your resume.  
- **💡 User-Friendly Interface:** Built with **Streamlit** for an intuitive and interactive experience.  

## 🛠️ Tech Stack  

- **Frontend:** Streamlit  
- **Backend:** Python, LangChain, Ollama  
- **Libraries:** PyMuPDF (Fitz), PDFPlumber, JSON, NLP (Spacy/NLTK - optional)  
- **LLMs:** Llama 3, Qwen (or similar models for analysis)  

## ⚙️ How It Works  

1. **Upload Your Resume** → Upload your resume (PDF format).  
2. **Paste the Job Description** → Input the job description you’re applying for.  
3. **Analyze Match** → Click the “Analyze Match” button to compare both.  
4. **View Results** → Get a match percentage and tailored improvement suggestions.  

## 🖥️ Installation  

### 1️⃣ Clone the Repository  
git clone https://github.com/your-username/resume-matching-tool.git
cd resume-matching-tool


2️⃣ Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run app.py

5️⃣ Access the Tool
Open your browser and navigate to:
🔗 http://localhost:8501

📌 Usage
Upload a Resume: Upload your resume in PDF format.
Paste Job Description: Copy and paste the job description into the provided text area.
Analyze Match: Click the "Analyze Match" button to start the analysis.
Review Results: View the match percentage and improvement suggestions.

📊 Example Output
Match Percentage: 85%

🔹 Suggestions for Improvement:
- Highlight specific projects where you used Three.js and WebGL.
- Emphasize your experience with cross-functional collaboration.
- Include metrics or outcomes from your previous projects.





import streamlit as st
import fitz  
import spacy
from serpapi import GoogleSearch
import urllib.parse

# Set up the Streamlit app
st.set_page_config(page_title="Engineering Job Finder", layout="centered")

# Load the language model
nlp = spacy.load("en_core_web_md")

# List of skills to search for
skills_to_look_for = [
    "catia", "siemens nx", "autocad", "webots", "matlab", "simulink", "ros", "arduino," "plc", "codesys", "python", "c++"
]

# Function to read text from uploaded PDF
def get_text_from_pdf(file):
    pdf_file = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf_file:
        text += page.get_text()
    return text

# Function to find skills in the resume text
def find_skills_in_text(text):
    text_doc = nlp(text.lower())
    found_skills = []
    for token in text_doc:
        if token.text in skills_to_look_for:
            found_skills.append(token.text)
    return list(set(found_skills))  # Remove duplicates

# Function to search for jobs based on skills
def find_jobs(skills, location="United Kingdom"):
    jobs_list = []

    if not skills:
        skills = ["Graduate Robotics engineer"]  

    for skill in skills:
        search_query = f"entry level {skill} jobs in {location}"

        params = {
            "engine": "google_jobs",
            "q": search_query,
            "location": location,
            "api_key": "API KEY HERE",  # Replace with your actual API key
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()

            job_results = results.get("jobs_results", [])

            if job_results:
                job = job_results[0] 
                jobs_list.append({
                    "skill": skill,
                    "title": job.get("title", "No title found"),
                    "company": job.get("company_name", "No company found"),
                    "location": job.get("location", "No location found")
                })

        except Exception as e:
            st.warning(f"Could not find jobs for {skill}: {e}")

    return jobs_list

# Streamlit App UI

st.title("📄 Engineering Job Finder")

uploaded_resume = st.file_uploader("Upload your CV (PDF)", type=["pdf"])

if uploaded_resume:
    with st.spinner("Reading your CV..."):
        resume_text = get_text_from_pdf(uploaded_resume)

    st.subheader("Skills Found")
    found_skills = find_skills_in_text(resume_text)

    if found_skills:
        st.success(", ".join(found_skills))
    else:
        st.warning("No skills found in your CV.")

    find_jobs_button = st.button("🔍 Find Jobs for Me")

    if find_jobs_button:
        with st.spinner("Searching for jobs..."):
            matching_jobs = find_jobs(found_skills)

        if matching_jobs:
            st.subheader("Job Suggestions for You")
            for job in matching_jobs:
                st.write(f"**Job Title:** {job['title']}")
                st.write(f"**Company:** {job['company']}")
                st.write(f"**Location:** {job['location']}")

                # Create a Google search link for the job
                search_query = f"{job['title']} at {job['company']}"
                encoded_query = urllib.parse.quote(search_query)
                search_link = f"https://www.google.com/search?q={encoded_query}"
                st.markdown(f"[Search and Apply Here]({search_link})", unsafe_allow_html=True)
                st.write("---")
        else:
            st.info("No jobs found. Try uploading a different CV.")

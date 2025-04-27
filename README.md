# 📄 Engineering Job Finder

A **Streamlit** web application that helps engineering graduates find **entry-level jobs** based on the skills extracted from their **CV (PDF)**.  
It uses **Natural Language Processing (NLP)** with **spaCy** to detect technical skills and then searches for matching job listings using the **SerpApi** Google Jobs engine.

## 🚀 Features

- Upload your **CV** (PDF format only)
- Automatically extract relevant **engineering and software skills**
- Find **entry-level job opportunities** in the **United Kingdom**
- Get clickable links to apply directly through Google Search

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [spaCy](https://spacy.io/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [SerpApi](https://serpapi.com/)
- [Python 3.8+](https://www.python.org/)

## 📂 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/engineering-job-finder.git
   cd engineering-job-finder
   ```

2. **Install dependencies**

   It is recommended to use a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you have the following key packages installed:
   - streamlit
   - pymupdf
   - spacy
   - serpapi

3. **Download spaCy model**

   ```bash
   python -m spacy download en_core_web_md
   ```

4. **Set up your SerpApi API key**

   - Sign up for a [SerpApi account](https://serpapi.com/users/sign_up) if you do not have one.
   - Replace `"API KEY HERE"` in the code with your actual API key.

5. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

## 📄 Requirements

- Python 3.8+
- A free (or paid) SerpApi account and API key
- A CV in **PDF** format containing your skills

## 🧠 Skills Recognised

The app can currently detect the following skills:

- catia
- siemens nx
- autocad
- webots
- matlab
- simulink
- ros
- arduino
- plc
- codesys
- python
- c++

_(More skills can easily be added by editing the `skills_to_look_for` list in the code.)_

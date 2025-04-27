# 📄 Engineering Job Finder

A **Streamlit** web application that helps engineering graduates find **entry-level jobs** based on the skills extracted from their **CV (PDF)**.  
It uses **Natural Language Processing** with **spaCy** to detect technical skills and then searches for matching job listings using the **SerpApi** Google Jobs engine.

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
   git clone https://github.com/Spades2002/Other-Project-2
   cd engineering-job-finder
   ```

2. **Open the project in your code editor**

   - Open **Visual Studio Code** (or any other code editor you prefer).
   - Select **File > Open Folder** and choose the project folder.

3. **Install the dependencies**

   You can install the required dependencies directly by running the following command in your terminal:

   ```bash
   pip install streamlit spacy pymupdf serpapi
   ```

4. **Download the spaCy model**

   Download the necessary spaCy language model:

   ```bash
   python -m spacy download en_core_web_md
   ```

5. **Set up your SerpApi API key**

   - Sign up for a [SerpApi account](https://serpapi.com/users/sign_up) if you do not have one.
   - In the code, replace `"API KEY HERE"` with your actual API key.

6. **Run the Streamlit app**

   To launch the app, run:

   ```bash
   streamlit run app.py
   ```

7. **View the application**

   After running the above command, a local web page will open (usually at `http://localhost:8501/`) where you can interact with the app.

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

## 💬 Notes

- If Streamlit does not open automatically, you can manually visit the URL printed in your terminal (usually `http://localhost:8501/`).
- You can freely customise the skills list and improve the job search by adjusting the code.

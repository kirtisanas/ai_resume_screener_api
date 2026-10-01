# AI Resume Screener API

A backend API that analyzes a resume against a job description and calculates a similarity score using Natural Language Processing (NLP).

The system extracts text from PDF resumes, compares the resume with a job description using TF-IDF and cosine similarity, identifies matching and missing skills, and stores analysis results in SQLite.

## Features

- Upload PDF resumes
- Extract text from PDF files
- Compare resumes with job descriptions
- Calculate resume-job similarity score
- Identify matching skills
- Identify missing skills
- Store analysis results using SQLite
- View analysis history
- Retrieve individual analysis results
- Input validation and error handling
- Interactive API documentation using Swagger UI

## Technologies Used

- Python
- FastAPI
- Uvicorn
- scikit-learn
- TF-IDF
- Cosine Similarity
- pypdf
- SQLite
- REST API

## How It Works

```text
PDF Resume
    ↓
Text Extraction
    ↓
Resume Text + Job Description
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Match Score
    ↓
Skill Matching
    ↓
SQLite Database
    ↓
Analysis Result
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check API status |
| POST | `/upload-resume` | Upload and extract resume text |
| POST | `/analyze` | Analyze resume against a job description |
| GET | `/history` | View previous analyses |
| GET | `/results/{analysis_id}` | Retrieve a specific analysis |

## Swagger UI

The API provides interactive documentation using Swagger UI.

![Swagger UI](./swagger_ui.png)

## Example Analysis Response

```json
{
  "analysis_id": 1,
  "filename": "resume.pdf",
  "match_score": 72.45,
  "matching_skills": [
    "python",
    "sql",
    "pandas"
  ],
  "missing_skills": [
    "tableau"
  ],
  "message": "Resume analyzed and saved successfully"
}
```

## Matching Approach

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert the resume and job description into numerical vectors.

Then, **cosine similarity** is used to measure how similar the two texts are.

The similarity value is converted into a percentage-style match score.

The project also checks skills mentioned in the job description against the skills found in the resume to identify matching and missing skills.

## Project Structure

```text
ai_resume_screener_api/
│
├── app/
│   ├── main.py
│   ├── matcher.py
│   └── database.py
│
├── .gitignore
├── README.md
├── swagger_ui.png
└── resume_screener.db
```

> The local SQLite database and virtual environment are excluded from Git using `.gitignore`.

## Installation

Clone the repository:

```bash
git clone https://github.com/kirtisanas/ai_resume_screener_api.git
```

Go into the project folder:

```bash
cd ai_resume_screener_api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn python-multipart pypdf scikit-learn
```

## Run the API

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, you can test all available API endpoints interactively.

## Future Improvements

- Improve automatic skill extraction
- Add more advanced NLP techniques
- Add resume section extraction
- Add job-role recommendations
- Add authentication
- Add a web-based frontend
- Add automated testing
- Deploy the API to the cloud

## Author

**Kirti Sanas**

M.Sc. Information Technology Student | BSc IT Graduate

Interested in Data, Machine Learning, APIs and Software Development.
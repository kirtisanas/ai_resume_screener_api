from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from pypdf import PdfReader
from app.matcher import calculate_match_score, find_skills
from app.database import ( create_table, save_analysis,get_all_analyses,get_analysis_by_id
)
import io

app = FastAPI(
    title="AI Resume Screener API",
    description="API for analyzing resumes against job descriptions",
    version="1.0.0"
)

create_table()

@app.get("/")
def home():
    return {
        "message": "AI Resume Screener API is running!"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()

    reader = PdfReader(io.BytesIO(contents))

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully",
        "text": text
    }


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form("")
):
    # 1. Check if file is a PDF
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF resume."
        )

    # 2. Check if job description is empty
    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    # 3. Read the PDF
    contents = await file.read()

    try:
        reader = PdfReader(io.BytesIO(contents))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted PDF file."
        )

    # 4. Extract resume text
    resume_text = ""

    for page in reader.pages:
        resume_text += page.extract_text() or ""

    # 5. Check if text was extracted
    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the resume."
        )

    # 6. Calculate match score
    score = calculate_match_score(
        resume_text,
        job_description
    )

    # 7. Find matching and missing skills
    matching_skills, missing_skills = find_skills(
        resume_text,
        job_description
    )

    # 8. Save analysis to database
    analysis_id = save_analysis(
        file.filename,
        score,
        matching_skills,
        missing_skills
    )

    # 9. Return result
    return {
        "analysis_id": analysis_id,
        "filename": file.filename,
        "match_score": score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "message": "Resume analyzed and saved successfully"
    }
@app.get("/history")
def history():
    return {
        "analyses": get_all_analyses()
    }
@app.get("/results/{analysis_id}")
def get_result(analysis_id: int):
    result = get_analysis_by_id(analysis_id)

    if result is None:
        return {
            "message": "Analysis not found"
        }

    return {
        "analysis": result
    }
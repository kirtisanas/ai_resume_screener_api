from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS = [
    # Programming
    "python",
    "java",
    "javascript",
    "c++",
    "c#",

    # Database
    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    # Data
    "excel",
    "power bi",
    "tableau",
    "pandas",
    "numpy",
    "data analysis",
    "data visualization",

    # Machine Learning
    "machine learning",
    "scikit-learn",
    "tensorflow",
    "pytorch",

    # Web / API
    "fastapi",
    "flask",
    "django",
    "rest api",
    "html",
    "css",

    # Development tools
    "git",
    "github"
]


def calculate_match_score(resume_text: str, job_description: str):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    score = round(similarity * 100, 2)

    return score


def find_skills(resume_text: str, job_description: str):
    resume_lower = resume_text.lower()
    job_lower = job_description.lower()

    matching_skills = []
    missing_skills = []

    for skill in SKILLS:

        if skill in job_lower:

            if skill in resume_lower:
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)

    return matching_skills, missing_skills
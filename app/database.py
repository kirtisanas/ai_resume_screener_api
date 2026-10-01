import sqlite3
from datetime import datetime

DATABASE = "resume_screener.db"


def create_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_name TEXT,
            match_score REAL,
            matching_skills TEXT,
            missing_skills TEXT,
            created_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    resume_name,
    match_score,
    matching_skills,
    missing_skills
):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses
        (resume_name, match_score, matching_skills, missing_skills, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        resume_name,
        match_score,
        ", ".join(matching_skills),
        ", ".join(missing_skills),
        datetime.now().isoformat()
    ))

    connection.commit()

    analysis_id = cursor.lastrowid

    connection.close()

    return analysis_id


def get_all_analyses():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM analyses
        ORDER BY id DESC
    """)

    results = cursor.fetchall()

    connection.close()

    return [dict(row) for row in results]


def get_analysis_by_id(analysis_id):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM analyses
        WHERE id = ?
    """, (analysis_id,))

    result = cursor.fetchone()

    connection.close()

    if result:
        return dict(result)

    return None
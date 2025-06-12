from db import get_connection
from utils import calculate_total_avg, calculate_grade

def insert_student():
    conn = get_connection()
    cursor = conn.cursor()
    id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    c_language = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))
    total, average = calculate_total_avg(english, c_language, python)
    grade = calculate_grade(average)
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, name, english, c_language, python, total, average, grade, 0))
    conn.commit()
    conn.close()

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    id = input("삭제할 학생의 학번: ")
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

def search_student():
    conn = get_connection()
    cursor = conn.cursor()
    keyword = input("검색할 학번 또는 이름: ")
    cursor.execute("SELECT * FROM students WHERE id=? OR name=?", (keyword, keyword))
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def calculate_rank():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, total FROM students ORDER BY total DESC")
    rows = cursor.fetchall()
    rank = 1
    for id, _ in rows:
        cursor.execute("UPDATE students SET rank=? WHERE id=?", (rank, id))
        rank += 1
    conn.commit()
    conn.close()

def count_over_80():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM students WHERE average >= 80")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"80점 이상 평균을 받은 학생 수: {count}명")
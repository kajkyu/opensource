from db import get_connection
from models import calculate_rank

def display_all():
    calculate_rank()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY rank ASC")
    rows = cursor.fetchall()
    print("학번 | 이름 | 영어 | C | 파이썬 | 총점 | 평균 | 학점 | 등수")
    for row in rows:
        print(" | ".join(map(str, row)))
    conn.close()

def sort_by_total():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY total DESC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
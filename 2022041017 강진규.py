def grade(score):
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'
    
    students=[]
    for i in range(5):
        data=input(f"{i+1}번째 학생의 이름, 영어성적, C언어 성적, 파이썬 성적을 입력하세요:")
        name, english, c_language, python=data.split(',')
        english=int(english)
        c_language=int(c_language)
        python=int(python)
        total=english + c_language + python
        aberage=total/3
        grade_L=grade(average)
        student_inf=[name,english,c_language,python,total,average,grade_L]
        students.append(student_inf)

        students=sorted(students, key=lambda x:x[4],reverse=True)

        for i in range(5):
            print(f"{i+1}등: {students[i][0]}, 총점: {students[i][4]}, 평균: {students[i][5]:.2f}, 학점: {students[i][6]}")
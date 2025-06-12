def add_student():
    stdnum=input("학번: ")
    stdname=input("이름: ")
    engs=input("영어: ")
    clans=input("C-언어: ")
    pys=input("파이썬: ")
    engs=int(engs)
    clans=int(clans)
    pys=int(pys)
    return [stdnum,stdname,engs,clans,pys]

def totave(stdstat):
    for i in range(5):
        total=stdstat[2]+stdstat[3]+stdstat[4]
        ave=total/3
        stdstat.append(total)
        stdstat.append(ave)
        return stdstat
    
def grade(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'
    
def sortstd(stdstat):
    return sorted(stdstat, key=lambda x: x[5],reverse=True)

students=[]

for i in range(5):
    print(f"{i+1}번째 학생의 정보를 입력하세요.")
    student=add_student()
    student=totave(student)
    student.append(grade(student[6]))
    students.append(student)
    
students=sortstd(students)

print("\t\t\t\t성적관리 프로그램\n")
print("===============================================\n")
print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("===============================================\n")
for i in range(5):
    print(f"{students[i][0]}  {students[i][1]}\t{students[i][2]}\t{students[i][3]}\t{students[i][4]}\t{students[i][5]}\t{students[i][6]:.2f}\t{students[i][7]}\n")
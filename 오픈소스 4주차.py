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

def plus_student():
    student=add_student()
    student=totave(student)
    student.append(grade(student[6]))
    return student

def rem_student(num,student,SIZE):
    for i in range(SIZE):
        if(num==student[i][0]):
            del student[i]
            break

def count(average):
    x=0
    for i in range(5):
        if(average[i][6]>=80):
            x+=1
    return x

def find_student(student,SIZE):
    num=input("찾으려는 학생의 학번: ")
    name=input("찾으려는 학생의 이름: ")
    k=0
    for i in range(SIZE):
        if(num==student[i][0]and name==student[i][1]):
            print(f"찾는 학생의 영어 점수는 {student[i][2]}, C-언어 점수는 {student[i][3]}, 파이썬 점수는 {student[i][4]}, 평균 점수는 {student[i][6]:.2f}, 학점은 {student[i][7]}입니다.")
            k+=1
            break
    if k==0:
        print("해당 학생의 정보가 없습니다.")

students=[]

for i in range(5):
    print(f"{i+1}번째 학생의 정보를 입력하세요.")
    student=add_student()
    student=totave(student)
    student.append(grade(student[6]))
    students.append(student)
    
students=sortstd(students)
n=count(students)
menu=0
x=5

print("\t\t\t\t성적관리 프로그램\n")
print("===============================================\n")
print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("===============================================\n")
for i in range(5):{
    print(f"{students[i][0]}  {students[i][1]}\t{students[i][2]}\t{students[i][3]}\t{students[i][4]}\t{students[i][5]}\t{students[i][6]:.2f}\t{students[i][7]}\n")
}
print("80점 이상인 학생의 수: %d"%n)
while menu!=9:
    print("----------------------------------")
    print("1.학생 정보 추가")
    print("2.학생 정보 삭제")
    print("3.학생 찾기")
    print("9.종료")
    menu=int(input("메뉴를 선택하세요: "))
    if menu==1:
        student=plus_student()
        students.insert(x+1,student)
        x+=1
    if menu==2:
        delnum=input("지우고 싶은 학생의 학번: ")
        rem_student(delnum,students,x)
        x-=1
    if menu==3:
        find_student(students,x)
#학생 정보 관리 파일
#manage.py
from student import Student

class Managing:
    def __init__(self):
        self.students=[]

    def add_student(self,student): #학생 목록 추가
        self.students.append(student)
        self.cal_rank()

    def input_student(self,count=5): #기본적으로 5명 추가
        for _ in range(count):
            student=self.get_student_input()
            self.add_student(student)

    def get_student_input(self): #학생 정보 입력
        stdnum=input("학번: ")
        stdname=input("이름: ")
        engs=int(input("영어: "))
        clans=int(input("C-언어: "))
        pys=int(input("파이썬: "))
        return Student(stdnum, stdname, engs, clans, pys)
    
    def cal_rank(self): #등수 계산
        for student in self.students:
            student.rank=1
            for other in self.students:
                if (other.total>student.total):
                    student.rank+=1
    
    def __str__(self): #정보 출력
        result = "\n학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수\n"
        for student in self.students:
            result += str(student) + "\n"  # student.__str__()이 호출됨
        return result
        

    def delete_student(self,stdnum): #학생 정보 삭제
        for i, student in enumerate(self.students):
            if(student.stdnum==stdnum):
                del self.students[i]
                print("삭제되었습니다.")
                self.cal_rank()
                return #break를 쓰면 아래의 print는 계속 반복되므로 return 사용으로 함수 자체를 끝낸다
        print("해당 학번은 없습니다.")
    
    def search_student(self,stdnum): #학생 정보 찾기
        for student in self.students:
            if student.stdnum==stdnum:
                print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print(student)
                return
        print("해당 학번의 학생은 없습니다.")

    def sort_by_total(self): #점수대로 정렬
        self.students.sort(key=lambda s:s.total, reverse=True)
        self.cal_rank()
        print("총점 기준으로 정렬 완료")

    def count_avg_80(self): #평균이 80점 이상인 학생 수 계산
        count=sum(1 for s in self.students if s.avg>80)
        print(f"평균 80점 이상인 학생의 수: {count}")

#학생 정보를 저장할 클래스 만들기
#student.py
class Student:
    def __init__(self, stdnum, stdname, engs, clans, pys): #학생 정보를 저장할 클래스
        self.stdnum=stdnum
        self.stdname=stdname
        self.engs=engs
        self.clans=clans
        self.pys=pys
        self.total=0
        self.avg=0.0
        self.grade=''
        self.rank=1
        self.cal_total_avg()
        self.cal_grade()

    def cal_total_avg(self): #점수 총점, 평균 계산
        self.total=self.engs+self.clans+self.pys
        self.avg=round(self.total/3,2)

    def cal_grade(self): #학점 계산
        if(self.avg>=90):
            self.grade='A'
        elif(self.avg>=80):
            self.grade='B'
        elif(self.avg>=70):
            self.grade='C'
        elif(self.avg>=60):
            self.grade='D'
        else:
            self.grade='F'

    def __str__(self): #정보 리턴
        return(f"{self.stdnum}\t{self.stdname}\t{self.engs}\t{self.clans}\t{self.pys}\t{self.total}\t{self.avg}\t{self.grade}\t{self.rank}")

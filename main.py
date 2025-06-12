#메인 함수
#전체 실행 및 메뉴 처리
#main.py
#chatGPT의 도움을 약간 받았습니다.
from manage import Managing

def main():
    manager=Managing()

    while True:
        print("\n----------------------------------------")
        print("\n메뉴")
        print("1. 학생 입력")
        print("2. 전체 출력")
        print("3. 학생 추가")
        print("4. 학생 삭세")
        print("5. 학생 탐색")
        print("6. 총점 정렬")
        print("7. 80점 이상인 학생의 수")
        print("9. 종료")
        choice=int(input("선택: "))

        if choice==1:
            manager.input_student()
        elif choice==2:
            manager.__str__()
            print(manager)
        elif choice==3:
            student =manager.get_student_input()
            manager.add_student(student)
        elif choice==4:
            stdnum=input("삭제할 학번: ")
            manager.delete_student(stdnum)
        elif choice==5:
            searchnum=input("찾는 학번 입력: ")
            manager.search_student(searchnum)
        elif choice==6:
            manager.sort_by_total()
        elif choice==7:
            manager.count_avg_80()
        elif choice==9:
            print("종료합니다.")
            break
        else:
            print("없는 메뉴입니다.")


if __name__=="__main__":
    main()

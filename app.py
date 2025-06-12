from db import initialize_db
from models import insert_student, delete_student, search_student, count_over_80
from display import display_all, sort_by_total

def main():
    initialize_db()
    while True:
        print("\n=== 학생 성적 관리 시스템 ===")
        print("1. 학생 정보 입력")
        print("2. 학생 정보 삭제")
        print("3. 학생 정보 탐색")
        print("4. 전체 출력")
        print("5. 총점 기준 정렬")
        print("6. 80점 이상 학생 수")
        print("0. 종료")
        choice = input("선택: ")

        if choice == "1":
            insert_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_all()
        elif choice == "5":
            sort_by_total()
        elif choice == "6":
            count_over_80()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()
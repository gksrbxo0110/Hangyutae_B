import random

def generate_students():
    students = []
    for _ in range(30):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

def sort_students(students, field, algorithm, reverse):
    if algorithm == '선택 정렬':
        for i in range(len(students)):
            idx = i
            for j in range(i + 1, len(students)):
                if (students[j][field] < students[idx][field]) != reverse:
                    idx = j
            students[i], students[idx] = students[idx], students[i]
    elif algorithm == '삽입 정렬':
        for i in range(1, len(students)):
            key = students[i]
            j = i - 1
            while j >= 0 and (students[j][field] > key[field]) != reverse:
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key
    elif algorithm == '퀵 정렬':
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if (x[field] < pivot[field]) != reverse]
            middle = [x for x in arr if x[field] == pivot[field]]
            right = [x for x in arr if (x[field] > pivot[field]) != reverse]
            return quick_sort(left) + middle + quick_sort(right)
        students[:] = quick_sort(students)
    elif algorithm == '기수 정렬' and field == "성적":
        # 최대 값의 자리수를 계산
        max_score = max(student[field] for student in students)
        exp = 1

        # 기수 정렬 수행 (계수 정렬을 활용)
        while max_score // exp > 0:
            count = [0] * 10  # 계수 정렬에 사용할 버킷
            output = [None] * len(students)

            # 각 학생의 현재 자리수에 해당하는 값의 빈도를 계산
            for student in students:
                index = (student[field] // exp) % 10
                count[index] += 1

            # 계수 정렬을 위한 누적 합 계산
            for i in range(1, 10):
                count[i] += count[i - 1]

            # 출력 리스트에 정렬된 값을 삽입 (뒤에서부터 삽입하여 안정성 유지)
            for i in range(len(students) - 1, -1, -1):
                index = (students[i][field] // exp) % 10
                output[count[index] - 1] = students[i]
                count[index] -= 1

            # 정렬 결과를 원본 리스트에 복사
            students[:] = output

            # 다음 자리수로 이동
            exp *= 10

        # 내림차순을 선택한 경우 결과를 뒤집음
        if reverse:
            students.reverse()

        # 주석: 위의 구현은 기수 정렬 알고리즘에서 계수 정렬을 활용하여
        #       각 자리수를 안정적으로 정렬함으로써 효율성을 개선합니다.
        #       시간 복잡도는 O(nk)로, 여기서 n은 학생 수, k는 자리수입니다.

def display_students(students):
    print("생성된 학생 정보:")
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

def main():
    students = generate_students()
    display_students(students)
    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4): ")
        if choice == '4':
            print("프로그램을 종료합니다.")
            break
        field = {"1": "이름", "2": "나이", "3": "성적"}.get(choice)
        if not field:
            print("잘못된 입력입니다.")
            continue
        print("정렬 알고리즘:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만 가능)")
        algo_choice = input("정렬 알고리즘을 선택하세요 (1, 2, 3, 4): ")
        algorithm = {"1": "선택 정렬", "2": "삽입 정렬", "3": "퀵 정렬", "4": "기수 정렬"}.get(algo_choice)
        if not algorithm or (field != "성적" and algorithm == "기수 정렬"):
            print("잘못된 입력입니다.")
            continue
        reverse = input("오름차순(0) 또는 내림차순(1)을 선택하세요: ") == '1'
        sort_students(students, field, algorithm, reverse)
        display_students(students)

if __name__ == "__main__":
    main()

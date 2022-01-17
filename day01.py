# 사용자로부터 이름과 성적을 입력받아 총점과 평균을 구해
# 출력하는 프로그램을 작성하세요

# 현 input은 str
name = input("이름을 입력하세요: ")
korean = input("국어 점수를 입력하세요:")
english = input("영어 점수를 입력하세요: ")
math = input("수학 점수를 입력하세요: ")

# str -> int (총점과 평균값을 구해야함으로 변경해줌)
total = int(korean) + int(english) + int(math)
avg = total / 3

print(name, "님의 총점은", total, "점,", "평균은", avg, "입니다.")

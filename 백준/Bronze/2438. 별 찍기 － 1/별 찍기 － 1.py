# *별 찍기, problem_2438.py
# 접근방법: 입력을 숫자 값으로 받고, 출력을 입력한 숫자만큼 i번 반복해서 출력한다. ( 0< i < 입력 값+1 )

N = int(input()) 
# 입력값을 input() 으로 받고 int() 함수를 사용해 정수로 변환하여 N에 저장
for i in range(1, N+1):
    print('*' * i)
# 반복문을 통해 1 부터 N까지 반복
# for 루프에 range() 함수를 사용하여 반복 범위를 지정, range(start, stop) ; range 함수에서는 start 는 포함하고 stop은 포함하지 않는다.

# https://www.acmicpc.net/problem/2745
# 진법 변환

# 접근 방법
# - 파이썬의 기본 int 함수는 주어진 수를 특정 진법에서 10진법으로 변환할 수 있는 기능이 있음
# - 진법을 나타내는 B와 수 N을 입력받아 int 함수에 전달

# 입력받기
N, B = input().split()
B = int(B)

# B진법 수 N을 10진법으로 변환
decimal_value = int(N, B)

# 결과 출력
print(decimal_value)
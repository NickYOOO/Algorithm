# 알고리즘 수업 - 알고리즘의 수행 시간 4
# https://www.acmicpc.net/problem/24265

# 접근방법:
# - N을 입력받는다
# - 이중 for문의 수행 시간은 1부터 (N-1)까지의 합이므로 (N * (N - 1)) / 2
# - 정수로 출력하기 위해 // 연산자를 사용
# - 마지막으로 시간 복잡도가 O(N^2)임을 나타내기 위해 정수 2를 출력

# 백준 24265번 풀이
N = int(input())

# 수행 시간이 i에 대해서 1부터 N까지의 합
execution_time = N * (N - 1) // 2

# 수행 시간을 출력
print(execution_time)

# 시간 복잡도를 나타내는 정수 2를 출력
print(2)
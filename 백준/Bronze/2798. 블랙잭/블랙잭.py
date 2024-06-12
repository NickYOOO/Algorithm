# 2798번 - 블랙잭
# 1. 입력값 읽기
# 2. 세 카드의 모든 조합 생성
# 3. 조합 값이 조건에 맞는지 확인
# 4. M에 가까운 최대값 찾기

# 입력값 읽기, 처리
import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
M = int(data[1])
cards = list(map(int, data[2:]))

# 조건에 가까운 최대값을 저장할 변수
max_sum = 0

# 3중 루프, 브루트 포스(완전 탐색)으로 3장의 모든 조합의 합 계산
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]

            # 3장의 합이 M을 넘지 않으면 최대값 갱신
            if card_sum <= M:
                max_sum = max(max_sum, card_sum)

print(max_sum)
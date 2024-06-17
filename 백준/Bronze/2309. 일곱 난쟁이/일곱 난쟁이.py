# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이

#못 풀었음 

# 접근 방법
# 입력 처리: 9명의 난쟁이의 키를 입력
# 조합 생성: 9명 중 7명을 선택하는 모든 조합을 생성. (파이썬의 itertools 라이브러리를 이용하여 쉽게 조합을 생성)
# 합 체크: 생성된 조합 중 합이 100인 조합을 찾는다.
# 결과 출력: 합이 100인 조합을 오름차순으로 정렬하여 출력

import itertools

# 9명의 난쟁이 키를 입력 받는다.
heights = [int(input()) for _ in range(9)]

# 9명 중에서 7명을 뽑아 그 키의 합이 100이 되는 조합을 찾는다.
for combination in itertools.combinations(heights, 7):
    if sum(combination) == 100:
        result = sorted(combination)
        for height in result:
            print(height)
        break

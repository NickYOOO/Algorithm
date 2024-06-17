# https://www.acmicpc.net/problem/7567
# 그릇

# 접근 방법
# - 주어진 그릇의 모양을 순서대로 탐색하여 높이를 계산
# - 인접한 그릇의 모양이 같은지를 비교하여 높이를 더한다.
# - 최종 높이를 출력 형식에 맞게 반환.

plates = input()
height = 10

for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:
        height += 5
    else:
        height += 10

print(height)

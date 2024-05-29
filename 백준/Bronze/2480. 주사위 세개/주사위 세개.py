# 주사위 세개
# 접근방법: 입력값을 받고, 3가지 조건을 부여한다. (3개 일치, 2개일치, 일치하지 않을 때)


dice = list(map(int, input().split()))
# 입력 받기가 어려웠음.
dice.sort()
# 오름차순 정렬을 해주면서 값의 비교가 쉬워짐

if dice[0] == dice[1] == dice[2]:
    prize = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[1] == dice[2]:
        prize = 1000 + dice[1] * 100
else:
    prize = dice[2] * 100

print(prize)
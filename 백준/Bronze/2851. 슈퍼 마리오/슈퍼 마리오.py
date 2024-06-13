def nearest_to_100(scores):
    total_score = 0
    previous_score = 0  # 마지막에 더하기 전 점수를 저장할 변수
    for score in scores:
        previous_score = total_score  # 더하기 전의 상태를 저장
        total_score += score
        if total_score >= 100:
            break

    if total_score <= 100:
        return total_score
    else:
        if (total_score - 100) <= (100 - previous_score):
            return total_score
        else:
            return previous_score

# 입력과 관련된 부분(입력을 받아서 nearest_to_100 함수를 호출하는 부분)
mushroom_scores = [int(input()) for _ in range(10)]
print(nearest_to_100(mushroom_scores))
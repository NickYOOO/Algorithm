# https://www.acmicpc.net/problem/10798
# 세로읽기

# 접근방법:
# - 다섯 개의 문자열을 입력고
# - 각 문자열의 각 문자를 세로로 읽어가며 새로운 문자열을 생성
# - 모든 문자열의 각 인덱스에 해당하는 문자를 차례로 읽는다.

# 5개의 문자열을 입력받기
strings = [input().strip() for _ in range(5)]

# 최종 결과를 저장할 리스트 초기화
result = []

# 최대 문자열의 길이 구하기
max_len = max(len(s) for s in strings)

# 세로로 읽기
for i in range(max_len):
    for s in strings:
        if i < len(s):
            result.append(s[i])

# 결과 출력
print(''.join(result))


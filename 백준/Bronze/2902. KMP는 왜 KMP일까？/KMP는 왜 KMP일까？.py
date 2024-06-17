# KMP는 왜 KMP일까?
# https://www.acmicpc.net/problem/2902

# 접근방법:
# - 문자열이 하이픈("-")으로 구분된 단어들로 이루어져 있으므로 이를 기준으로 문자열을 분리
# - 분리된 각 단어의 첫 글자를 추출
# - 추출된 첫 글자들을 이어 붙여 결과 문자열을 만듬

# 입력받기
full_name = input().strip()

# 하이픈('-')을 기준으로 문자열 나누기
words = full_name.split('-')

# 각 단어의 첫 글자 추출
initials = ''.join(word[0] for word in words)

# 결과 출력
print(initials)


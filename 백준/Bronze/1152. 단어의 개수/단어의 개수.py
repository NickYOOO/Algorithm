# 단어의 개수
# 접근방법: 문자열을 공백 기준으로 나누고, 배열의 요소를 카운트 한다. 

string = input()

words = string.split()

word_count = len(words)
# len() 함수는 파이썬 내장 함수로, 객체(문자열, 리스트, 튜플 등)의 길이(또는 요소의 개수)를 반환한다.
print(word_count)
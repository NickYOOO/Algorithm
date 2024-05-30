# 단어의 개수
# 접근방법: 문자열을 공백 기준으로 나누고, 배열의 요소를 카운트 한다. 
import sys

def count_words(input_string):
    words = input_string.split()
    word_count = len(words)
    return word_count
# len() 함수는 파이썬 내장 함수로, 객체(문자열, 리스트, 튜플 등)의 길이(또는 요소의 개수)를 반환한다.
input_string = sys.stdin.read().strip()
print(count_words(input_string))
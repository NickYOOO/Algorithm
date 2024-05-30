def count_words(input_str):  
    return len(input_str.split()) # 단어의 개수를 반환  
  
# 사용자로부터 문자열 입력 받기  
input_str = input()  
  
# 단어의 갯수 출력  
print(count_words(input_str))
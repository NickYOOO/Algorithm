# 상수
# 문제분석: 각각의 숫자들을 reverse 하여 비교한다.

def reverse_compare_num(num1, num2):
    num1_reversed = num1[::-1]
    # [::-1]은 파이썬의 리스트나 문자열을 거꾸로 뒤집는다. 
    num2_reversed = num2[::-1]

    if int(num1_reversed) > int(num2_reversed):
        return num1_reversed
    else:
        return num2_reversed

num1, num2 = input().split()
print(reverse_compare_num(num1, num2))
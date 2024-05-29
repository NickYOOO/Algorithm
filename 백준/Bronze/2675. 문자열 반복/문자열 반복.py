# 문자열 반복
# (못풀었음)
# 해결 방법: 수 와 문자열을 받고,   

T = int(input()) 

for _ in range(T):
    #  언더스코어 _는 반복되는 요소에 대한 변수가 필요하지 않을 때 사용, 
    data = input().split()
    # R 과 S 분리하여 값을 받는다
    R = int(data[0])
    S = data[1]
    result = ""
    # 결과를 저장할 빈 문자열

    for char in S: 
        result += char * R

    print(result)
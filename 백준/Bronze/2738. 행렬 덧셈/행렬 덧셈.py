# 행렬 덧셈

# 해결 방법: 크기가 같은 두 행렬의 덧셈
# - 행과 열이 M,N 으로 주어짐
# - 각 행의 원소들이 주어지며 두 행렬을 더해준다.

# 행렬의 크기 N, M 입력 받기 , (입렵값 공백 기준 맵 함수 -> 각 요소 정수 적용)
n, m = map(int, input().split())

# 첫 번째 행렬 A 입력 받기 , (빈 리스트 선언 -> 반복 -> row; 한 행을 받아 리스트로 변환 -> append 한 행씩 추가) 
A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

# 두 번째 행렬 B 입력 받기 , ( 동일 )
B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

# 결과 행렬 C 초기화 및 계산 , ( 빈 리스트 생성 -> 행 수 n만큼 반복 -> 각 행을 저장할 row 리스트 선언 -> 행i , 열j 요소를 더하여 row에 추가 완성 된 행을 C리스트에 추가)
C = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# 결과 행렬 C 출력
for row in C:
    print(' '.join(map(str, row)))
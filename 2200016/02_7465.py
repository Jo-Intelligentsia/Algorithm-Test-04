# 7465 창용 마을 무리의 개수
# 창용 마을에는 N명의 사람이 살고 있다.
# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
# 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
# 이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
# 같은 관계는 반복해서 주어지지 않는다.
# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 무리의 개수를 출력한다.

import sys
sys.stdin = open("0210_swea/02_text.txt", "r")

T = int(input())
for i in range(1,T+1):
        
    N , M = map(int,input().split())
    ls = [] # 모든 사람 넣기
    total = 0 # 그룹생길때 마다 하나씩 늘리기
    for i in range(M):  # 아는 관계수 만큼 반복 입력받기 
        x , y = map(int,input().split()) # 아는 사람 번호 받기
        if len(ls) == 0:    # 첫 숫자 추가
            a = [x,y]
            ls.append(a)
        else:
            if x in ls[0]:           # 첫 숫자와 입력값 비교해서 넣기
                if y in ls[0]:
                    continue
                ls[0].append(y)
            elif y in ls[0]:
                if x in ls[0]:
                    continue
                ls[0].append(x)
            if x not in ls[0] and y not in ls[0]:
                a = [x,y]
                ls.append(a)
    for i in range(len(ls)): # 3번 반복 ( 0, 1 )
        for j in range(len(ls[i])): # 5
            for k in range(len(ls[i+1])): # 2
                if i >= len(ls):
                    continue
                if ls[i][j] == ls[i+1][k]:
                    ls[i].append(ls[i][j])
                    print(ls[i][j])
                    print(ls)

# 1 2
# 2 5   [[1, 2, 5, 4, 3], [3, 4], [4, 6]]
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3
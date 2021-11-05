# global m
# n,m = map(int, input().split()) # n : 길이 m : 던지기/굴리기 가능 횟수
# a = list(map(int, input().split()))
# a.insert(0, 0)
# # a.insert(len(a), 0)
# global i
# i = 0 #현재 위치
# global size 
# size= 1 #현재 크기

# # state = {'i': 0, 'size':1}
# # print(state)

# x = 0 
# cases = [x for x in range(n**2)] # case 0으로 초기화

# def roll():
#     global size, i
#     print(f"roll실행 : 현재위치: {i} 현재 사이즈: {size}")
#     if i+1 <= n:
#         size = size + a[i+1]
#         i = i + 1
#         print(f"after roll실행 : 현재위치: {i} 현재 사이즈: {size}\n")
#     else:
#         return

# def throw():
#     global size, i
#     print(f"throw 실행 : 현재위치: {i} 현재 사이즈: {size}")
#     if i+2 <= n:
#         size = (size//2) + a[i+2]
#         i = i + 2
#         print(f"after throw 실행: 현재위치: {i} 현재 사이즈: {size}\n")
#     else:
#         return

# temp = 0
# for k in range(len(cases)):
#     # if i > m: # 시간이 되기 전 위치만큼 갔을 때
#     #     print(size)
#     #     break
#     for j in range(n-temp):
#         if i <= m:
#             roll()
#     for l in range(temp):
#         if i <= m:
#             throw()
#     cases.append(size)
#     size = 0
#     temp = temp+1
#     m = m+1 #시간 제한
#     print('-'*20)

# print(max(a))


a = 3

def test():
    a = 2
    print(a)

test()
print(a)
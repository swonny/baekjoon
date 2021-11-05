a,b,c = map(int, input().split())

print( a//(c-b)+1 if c>b else -1)

# i = 1;

# while c*i < a+b*i:
#     # print(a+b*i)
#     # print(c*i)
#     # print(i)
#     try:
#         i += 1
#     except:
#         i = -1
#     # print(f"i : {i}")

# while b*i + a != c*i:
#     if b>c:
#         i = -1
#         break
#     i += 1



# print(i+1 if i>0 else i)
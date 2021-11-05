n = int(input())

start = 2
i = 1
cnt = 1

while n != 1:
    if start <= n <= start+6*i-1:
        break
    else:
        start = start + 6*i
        cnt += 1
        i += 1

print(cnt if n==1 else cnt+1)


# while True:
#     if n >= start and n <= start+6*i -1:
#         break
#     else:
#         start = start + 6*i
#         cnt += 1
#         i += 1


# if n == start:
#     print(cnt)
# else:


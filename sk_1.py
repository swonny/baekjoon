# s = input()
s = list(input())

a =list()

for i in s:
    a.append(list(map(int, str(ord(i)))))
    # a.append(ord(i))

for i in range(len(s)):
    print(s[i]*sum(a[i]))


# print(ord('a'))


# for i in s:
#     # a.append(list(map(int, str(ord(i)))))
#     a.append(ord(i))

# idx = 0
# for i in s:
#     print(i*sum(a[idx]))
#     idx = idx+1

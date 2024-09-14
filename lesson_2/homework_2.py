# Number 1
# A = list(map(int, input().split()))
# A_1 = A[1] + A[0] + A[3] + A[2] + A[4]
# print(A_1)

# Number 2
# B = list(map(int, input().split()))
# print(B.insert(0, B.pop()), [i for i in B])

# Numder 3
# C = list(map(int, input().split()))
# for i in C:
#     if C.count(i) == 1:
#         print(i)

# Number 4
# E = list(map(int, input().split()))
# maximum = E.count(E[0])
# for i in E:
#     if E.count(i) > maximum:
#         maximum = E.count(i)
# print(E[i])

# Number 5
# n, s = input().split()
# n = int(n)
# res = list()
# for i in range(0, len(s), n):
#     res += reversed(s[i:i+n])
# print(''.join(res))

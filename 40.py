'''

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
n = int(input('Enter range from 1 to '))

ans = '0.'

for i in range(1, n):
    ans += str(i)

# print(ans)

lisAns = [x for x in ans[1:]]
# print(lisAns)
# print(lisAns[12])

main = int(lisAns[1]) * int(lisAns[10]) * int(lisAns[100]) * int(lisAns[1000]) * int(lisAns[10000]) * int(lisAns[100000]) * int(lisAns[1000000])

print(main)

# liss = [x for x in range(1, 10)]
# ans = ''

# for j in range(1, 5):
#     for i in liss:
#         ans += str(i)
#     for k in range(0, 10):
#         ans += str(j) + str(k)
#     # ans+=str(i)

# print(ans)

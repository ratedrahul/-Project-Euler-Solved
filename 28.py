'''

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


dig = int(input('Enter Odd digonal size : '))
odd_list = [n for n in range(0, 1500) if n % 2 != 0]
dig_list = [x for x in range(1, dig * dig + 1)]
ans = 0
# print('dig list is ', dig_list)
factor_list = [o**2 for o in odd_list]
# print('factor list is ', factor_list)
new_fac = [x for x in odd_list if x <= dig_list[-1]]
new_fac.insert(0, 0)
# print('new_fac : ', new_fac)

new_dig_list = []

# for x in factor_list:
#     for t in range(x):
#         new_dig_list.append(t)
# print(new_dig_list)

i = 1
start = 2
for k in range(len(dig_list)):
    if dig_list[k] == 1:
        new_dig_list.append(1)

    if dig_list[k] == factor_list[i]:
        new_dig_list.extend(dig_list[start:factor_list[i] + 1:new_fac[i] + 1])
        # print('ye he new_dig_list ', new_dig_list)
        # print('new_fac[1] : ', new_fac[1])
        start = new_dig_list[-1] + new_fac[i + 1]
        i += 1
print(sum(new_dig_list))
# print("New dig list ", new_dig_list)
#         factor = new_fac[i]
# #         faq = 1

#     if dig_list[k] >= factor_list[i]:
#         i += 1

#         print(new_dig_list)
#         i = 1


# print('new_dig_list : ', new_dig_list)

#         factor = factor_list[i]
#         new_fac+=2

#         print('factor for ', dig_list[k], 'is ', factor)
#     if dig_list[k] >= factor_list[i]:
#         i += 1

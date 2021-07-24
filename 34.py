'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

# x = int(input('Enter a number '))

ans = []
for NUM in range(1, 404600):
    str_x = str(NUM)
    listt = []

    for i in str_x:
        j = int(i)
        fact = 1
        for L in range(1, j + 1):
            fact *= L
        # print('fact is ', fact)
        listt.append(fact)
    # print('num is ', NUM)
    # print('sum of list '	, 'is ', sum(listt))
    # print()
    # print(listt)
    # print('\n and sum of list is ', sum(listt))
    if sum(listt) == NUM:
        print('FOUND IT BC, num is ', NUM, 'Sum is ', sum(listt))
        ans.append(NUM)

print('Final list will be ', ans)

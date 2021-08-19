'''

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''


num = int(input('Enter num : '))
from timeit import timeit


# Count = True
ans = []
for x in range(1, num):
    # print('\n\nDoing for num', x)
    lis = []
    Count = True
    str_num = str(x)

    while Count:
        k = 0
        for i in str_num:
            k += int(i) * int(i)
        # print(k)

        # print('list he ', lis)
        lis.append(k)
        if 89 in lis:
            # print(x, ' 89 wali list')
            ans.append(x)
            # print()
            # print('Ans ki list', ans)

            Count = False

        # if len(lis) == 100:
        #     break
        if 1 in lis:
            # print(x, ' 1 wali list')
            break
        str_num = str(k)
print(len(ans))
print(timeit())

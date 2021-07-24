'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
# n = int(input('Enter a number '))


def even(n):
    n = n / 2
    return n


def odd(n):
    n = 3 * n + 1
    return n


# dicto = {}
val = []
IND = [1, 2, 3, 4]
for n in range(5, 1000000):
    count = 0
    IND.append(n)
    # print(n, '--> ', end=' ')
    for i in range(1000000):

        if n % 2 == 0:
            count += 1
            n = even(n)
            # print(n, '--> ', end='')
        if n == 1:
            break
        if n % 2 != 0:
            n = odd(n)
            count += 1
            # print(n, '--> ', end='')
        if n == 1:
            break
    # print('\n\n')
    val.append(count)
    # dicto{n: i}
    # dx = dict(n=i)

# print(dx)
# print(type(dx))

print('val is ', val)

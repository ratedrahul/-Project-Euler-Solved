'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
t = int(input('Enter a range to  find amicable number pair of it : '))

amic = []
for n in range(1, t + 1):

    def divisors(n):
        global div
        div = []
        for i in range(1, n):
            if n % i == 0:
                div.append(i)
        return sum(div)

    divisors(n)
    print('All divisors of number ', n, 'is : ', div)
    y = sum(div)

    print('Sum of all divisors of ', n, 'is :', y)

    x = divisors(y)
    if x == n and y != x:

        amic.append(x)
        print(x, 'is a amicable number ')
print('Amicable pair in the range :', amic)

'''

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

main = []
for n in range(99, 999999):

    if len(str(n)) == len(str(2 * n)) == len(str(3 * n)) == len(str(4 * n)) == len(str(5 * n)) == len(str(6 * n)):

        def func(ran):
            liss = []

            for a in str(n):
                if a in str(ran * n):
                    liss.append(1)
                else:
                    liss.append(0)
                # print(liss)
            global stat
            stat = all(liss)
        func(2)
        if stat == True:
            func(3)
            if stat == True:
                func(4)
                if stat == True:
                    func(5)
                    if stat == True:
                        func(6)
                        if stat == True:
                            main.append(n)
print(main)

# print(n, 'and ', ran * n)
# main.append(str(n))

# return str(n)

# for i in range(2,7):

# main.append(func(2))

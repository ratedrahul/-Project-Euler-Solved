'''

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

prime = [2, 3]
for i in range(1, 9999):
    for k in range(2, i):
        if i % k == 0:
            break
        if k == (i - 2):
            prime.append(i)

for n in range(1000, 9999):
    n1 = n + 3330
    n2 = n1 + 3330

    if (n1 in prime) and (n2 in prime) and (n in prime):
        if len(str(n)) and len(str(n1)) and len(str(n2)) == 4:

            temp = []
            # print('All three is in ', n, n1, n2)
            ns = str(n)
            ns1 = str(n1)
            ns2 = str(n2)
            n_list = [str(n) for n in ns]
            n1_list = [str(n) for n in ns1]
            n2_list = [str(n) for n in ns2]

            # # print(n_list, n1_list, n2_list)
            temp.extend(ns)
            count = 0
            for element in temp:
                if element in ns1:
                    if element in ns2:
                        count += 1
                        # continue
                    else:
                        break

            #     if element not in n1_list and element not in n2_list:
            #         # print('not permuted')
            #         break
            #     else:
            #         count += 1
            #     # print('count is ', count)
                # print(count)
                if count == 4:
                    print('it is permutedly perfect ', n, n1, n2)

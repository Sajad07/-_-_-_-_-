from numpy import power, e, sqrt, arccos
import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return (1.7 * power(t, 2))


def g(t):
    return (power(e, t) - 1)


listx = []
listyf = []
listyg = []


def Similariy(start, stop):
    step = stop/1000
    numerator = 0
    SumOfSquaresf = 0
    SumOfSquaresg = 0
    listx.extend(np.arange(start, stop, step))

    for index in listx:
        resultf = f(index)
        resultg = g(index)

        listyf.append(resultf)
        listyg.append(resultg)
        numerator += resultf*resultg
        SumOfSquaresf += power(resultf, 2)
        SumOfSquaresg += power(resultg, 2)

    denominator = sqrt(SumOfSquaresg)*sqrt(SumOfSquaresf)
    return arccos(numerator/denominator)


# print(Similariy(0, 1))
# plt.plot(listx, listyf, '-b', listx, listyg, '-r')
# plt.show()

print(Similariy(0, 10))
plt.plot(listx, listyf, '-b', listx, listyg, '-r')
plt.show()

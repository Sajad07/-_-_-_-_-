from numpy import arange, power, e, sqrt, arccos
import matplotlib.pyplot as plt


def f(t):
    return (1/sqrt(1+t**2))


def g(t, a):
    return (e**(-a*t**2))


def Similariy():
    numerator = 0
    SumOfSquaresf = 0
    SumOfSquaresg = 0
    for a in arange(0, 0.2, 0.001):

        for t in arange(0, 5, 0.001):
            resultf = f(t)
            resultg = g(t, a)

            numerator += resultf*resultg
            SumOfSquaresf += power(resultf, 2)
            SumOfSquaresg += power(resultg, 2)

        denominator = sqrt(SumOfSquaresg)*sqrt(SumOfSquaresf)
        yield arccos(numerator/denominator)


listy = []
for i in Similariy():
    print(i)
    listy.append(i)


plt.plot(arange(0, 0.2, 0.001), listy)
plt.show()

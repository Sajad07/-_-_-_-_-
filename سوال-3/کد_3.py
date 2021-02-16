import soundfile as SF
from matplotlib.pyplot import *
from numpy import arange, arccos, sqrt

violinData, violinFrequency = SF.read(r'.\Sound\violin.wav')
violaData, violaFrequency = SF.read(r'.\Sound\viola.wav')
pianoData, pianoFrequency = SF.read(r'.\Sound\piano.wav')
hornData, hornFrequency = SF.read(r'.\Sound\horn.wav')


violinVector = violinData[:, 1]
violaVector = violaData[:, 1]
pianoVector = pianoData[:, 1]
hornVector = hornData[:, 1]

# =============================================الف=========================================
print("=============================================فلا=========================================")


violinLenght = len(violinVector)
violaLenght = len(violaVector)
pianoLenght = len(pianoVector)
hornLenght = len(hornVector)

print(f"violin's lenght : {violinLenght}", f"viola's lenght : {violaLenght}",
      f"piano's lenght : {pianoLenght}", f"horn's lenght : {hornLenght}", sep='\n', end='\n')

print(f"violin's Frequency : {violinFrequency}", f"viola's Frequency : {violaFrequency}",
      f"piano's Frequency : {pianoFrequency}", f"horn's Frequency : {hornFrequency}", sep='\n', end='\n')

print(f"violin's Periodicity : {1/violinFrequency}", f"viola's Periodicity : {1/violaFrequency}",
      f"piano's Periodicity : {1/pianoFrequency}", f"horn's Periodicity : {1/hornFrequency}", sep='\n', end='\n')

# =============================================ب=========================================


waves = {'violin': violinVector, 'viola': violaVector,
         'piano': pianoVector, 'horn': hornVector}
frequencys = {'violin': violinFrequency, 'viola': violaFrequency,
              'piano': pianoFrequency, 'horn': hornFrequency}


def x(Vector, Frequency):
    listx = list(arange(0, 2, 1/Frequency))
    for i in range(len(listx)-len(Vector)):
        listx.pop()
    return listx


for name, vector in waves.items():
    plot(x(vector, frequencys[name]), vector)
    title(name)
    show()
# =============================================ج=========================================

print("=============================================ج=========================================")


def Similariy(vector, frequency):
    numerator = 0
    SumOfSquaresf = 0
    SumOfSquaresg = 0
    listx = x(vector, frequency)

    for i in range(len(listx)):
        resultf = vector[i]
        resultg = violinVector[i]

        numerator += resultf*resultg
        SumOfSquaresf += resultf**2
        SumOfSquaresg += resultg**2

    denominator = sqrt(SumOfSquaresg)*sqrt(SumOfSquaresf)
    return arccos(numerator/denominator)


for name, vector in waves.items():
    if name == 'violin':
        continue
    print(
        f"Angular similarity between violin and {name} : {Similariy(vector,frequencys[name])}")

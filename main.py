n = int(input())
sumFact = 0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sumFact += fact

print(sumFact)
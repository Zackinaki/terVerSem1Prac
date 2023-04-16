from math import factorial

# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 
# приобретенных билета окажутся выигрышными?

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))

n=combination(100,2)
m=combination(2,2)
p=(m/n)*100

print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {p :.2f}%')
from math import factorial

# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 
# детали. Какова вероятность того, что все извлеченные детали окрашены?

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))

n=combination(15,3)
m=combination(9,3)
p=(m/n)*100

print(f'Вероятность того, что все извлеченные детали окрашены = {p :.2f}%')
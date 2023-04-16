# ; Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все 
# ; карты – крести. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial

def combination(n,k):
    return(factorial(n)/(factorial(k)*(factorial(n-k))))


n=combination(52,4)
m=combination(13,4)

p=(m/n)*100
print(f'а)Вероятность того, что все карты - крести = {p :.2f}%')


P1 = combination(4,1) * combination(48,3) / n
P2 = combination(4,2) * combination(48,2) / n
P3 = combination(4,3) * combination(48,1) / n
P4 = combination(4,4)*combination(48,0) / n
P = (P1 + P2 + P3+P4)*100
# print(P4)
# почему p4=3.69, а при сладывание вер-тей p =0,28
print(f'б)Вероятность того, что из 4 вытащенных из колоды хотя бы один туз = {P :.2f}%')



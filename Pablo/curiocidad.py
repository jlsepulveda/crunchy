#juego de cartar
def blackss(a,b,c):
    if sum([a,b,c])<= 21:
        return sum([a,b,c])
    elif 11 in[a,b,c] and sum([a,b,c]) <=31:
        return sum([a,b,c])-10
    else:
        return 'BUST'
black_1 =(5,6,7)
f = blackss(5,6,7)
print(f)
f = blackss(9,9,9)
print(f)
f = blackss(9,9,11)
print(f)

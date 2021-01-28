#juego de cartar
'''
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
print(f)'''

# crea una lista y mirar si tiene 007 eb orden es True y si no  False
'''
def juego_de_espia(num):
    #print(len(num))
    contador = 0
    for i in range(len(num)):
        #print(i)
        if (num[i] == 0):
            #print(num)
            contador +=1
        elif (contador ==2)and(num[i]==7):
            return True
    else:
        return False
        
spy_game =([0,2,4,0,0,7,5])
print(juego_de_espia(spy_game))
spy_game =([1,0,2,4,0,5,7])
print(juego_de_espia(spy_game))
spy_game =([1,0,2,0,7,5,1])
print(juego_de_espia(spy_game))'''

#Otra forma de realizarlo de la forma del curso 
def juego_de_espia(nums):
    
    code = [0,0,7,'x']
    #[0,7,'x']
    #[7,'x']
    #['x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

spy_game =([0,0,4,0,0,7,5])
print(juego_de_espia(spy_game))
spy_game =([1,6,2,4,0,5,7])
print(juego_de_espia(spy_game))
spy_game =([1,0,2,0,7,5,1])
print(juego_de_espia(spy_game))































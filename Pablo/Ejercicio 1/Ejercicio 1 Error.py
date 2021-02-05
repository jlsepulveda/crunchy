#como eliminar es pacios en blanco '.replace()'
#



#Por que muestra false si es lo mismo

def espacio(s):
    # asi se elimina espacio
    s = s.replace(' ','')
    #ahora imprimir al revez
    return s == s[::-1]
print(espacio('Hola mu ndo'))

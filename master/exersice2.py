texto = "Hellowold" = ['H','e','l','l','o','w','o','r','l','d']
contador = 1
texto_configurado = []

print("Forma o solucion #1")
for chart in texto:
	if(contador%2==0):
 		texto_configurado.append(chart.upper())
	else:
		texto_configurado.append(chart.lower())
	contador=contador+1

print(str(texto_configurado))

texto_configurado_2 = []
print("Forma o solucion # 2")
for i in range(1,len(texto)):
	if(i%2==0):
 		texto_configurado_2.append(texto[i-1].upper())
	else:
		texto_configurado_2.append(texto[i-1].lower())

print(str(texto_configurado_2))

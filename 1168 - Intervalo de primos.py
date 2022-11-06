
inicio = int(input('ano inicio:')) 
final = int(input('ano final:'))
qtd = 0

for n in range(inicio, final + 1):
    cont = 0
    for i in range (1, n+1):
        if n % i == 0:
            cont+= 1
    if cont == 2:
        print (n)
        qtd += 1

print ('primos:', qtd)

         
    
        

        
      
        



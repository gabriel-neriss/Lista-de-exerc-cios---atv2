
ano_inicio = int(input('ano inicio:'))
ano_final = int(input('ano final:'))
cont = 0

for c in range(ano_inicio, ano_final + 1):

    if c % 4 == 0 and c % 100 != 0 or c % 400 == 0:
        print (c)
        cont += 1
    
print ('bissextos:', cont)

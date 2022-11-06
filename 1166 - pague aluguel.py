valor_total_da_divida = int(input('valor total?'))
pagar_mensalmente = int(input('valor mensalmente?'))


meses = 0

while meses < 14:

    antes = valor_total_da_divida
    depois = valor_total_da_divida -  pagar_mensalmente
        
    if meses == 0:
       antes
       depois
       
    else:
        antes = valor_total_da_divida - pagar_mensalmente * meses
        depois = antes - pagar_mensalmente

    if antes <= 0 and depois <= 0:
        break
    elif depois < 0:
        depois = 0
   
    meses += 1
    
  

    print ('pagamento:', meses)
    print ('antes:', antes)
    print ('depois:', depois )
    print ('-----')

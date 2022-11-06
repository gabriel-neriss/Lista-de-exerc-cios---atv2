doação_total = reais = doação = 0
doação = float(input('d'))

while doação != -1:
    doação_total += doação
    reais = doação_total * 2.50
    doação = float(input('d'))
    
print ('VC$', '{:.2f}'.format(doação_total) )
print ('R$', '{:.2f}'.format(reais) )

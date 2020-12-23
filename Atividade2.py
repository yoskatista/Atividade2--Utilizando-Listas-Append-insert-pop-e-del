#Criar uma lista com 3 pessoas  PG81
lista = ['Sherek','Xandão','Saltitão']
print('A lista de convidados é {}'.format(lista))


#Substituindo Str da lista
lista[1] = 'Leo Estronda'
print('\n Xandão não poderá comparecer ao encontro de monstros, nós o substituimos!\n a nova lista é: {}'.format(lista))

#Mandando saudação para cada um!
print('\nSeja bem vindo {}, {} e {}'.format(lista[0],lista[1],lista[2]))

#Acrescentando mais 3 convidados com insert e append
lista.insert(3, 'Hulk')
lista.append('BamBam')
lista.insert(0, 'Xandão')
print('\nAcrescentamos mais convidados.\nA nova lista é: {} '.format(lista))

#Acrescentando no inicio, no meio e no final da lista com insert e append
lista.insert(0, 'Terry Crews')
lista.insert(4, 'Kratos')
lista.append('Saitama')
print('\nA Lista agora é:{}'.format(lista))

#Removendo 2 convidados com pop
excluidos = lista.pop(), lista.pop(), lista.pop(), lista.pop(), lista.pop(), lista.pop(), lista.pop()
print('\nAs pessoas que foram removidas da lista são: {}'.format(excluidos))
print('A lista agora é {}'.format(lista))

#Removendo os 2 unicos da lista com del
del lista[0]
del lista[0]
print('\nA lista foi removida. {}'.format(lista))
#
str_ip = '192.168.10.200/26'
cp = []; ip = []
#
cp = str_ip.split('/')
ip = cp[0].split('.')
#
rede_b = []; cast_b = []
#
for i in range(8 - (32 - int(cp[1]))):
  rede_b.append(1); cast_b.append(1)
for i in range(32 - int(cp[1])):
  rede_b.append(0); cast_b.append(1)
#
rede_b.reverse(); base_dois = 1
rede = 0; cast = 0
#
for i in range(8):
  if rede_b[i] == 1:
    rede = rede + base_dois 
  if cast_b[i] == 1:
    cast = cast + base_dois
  base_dois = base_dois * 2
#
host = cast - rede - 1
temp = rede
#
rede = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(rede)
cast = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(cast)
#
tabela = []; estado = []
m = host
#
for i in range(m):
  tabela.insert(i, ' '); estado.insert(i, 'L')
#
for i in range(m):
  x = temp + i + 1
  h = x % m
  while h > -1:
#
    if estado[h] == 'O':
      h = (h + 1) % m
#
    else:
      del tabela[h]; tabela.insert(h, x)
      del estado[h]; estado.insert(h, 'O')
      h = -1
#
op = '§'
while op != '0':
  op = input(''' _________________________ 
|                         |
| 1 - Buscar Usando Ip.   |\n| 2 - Buscar Usando Maq.  |
| 3 - Listar Tabela Hash. |\n| 0 - Sair.               |
|_________________________|\n\n
-------------V-------------
             ''')
  print('-------------Λ-------------\n')
#
  if op == '1':
    while op != '§':
      busca = input('''--------< BUSCAR: >--------
      ''')
      print('---------------------------')
      #
      for i in range(m):
        if busca == ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(tabela[i]):
          indice = tabela.index(tabela[i]); op = '§'
          #
          if indice < 10:
            indice = '00' + str(i)
          elif indice < 100:
            indice = '0' + str(i)
          else:
            indice = str(i)
          #
          print('\n   ---------------------')
          print('   MAQ | ENDEREÇOS/HOSTS')
          print('   ---------------------')
          print('  ', indice, '|', ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(tabela[i]))
          print('   ---------------------')
      if op == '1':
        print('''
 _________________________
|                         |
|     A BUSCA FALHOU!     |
|_________________________|\n\n''')
    enter = input('             ')
#
  elif op == '2':
    while op != '§':
      busca = int(input('''--------< BUSCAR: >--------
            '''))
      print('---------------------------')
      if busca < host and busca > -1:
        op = '§'
        #
        if busca < 10:
          indice = '00' + str(busca)
        elif busca < 100:
          indice = '0' + str(busca)
        else:
          indice = str(busca)
        #
        print('\n   ---------------------')
        print('   MAQ | ENDEREÇOS/HOSTS')
        print('   ---------------------')
        print('  ', indice, '|', ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(tabela[busca]))
        print('   ---------------------')
      if op == '2':
        print('''
 _________________________
|                         |
|     A BUSCA FALHOU!     |
|_________________________|\n\n''')
    enter = input('             ')


#
  elif op == '3':
    print('   -----< TABELA: >-----')
    print('   REDE: ' + str(rede))
    print('   CAST: ' + str(cast))
    print('   ---------------------')
    print('   MAQ | ENDEREÇOS/HOSTS')
    print('   ---------------------')
    for i in range(m):
      #
      if i < 10:
        maq = '00' + str(i)
      elif i < 100:
        maq = '0' + str(i)
      else:
        maq = str(i)
      #
      print('  ', maq, '|', ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(tabela[i]))
    print('   ---------------------')
    enter = input('             ')
#
  else:
    print(''' _________________________
|                         |
|   EXECUÇÃO ENCERRADA!   |
|_________________________|\n\n''')




#
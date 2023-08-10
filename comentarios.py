'''def motoqueiro():
    dados_motoqueiro1 = ( 1 ,'Pedro', '81988229997') 
    cursor.execute("INSERT INTO motoqueiro (id, nome, telefone) VALUES (?, ?, ?)", dados_motoqueiro1)

    dados_motoqueiro2 = ( 2 ,'João', '81988229998') 
    cursor.execute("INSERT INTO motoqueiro (id, nome, telefone) VALUES (?, ?, ?)", dados_motoqueiro2)

    dados_motoqueiro3 = ( 3 ,'Paulo', '81988229999') 
    cursor.execute("INSERT INTO motoqueiro (id, nome, telefone) VALUES (?, ?, ?)", dados_motoqueiro3)
    
    conexao.commit()        

motoqueiro()'''
    
''''def restaurante():
    dados_restaurante = ( 1 ,'JAPA SENAC', '8132521395', 'Rua do Apolo, 235')
    cursor.execute("INSERT INTO restaurante (id, nome, telefone, endereço) VALUES (?, ?, ?, ?)", dados_restaurante)

    conexao.commit()

restaurante()''''''














'''
'''''''''''
def pedido():
    query1 = cursor.execute(f"select * from clientes")
    for i in query1:
            print(i)
            selecao_cliente_nome = input('digite o nome do cliente: ')
            selecao_cliente = cursor.execute(f"select id from clientes WHERE nome = '{selecao_cliente_nome}'")
            print(selecao_cliente)

    conexao.commit()

  ''''''
def pagamento():
    query2 = cursor.execute(f"select * from pedidos")
    for i in query2:
        print(i)    
        selecao_pedido_nome = input('digite o pedido: ')
        selecao_pedido = cursor.execute(f"select id from pedidos WHERE nome = '{selecao_pedido_nome}'")
        print(selecao_pedido)

    conexao.commit() 

    #dados_pagamento = ( 1 ,'100', '18/10/2023', 'Samuel', '81988229997', 'JAPA SENAC')
    #cursor.execute('INSERT INTO pagamento (id, valor, data_hora, id_clientes, id_motoqueiro, id_pedidos) VALUES (?, ?, ?, (SELECT id FROM clientes WHERE id = ?), (SELECT id FROM motoqueiro WHERE telefone = ?), (SELECT id FROM pedidos WHERE id_restaurante = ?))', dados_pagamento)

  
def inserir1():  
    dados_clientes = ( 1 ,'Samuel', 'Dom manoel da costa 125', '81999229997')
    cursor.execute("INSERT INTO clientes (id, nome, endereço, telefone) VALUES (?, ?, ?, ?)", dados_clientes)  

    conexao.commit()
    ''''''

'''''''''
query1 = f"select * from clientes"
    for i in query1:
        print(i)
    selecao_cliente_nome = input('digite o cliente: ')
    selecao_cliente = f"select id from clientes WHERE nome = '{selecao_cliente_nome}'"

'''''''''''''
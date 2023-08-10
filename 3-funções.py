import sqlite3
#import motoqueiros from *
import datetime

conexao = sqlite3.connect('ifood.db')
cursor = conexao.cursor()

def cadastro_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereço = input("Endereço: ")
    print("Cadastro criado com sucesso!")
    #Conecta ao banco de dados
    conn = sqlite3.connect('ifood.db')
    cursor = conn.cursor()

    # Inserir o novo registro na tabela 'contas'
    cursor.execute(f"INSERT INTO clientes (nome, endereço, telefone) VALUES ('{nome}', '{endereço}', '{telefone}')")
   
    conn.commit()
cadastro_cliente()



def cadastro_pedido():
    pedidos = input("Digite o seu pedido: ")
    data_hora_pedido = datetime.datetime.now()
    
    print("Pedido realizado com sucesso!")
    
    conn = sqlite3.connect('ifood.db')
    cursor = conn.cursor()

    # Quando isso for para o Django, vamos criar um modelo tipo choices.
    # cliente = Cliente.objects.all()
    #usuario = resquest.user

    #usuario = input('digite o nome: ')
    #cursor = conn.execute (f"SELECT id from clientes WHERE nome ='{usuario}' ")

    #motorista = input('digite o nome: ')
    #cursor = conn.execute (f"SELECT id from motoqueiros WHERE nome ='{motorista}' ")
    #cursor.execute(f"INSERT INTO pedidos (nome_pedido, data_hora) VALUES ('{pedidos}', '{data_hora_pedido}', '{usuario}', '{motorista}')")
    cursor.execute(f"INSERT INTO pedidos (nome_pedido, data_hora) VALUES ('{pedidos}', '{data_hora_pedido}')")

    conn.commit()
cadastro_pedido()

def pagamento ():
    valor = input ('Digite o valor do pedido:') 
    data_hora_pedido = datetime.datetime.now()
    conn = sqlite3.connect('ifood.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO pagamento (valor, data_hora) VALUES ('{valor}', '{data_hora_pedido}')")

    print("Pedido realizado com sucesso!")

    conn.commit()
pagamento()



cursor.close()


'''dados_clientes = ('Will', '123', 'torre') 
    cursor.execute("INSERT INTO clientes (nome, telefone, endereço) VALUES (?, ?, ?)", dados_clientes)

    dados_motoqueiros = ('Paulo', '81988229999') 
    cursor.execute("INSERT INTO motoqueiro (nome, telefone) VALUES (?, ?)", dados_motoqueiros)
#nome = input()
#nome = 'chico'
#nome = request.user
#nome = 1+2*100*24654/2135431

#context = (nome, cpf)
#(insert into clientes (name, cpf) values(?,?), context)'''
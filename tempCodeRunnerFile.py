def pagamento ():
    valor = input ('Digite o valor do pedido:') 
    data_hora_pedido = datetime.datetime.now()
    conn = sqlite3.connect('ifood.db')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO pagamento (valor, data_hora) VALUES ('{valor}', '{data_hora_pedido}')")

    print("Pedido realizado com sucesso!")

    conn.commit()
pagamento()
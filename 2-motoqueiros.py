import sqlite3
import datetime

conexao = sqlite3.connect('ifood.db')
cursor = conexao.cursor()

def motoqueiros():
    dados_motoqueiro1 = ('Pedro', '81988229997') 
    cursor.execute("INSERT INTO motoqueiro (nome, telefone) VALUES (?, ?)", dados_motoqueiro1)

    dados_motoqueiro2 = ('João', '81988229998') 
    cursor.execute("INSERT INTO motoqueiro (nome, telefone) VALUES (?, ?)", dados_motoqueiro2)

    dados_motoqueiro3 = ('Paulo', '81988229999') 
    cursor.execute("INSERT INTO motoqueiro (nome, telefone) VALUES (?, ?)", dados_motoqueiro3)
    
    conexao.commit()        

motoqueiros()
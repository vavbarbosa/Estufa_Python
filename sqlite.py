import sqlite3
import pandas as pd

#Valores de Dia/Hora solicitados
dia_begin = '2022-02-27'
dia_end = '2022-02-27'
hora_begin = '20:00:00'
hora_end = '20:37:00'

#Simulação de valores para o banco
temp1=100
temp2=105
temp3=98
temp4=106
temp5=103
temp6=106
temp7=101
temp8=99

#Conectando com o banco
banco = sqlite3.connect('Estufa.db')

#Gerando cursor do banco
cursor = banco.cursor()

#Criando tabela TEMP
#cursor.execute('CREATE TABLE TEMP (diahora datetime, temp1 real, temp2 real, temp3 real, temp4 real, temp5 real, temp6 real, temp7 real, temp8 real)')

#Inserindo valores na tabela TEMP
#cursor.execute("""INSERT INTO TEMP (diahora, temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8) VALUES(datetime('now'),?,?,?,?,?,?,?,?)"""
#              ,(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8))

#Salvando no dataframe os valores  filtrados
df = pd.read_sql_query("SELECT * FROM TEMP WHERE diahora BETWEEN '"+dia_begin+" "+hora_begin+"' AND '"+dia_end+" "+hora_end+"'", banco)


#df = pd.read_sql_query("SELECT * FROM TEMP WHERE diahora BETWEEN '2022-02-27 20:00:00' AND '2022-02-27 20:37:00'", banco)
print(df.head())
    

banco.close()

import PySimpleGUI as sg
import sqlite3
import pandas as pd

#Tela de Solicitação de dados
class TelaPy:
    def __init__(self):
#Definição do modelo de layout        
        layout = [
            [sg.Text('Data Inicio',size=(16,0)),sg.Input(size=(15,0),key='dia_inicio')],
            [sg.Text('Hora Inicio',size=(16,0)),sg.Input(size=(15,0),key='hora_inicio')],
            [sg.Text('Data Fim',size=(16,0)),sg.Input(size=(15,0),key='dia_fim')],
            [sg.Text('Hora Fim',size=(16,0)),sg.Input(size=(15,0),key='hora_fim')],
            [sg.Button('Gerar Planilha')]
        ]
#Definição da Janela de Aprensetação
        janela = sg.Window("Dados Estufa",font=12).layout(layout)
        self.button, self.values = janela.Read()

#Alocação dos valores digitados na variáveis
    def Iniciar(self):
        
        global dia_begin
        global hora_begin
        global dia_end
        global hora_end
        dia_begin = self.values['dia_inicio']
        hora_begin = self.values['hora_inicio']
        dia_end = self.values['dia_fim']
        hora_end = self.values['hora_fim']
        
#Exibição da tela
tela = TelaPy()
tela.Iniciar()

#Conectando com o banco
banco = sqlite3.connect('Estufa.db')

#Gerando cursor do banco
cursor = banco.cursor()

#Salvando no dataframe os valores  filtrados
df = pd.read_sql_query("SELECT * FROM TEMP WHERE diahora BETWEEN '"+dia_begin+" "+hora_begin+"' AND '"+dia_end+" "+hora_end+"'", banco)


#df = pd.read_sql_query("SELECT * FROM TEMP WHERE diahora BETWEEN '2022-02-27 20:00:00' AND '2022-02-27 20:37:00'", banco)
print(df.head())
    
banco.close()

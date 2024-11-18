import PySimpleGUI as sg
import pandas as pd
import sqlite3
sg.theme('DarkBlue')

#Conectar/Criar DB, Criar cursor e criar tabela se não existit
banco = sqlite3.connect('Estufa.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS TEMP (diahora datetime, temp1 real, temp2 real,
temp3 real, temp4 real, temp5 real, temp6 real, temp7 real, temp8 real)''')
flayout = [
    [sg.Text('Data Inicio',size=(16,0)),sg.Input(size=(15,0),key='dia_inicio')],
    [sg.Text('Hora Inicio',size=(16,0)),sg.Input(size=(15,0),key='hora_inicio')],
    [sg.Text('Data Fim',size=(16,0)),sg.Input(size=(15,0),key='dia_fim')],
    [sg.Text('Hora Fim',size=(16,0)),sg.Input(size=(15,0),key='hora_fim')],
    [sg.Listbox('',key='resposta',size=(70,10))],
    [sg.Button('Gerar Planilha'), sg.Button('Sair')]
]

window = sg.Window('Dados Estufa',flayout,element_justification='center')

while True:
    button,values = window.read()
    #Salvando no dataframe os valores  filtrados
    if button == 'Sair':
        window.close()
        quit()
        break
    if button == 'Gerar Planilha':
        dia_begin = values['dia_inicio']
        hora_begin = values['hora_inicio']
        dia_end = values['dia_fim']
        hora_end = values['hora_fim']
        print(dia_begin + ' até ' + dia_end + ' entre ' + hora_begin + ' e ' + hora_end)
        df = pd.read_sql_query("SELECT * FROM TEMP WHERE diahora BETWEEN '"+dia_begin+" "+hora_begin+"' AND '"+dia_end+" "+hora_end+"'", banco)
        print(df)
        window.find_element('resposta').Update(df)
    if button == sg.WIN_CLOSED:
        quit()
        break
    

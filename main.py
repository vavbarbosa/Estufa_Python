import PySimpleGUI as sg

class TelaPy:
    def __init__(self):
        layout = [
            [sg.Text('Data Inicio',size=(16,0)),sg.Input(size=(15,0),key='dia_inicio')],
            [sg.Text('Hora Inicio',size=(16,0)),sg.Input(size=(15,0),key='hora_inicio')],
            [sg.Text('Data Fim',size=(16,0)),sg.Input(size=(15,0),key='dia_fim')],
            [sg.Text('Hora Fim',size=(16,0)),sg.Input(size=(15,0),key='hora_fim')],
            [sg.Button('Gerar Planilha')]
        ]
        janela = sg.Window("Dados Estufa",font=12).layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        Dia_inicio = self.values['dia_inicio']
        Hora_inicio = self.values['hora_inicio']
        Dia_fim = self.values['dia_fim']
        Hora_fim = self.values['hora_fim']
        print('A coleta será feita do dia '+Dia_inicio+' até o dia '+Dia_fim)
        print(f'Das '+Hora_inicio+' até '+Hora_fim)
tela = TelaPy()
tela.Iniciar()

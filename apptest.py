import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='password')],
    [sg.Button('Loguin')],
    [sg.Text('',key='mensagem')]
]

window = sg.Window('loguin interface',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'loguin':
      pasword_correto = 'abcd1'
      usuario_correto = 'iago'
      usuario =  values['usuario']
      password = values['password'] 
      if password == pasword_correto and usuario == usuario_correto:
         window['mensagem'].update('loguin efetuado com sucesso')
      else: 
        window['mensagem'].update('loguin incorreto')
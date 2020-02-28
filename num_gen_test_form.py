# import PySimpleGUIWeb as sg
import PySimpleGUI as sg
# Very basic window.  Return values as a list      
sg.change_look_and_feel('Dark')

layout = [
            # [sg.Text("VDP"), sg.Checkbox('nummers', default=True), sg.Checkbox('beelden')],



            [sg.Text('Nummer generator 2.0', text_color="Yellow")],
            [sg.Text('Ordernummer', size=(15, 1)), sg.InputText(key="order_number")],


            [sg.Text()],
            [sg.CalendarButton("Datum")],
            [sg.Text()],

            [sg.Text('Totaal aantal', size=(15, 1)), sg.Input(key="totaal_aantal")],
            [sg.Text('Beginnummer', size=(15, 1)), sg.InputText(key="begin_nummer")],
            [sg.Text('posities', size=(15, 1)), sg.InputText(key="posities")],
            [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],

            [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(key="Y_waarde")],
            [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],
            [sg.Text('prefix', size=(15, 1)), sg.InputText(key="prefix")],
            [sg.Text('postfix', size=(15, 1)), sg.InputText(key="postfix")],




            [sg.Button("Ok"), sg.Cancel()],

        [sg.Text('_' * 80)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
            ]      

window = sg.Window('Nummer Generator test form').Layout(layout)
button, values = window.Read() 

print(button, values["order_number"], values["begin_nummer"], values["posities"])

print(type(int(values["order_number"])))
# aantallen = int(values[0])
# print(aantallen)



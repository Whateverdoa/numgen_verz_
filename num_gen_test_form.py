# import PySimpleGUIWeb as sg
import PySimpleGUI as sg
import sys
import mes_wikkel as mes_wik
from paden import *


# Very basic window.  Return values as a list

def main():
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
        [sg.Text('voorloop getal', size=(15, 1)), sg.InputText(key="vlg0")],
        [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],

        [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(key="Y_waarde")],
        [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],
        [sg.Text('prefix', size=(15, 1)), sg.InputText(key="prefix")],
        [sg.Text('postfix', size=(15, 1)), sg.InputText(key="postfix")],
        [sg.Text('hoogte etiket', size=(15, 1)), sg.InputText(key="hoogte")],

        [sg.Button("Ok"), sg.Cancel()],

        [sg.Text('_' * 80)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        # [sg.Text('Your Folder', size=(15, 1), justification='right'),
        #  sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('Nummer Generator test form').Layout(layout)

    while True:
        event, values = window.Read()

        if event in ("Exit", None):
            break

        elif event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            # False in mac OS otherwise it will crash
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            # False in mac OS otherwise it will crash
            window.LoadFromDisk(filename)
            # load(form)

        elif event == "Ok":

            print("ok")

            # print(button, values["order_number"], values["begin_nummer"], values["posities"])

            ordernummer = values["order_number"]
            totaal_aantal = int(values["totaal_aantal"])
            begin_nummer = int(values["begin_nummer"])
            posities = int(values["posities"])
            vlg = int(values["vlg0"])
            aantal_per_rol = int(values["aantal_per_rol"])
            Y_waarde = int(values["Y_waarde"])
            wikkel = int(values["wikkel"])
            hoogte = int(values["hoogte"])
            prefix = values["prefix"]
            postfix = values["postfix"]

            print(type(int(values["order_number"])))
            # aantallen = int(values[0])
            # print(aantallen)
            # mes_wik.df_csv_rol_builder_met_rolnummer()
            beginlijst = mes_wik.rol_num_dikt(begin_nummer, vlg, totaal_aantal, aantal_per_rol)
            print(beginlijst)





            # # mes_wik.df_csv_rol_builder_met_rolnummer(beginlijst_begin, posities,
            #                                          vlg,
            #                                          aantal_per_rol,
            #                                          wikkel,
            #                                          prefix,
            #                                          postfix,
            #                                          beginlijst_rolnummer)


    window.close()


if __name__ == '__main__':
    main()

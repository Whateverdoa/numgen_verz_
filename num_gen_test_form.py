# import PySimpleGUIWeb as sg
import PySimpleGUI as sg
import os
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
                [sg.Text('Mes', size=(15, 1)), sg.InputText(key='mes')],

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
            prefix =values["prefix"]
            postfix = values["postfix"]
            mes = int(values["mes"])

            inloop = Y_waarde * 10 - Y_waarde



            print(type(int(values["order_number"])))
            # aantallen = int(values[0])
            # print(aantallen)
            # mes_wik.df_csv_rol_builder_met_rolnummer()

            # ___________________________________________________________________________________
            csvs = [x for x in os.listdir(path_vdp) if x.endswith(".csv")]
            print(csvs)
            for file in csvs:
                naam = f"{path_vdp}/{file}"  # /VDP_map
                print(naam)
                if os.path.exists(naam):
                    os.remove(naam)
                else:
                    print("empty")

            csvs = [x for x in os.listdir(path) if x.endswith(".csv")]
            print(csvs)
            for file in csvs:
                naam = f"{path}/{file}"  # /tmp
                print(naam)
                if os.path.exists(naam):
                    os.remove(naam)
                else:
                    print("empty")

            VDP_final = [x for x in os.listdir(path_final) if x.endswith(".csv")]
            print(VDP_final)

            for file in VDP_final:
                naam = f"{path_final}/{file}"
                if os.path.exists(naam):
                    os.remove(naam)
                else:
                    print("empty")
            # _____________________________

            beginlijst = mes_wik.rol_num_dikt(begin_nummer,vlg,totaal_aantal,aantal_per_rol)


            count = 0
            for key in beginlijst.items():
                rol_nummer = key[0]
                beginnummer = int(key[1])
                filenaam = f'tmp{count:>{0}{6}}.csv'
                padnaam = Path(path, filenaam)
                print(padnaam)
                mes_wik.df_csv_rol_builder_met_rolnummer(beginnummer, posities, vlg, aantal_per_rol, wikkel, '', '',
                                                 rol_nummer).to_csv(padnaam, index=0)
                count += 1
                print(beginnummer, filenaam)



            aantal_rollen = len(beginlijst)
            print(f'aantal rollen {aantal_rollen}')
            combinaties = aantal_rollen // mes

            csv_files_in_tmp = [x for x in os.listdir(path) if x.endswith(".csv")]
            print(csv_files_in_tmp)
            sorted_files = sorted(csv_files_in_tmp)
            print(f'sortedfiles {sorted_files}')

            combinatie_binnen_mes = []
            begin = 0
            eind = mes
            for combi in range(combinaties):
                print(begin , eind)

                combinatie_binnen_mes.append(sorted_files[begin:eind])

                begin += mes
                eind += mes

            print(combinatie_binnen_mes)

            if mes == 4:
                mes_wik.mes_4(combinatie_binnen_mes, ordernummer)

                combinatie = sorted([x for x in os.listdir(path_vdp) if x.endswith(".csv")])
                # print(combinatie)
                mes_wik.stapel_df_baan(combinatie, ordernummer)

                VDP_final = [x for x in os.listdir(path_final) if x.endswith(".csv")]
                # print(VDP_final)
                mes_wik.wikkel_4_baans_tc(VDP_final, Y_waarde,  inloop)

            elif mes == 5:

                mes_wik.mes_5(combinatie_binnen_mes, ordernummer)

                combinatie = sorted([x for x in os.listdir(path_vdp) if x.endswith(".csv")])
                # print(combinatie)
                mes_wik.stapel_df_baan(combinatie, ordernummer)

                VDP_final = [x for x in os.listdir(path_final) if x.endswith(".csv")]
                # print(VDP_final)
                mes_wik.wikkel_5_baans_tc(VDP_final, Y_waarde, inloop)


    window.close()

if __name__ == '__main__':
    main()
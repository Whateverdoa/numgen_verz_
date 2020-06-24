import pandas as pd
import os
from paden import *


def lijstmaker(begin_nummer, totaal, aantal_per_rol):
    begin_nummer_lijst = [
        begin for begin in range(begin_nummer, begin_nummer + totaal - 1, aantal_per_rol)
    ]
    return begin_nummer_lijst


def rol_nummer_lijst(lijst):
    rol_nummers = [f'Rol {num:>{0}{3}}' for num in range(1, len(lijst) + 1)]
    return rol_nummers


def kol_naam_lijst_builder(mes=1):
    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'lees_per_lijst_file_{count:>{0}{4}}'
        print(naam)
        naam = pd.read_csv(posix_pad_naar_file, dtype="str")
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes)
    print(f'kolomnamen = {kolomnamen}')
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]
    # print(lijst_over_axis_1)

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1

    # naam = pd.read_csv(csv)  # naam = pd.read_csv(f'{pad}/{csv}')
    # concatlist.append(naam)

    # lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    # return lijst_over_axis_1


def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ";"
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"Kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)

    namen = list_to_string(kollomnaamlijst)

    return namen


def mes_3(lissst, ordernum):
    """builds  and concats 4 files over axis 1
    mes waarde toevoegen en list comporhension

    """
    stapel = []
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]

        color_1 = f"Baan_{index + 1:>{0}{3}}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"{path}\{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}\{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}\{c}", ",", dtype="str")

        combinatie_samenvoegen = pd.concat([file_1, file_2, file_3], axis=1)

        combinatie_samenvoegen.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",

        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        combinatie_samenvoegen.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}nieuw.csv", ";", encoding="utf-8"
        )


def wikkel_3_baans_tc(input_vdp_lijst, etikettenY, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"
        print(path_vdp / f"{file_naam}")

        with open(path_final / f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(path_final / f"def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;num_1;omschrijving_1;pdf_1;num_2;omschrijving_2;pdf_2;num_3;omschrijving_3;pdf_3\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg
            target.writelines(readline[1:etikettenY + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-etikettenY:])


def df_csv_rol_builder_met_rolnummer(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                     rolnummer, veelvoud=1):
    rol = [
        (f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "leeg.pdf")
        for getal in range(
            begin_nummer_uit_lijst, (begin_nummer_uit_lijst + aantal_per_rol))
        for i in range(veelvoud)
    ]
    df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol * veelvoud) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [(f"{prefix}{x:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(2)],
        columns=["num", "omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [(f"{prefix}{x:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(wikkel)],
        columns=["num", "omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", f"{rolnummer} {begin} t/m {eind}", "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def losse_csv_rollen_builder(posities,
                             vlg,
                             aantal_per_rol,
                             wikkel,
                             begin_nummer_lijst,
                             prefix,
                             postfix,
                             lijst_rolnummer):
    builder = [
        df_csv_rol_builder_met_rolnummer(begin, posities, vlg, aantal_per_rol, wikkel, prefix, postfix,
                                         lijst_rolnummer).to_csv(
            f"{path}/tmp{begin:>{0}{6}}.csv", index=0
        )
        for begin in begin_nummer_lijst
    ]
    # return len(builder)


def rol_num_dikt(begin, vlg, totaal, aantal_per_rol):
    """"maak twee lijsten nummers en rolnummers voeg samen tot dikt"""
    rollen_metbegin_nummers = {}

    beginnummers = [f'{begin:>{0}{vlg}}' for begin in range(begin, begin + totaal, aantal_per_rol)]

    # beginnummers
    aantal_rollen = len(beginnummers)
    getallenvoorrol = len(str(aantal_rollen))

    # rolnummers
    rolnummers = [f'Rol {rolnummer:>{0}{getallenvoorrol}}' for rolnummer in range(1, aantal_rollen + 1)]
    rollen_metbegin_nummers = {rolnummers[i]: beginnummers[i] for i in range(aantal_rollen)}
    # rollen_metbegin_nummers
    return rollen_metbegin_nummers


# todo create class!!! namedtuple

# beginlijst=rol_num_dikt(1, 3, 1000,100)

# for key in beginlijst.items():
#     print(key[0])
#     rol_nummer = key[0]
#     print(key[1])
#     beginnummer =int(key[1])
#     df_csv_rol_builder_met_rolnummer(beginnummer,4,0,100,10,'','',rol_nummer).to_csv("testmetrolnummer.csv")

# posities=4
# vlg=0
# aantal_per_rol=1000
# wikkel=12
# prefix=''
# postfix=''
#
# print(path.is_dir())
# path.mkdir(parents=True, exist_ok=True)
# print(path.is_dir())


# count=0
# for key in beginlijst.items():
#
#     rol_nummer = key[0]
#     beginnummer = int(key[1])
#     filenaam= f'tmp{count:>{0}{6}}.csv'
#     df_csv_rol_builder_met_rolnummer(beginnummer, posities, vlg, aantal_per_rol, wikkel, '', '', rol_nummer).to_csv(path / filenaam, index=0)
#     count+=1
#     print(beginnummer, filenaam)
def mes_2(lissst, ordernum):
    """builds  and concats 4 files over axis 1
    mes waarde toevoegen en list comporhension

    """
    stapel = []
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]

        color_1 = f"Baan_{index + 1:>{0}{3}}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"{path}\{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}\{b}", ",", dtype="str")

        combinatie_samenvoegen = pd.concat([file_1, file_2], axis=1)

        combinatie_samenvoegen.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        combinatie_samenvoegen.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}nieuw.csv", ";", encoding="utf-8"
        )


def wikkel_2_baans_tc(input_vdp_lijst, etikettenY, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"
        print(path_vdp / f"{file_naam}")

        with open(path_final / f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(path_final / f"def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;num_1;omschrijving_1;pdf_1;num_2;omschrijving_2;pdf_2\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg
            target.writelines(readline[1:etikettenY + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-etikettenY:])


def mes_4(lissst, ordernum):
    """builds  and concats 4 files over axis 1
    mes waarde toevoegen en list comporhension

    """
    stapel = []
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]

        color_1 = f"Baan_{index + 1:>{0}{3}}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"{path}\{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}\{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}\{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"{path}\{d}", ",", dtype="str")

        combinatie_samenvoegen = pd.concat([file_1, file_2, file_3, file_4], axis=1)

        combinatie_samenvoegen.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        combinatie_samenvoegen.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}nieuw.csv", ";", encoding="utf-8"
        )


def wikkel_4_baans_tc(input_vdp_lijst, etikettenY, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;num_1;omschrijving_1;pdf_1;num_2;omschrijving_2;pdf_2;num_3;omschrijving_3;pdf_3;num_4;omschrijving_4;pdf_4\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg
            target.writelines(readline[1:etikettenY + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-etikettenY:])


def mes_5(lissst, ordernum):
    """builds  and concats 4 files over axis 1
    mes waarde toevoegen en list comporhension

    """
    stapel = []
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]

        color_1 = f"Baan_{index + 1:>{0}{3}}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"{path}\{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}\{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}\{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"{path}\{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"{path}\{e}", ",", dtype="str")

        combinatie_samenvoegen = pd.concat(
            [file_1, file_2, file_3, file_4, file_5], axis=1
        )

        combinatie_samenvoegen.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        combinatie_samenvoegen.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_5_baans_tc(input_vdp_lijst, etikettenY, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;num_1;omschrijving_1;pdf_1;num_2;omschrijving_2;pdf_2;num_3;omschrijving_3;pdf_3;num_4;omschrijving_4;pdf_4;num_5;omschrijving_5;pdf_5\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg
            target.writelines(readline[1:etikettenY + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-etikettenY:])


def read_out_6(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"tmp/{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"tmp/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"tmp/{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"tmp/{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"tmp/{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"tmp/{f}", ",", dtype="str")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6

            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",

        ]

        # samengevoeg_10.fillna(
        #     {
        #         "pdf_1": "stans.pdf",
        #         "pdf_2": "stans.pdf",
        #         "pdf_3": "stans.pdf",
        #         "pdf_4": "stans.pdf",
        #         "pdf_5": "stans.pdf",
        #         "pdf_6": "stans.pdf",
        #         "pdf_7": "stans.pdf",
        #         "pdf_8": "stans.pdf",
        #         "pdf_9": "stans.pdf",
        #         "pdf_10": "stans.pdf",
        #     },
        #     inplace=True,
        # )

        samengevoeg_10.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_6_baans_tc(input_vdp_lijst, y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;" + kolom_naam_gever_num_pdf_omschrijving(
                    6))  # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:y_waarde])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-y_waarde:])  # check of dit laatste uit file is


def read_out_7(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"tmp/{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"tmp/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"tmp/{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"tmp/{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"tmp/{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"tmp/{f}", ",", dtype="str")

        file_7 = pd.read_csv(f"tmp/{g}", ",", dtype="str")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6,
                file_7,

            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",
            "num_7",
            "omschrijving_7",
            "pdf_7"

        ]

        # samengevoeg_10.fillna(
        #     {
        #         "pdf_1": "stans.pdf",
        #         "pdf_2": "stans.pdf",
        #         "pdf_3": "stans.pdf",
        #         "pdf_4": "stans.pdf",
        #         "pdf_5": "stans.pdf",
        #         "pdf_6": "stans.pdf",
        #         "pdf_7": "stans.pdf",
        #         "pdf_8": "stans.pdf",
        #         "pdf_9": "stans.pdf",
        #         "pdf_10": "stans.pdf",
        #     },
        #     inplace=True,
        # )

        samengevoeg_10.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_7_baans_tc(input_vdp_lijst, y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;" + kolom_naam_gever_num_pdf_omschrijving(
                    7))  # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:y_waarde])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-y_waarde:])  # check of dit laatste uit file is


def read_out_8(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]
        h = lissst[index][7]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"tmp/{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"tmp/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"tmp/{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"tmp/{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"tmp/{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"tmp/{f}", ",", dtype="str")

        file_7 = pd.read_csv(f"tmp/{g}", ",", dtype="str")
        file_8 = pd.read_csv(f"tmp/{h}", ",", dtype="str")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6,
                file_7,
                file_8,

            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",
            "num_7",
            "omschrijving_7",
            "pdf_7",
            "num_8",
            "omschrijving_8",
            "pdf_8"

        ]

        # samengevoeg_10.fillna(
        #     {
        #         "pdf_1": "stans.pdf",
        #         "pdf_2": "stans.pdf",
        #         "pdf_3": "stans.pdf",
        #         "pdf_4": "stans.pdf",
        #         "pdf_5": "stans.pdf",
        #         "pdf_6": "stans.pdf",
        #         "pdf_7": "stans.pdf",
        #         "pdf_8": "stans.pdf",
        #         "pdf_9": "stans.pdf",
        #         "pdf_10": "stans.pdf",
        #     },
        #     inplace=True,
        # )

        samengevoeg_10.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_8_baans_tc(input_vdp_lijst, y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;" + kolom_naam_gever_num_pdf_omschrijving(
                    8))  # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:y_waarde])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-y_waarde:])  # check of dit laatste uit file is


def read_out_9(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]
        h = lissst[index][7]
        i = lissst[index][8]
        j = lissst[index][9]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"tmp/{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"tmp/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"tmp/{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"tmp/{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"tmp/{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"tmp/{f}", ",", dtype="str")

        file_7 = pd.read_csv(f"tmp/{g}", ",", dtype="str")
        file_8 = pd.read_csv(f"tmp/{h}", ",", dtype="str")

        file_9 = pd.read_csv(f"tmp/{i}", ",", dtype="str")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6,
                file_7,
                file_8,
                file_9
            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",
            "num_7",
            "omschrijving_7",
            "pdf_7",
            "num_8",
            "omschrijving_8",
            "pdf_8",
            "num_9",
            "omschrijving_9",
            "pdf_9"
        ]

        # samengevoeg_10.fillna(
        #     {
        #         "pdf_1": "stans.pdf",
        #         "pdf_2": "stans.pdf",
        #         "pdf_3": "stans.pdf",
        #         "pdf_4": "stans.pdf",
        #         "pdf_5": "stans.pdf",
        #         "pdf_6": "stans.pdf",
        #         "pdf_7": "stans.pdf",
        #         "pdf_8": "stans.pdf",
        #         "pdf_9": "stans.pdf",
        #         "pdf_10": "stans.pdf",
        #     },
        #     inplace=True,
        # )

        samengevoeg_10.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_9_baans_tc(input_vdp_lijst, y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;" + kolom_naam_gever_num_pdf_omschrijving(
                    9))  # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:y_waarde])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-y_waarde:])  # check of dit laatste uit file is


def read_out_10(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]
        h = lissst[index][7]
        i = lissst[index][8]
        j = lissst[index][9]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"tmp/{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"tmp/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"tmp/{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"tmp/{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"tmp/{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"tmp/{f}", ",", dtype="str")

        file_7 = pd.read_csv(f"tmp/{g}", ",", dtype="str")
        file_8 = pd.read_csv(f"tmp/{h}", ",", dtype="str")

        file_9 = pd.read_csv(f"tmp/{i}", ",", dtype="str")
        file_10 = pd.read_csv(f"tmp/{j}", ",", dtype="str")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6,
                file_7,
                file_8,
                file_9,
                file_10,
            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "num_1",
            "omschrijving_1",
            "pdf_1",
            "num_2",
            "omschrijving_2",
            "pdf_2",
            "num_3",
            "omschrijving_3",
            "pdf_3",
            "num_4",
            "omschrijving_4",
            "pdf_4",
            "num_4",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",
            "num_7",
            "omschrijving_7",
            "pdf_7",
            "num_8",
            "omschrijving_8",
            "pdf_8",
            "num_9",
            "omschrijving_9",
            "pdf_9",
            "num_10",
            "omschrijving_10",
            "pdf_10"
        ]

        # samengevoeg_10.fillna(
        #     {
        #         "pdf_1": "stans.pdf",
        #         "pdf_2": "stans.pdf",
        #         "pdf_3": "stans.pdf",
        #         "pdf_4": "stans.pdf",
        #         "pdf_5": "stans.pdf",
        #         "pdf_6": "stans.pdf",
        #         "pdf_7": "stans.pdf",
        #         "pdf_8": "stans.pdf",
        #         "pdf_9": "stans.pdf",
        #         "pdf_10": "stans.pdf",
        #     },
        #     inplace=True,
        # )

        samengevoeg_10.to_csv(
            f"{path_vdp}/{ordernum}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_10_baans_tc(input_vdp_lijst, y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_final}/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{path_final}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;" + kolom_naam_gever_num_pdf_omschrijving(
                    10))  # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:y_waarde])

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf;0;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-y_waarde:])  # check of dit laatste uit file is


def stapel_df_baan(lijstin, ordernummer):
    stapel_df = []
    for index in range(len(lijstin)):
        print(lijstin[index])
        to_append_df = pd.read_csv(
            f"{path_vdp}/{lijstin[index]}", ";", dtype="str"
        )  #
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";", index=0)


def stapel_df_baan_met_df_lijst(lijst_van_dataframes, ordernummer):
    pd.concat(lijst_van_dataframes, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";")


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".;;stans.pdf;" * mes)
    inlooplijst = inlooplijst[:-1] + "\n"  # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = path_final / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])

# print(VDP_final)

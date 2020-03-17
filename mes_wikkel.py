import pandas as pd
import os
from paden import *

def lijstmaker(begin_nummer, totaal, aantal_per_rol):
    begin_nummer_lijst = [
        begin for begin in range(begin_nummer, begin_nummer + totaal - 1, aantal_per_rol)
    ]
    return begin_nummer_lijst

def rol_nummer_lijst(lijst):
    rol_nummers = [f'Rol {num:>{0}{3}}' for num in range(1,len(lijst)+1)]
    return rol_nummers


def mes_algemeen(lijst_met_posix_pad):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for csv in lijst_met_posix_pad:
        print(csv)
        naam = f'file{count}'

        naam = pd.read_csv(f'{pad}/{csv}')
        concatlist.append(naam)

    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    return lijst_over_axis_1


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


def df_csv_rol_builder_met_rolnummer(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix, rolnummer):

    rol = [
        (f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "leeg.pdf")
        for getal in range(
            begin_nummer_uit_lijst, (begin_nummer_uit_lijst + aantal_per_rol)
        )
    ]
    df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [("0", "", "stans.pdf") for x in range(2)],
        columns=["num", "omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [("0", "", "stans.pdf") for x in range(wikkel)],
        columns=["num", "omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [["0", f"{rolnummer} {begin} t/m {eind}", "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def losse_csv_rollen_builder(posities, vlg, aantal_per_rol, wikkel, begin_nummer_lijst, prefix,  postfix, lijst_rolnummer):
    builder = [
        df_csv_rol_builder_met_rolnummer(begin, posities, vlg, aantal_per_rol, wikkel,  prefix,  postfix, rol).to_csv(
        f"{path}/tmp{begin:>{0}{6}}.csv", index=0
    )
    for begin in begin_nummer_lijst
    ]
    # return len(builder)

def rol_num_dikt(begin,vlg, totaal, aantal_per_rol):
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

# todo create class!!!

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
            target.writelines(readline[1:etikettenY+1])
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
            target.writelines(readline[1:etikettenY+1])
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



def stapel_df_baan(lijstin, ordernummer):
    stapel_df = []
    for index in range(len(lijstin)):
        print(lijstin[index])
        to_append_df = pd.read_csv(
            f"{path_vdp}/{lijstin[index]}", ";", dtype="str", index_col=0
        )
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";")





def csv_bouwer_met_rolnummer():
    pass



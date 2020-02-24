import pandas as pd
import os

# build GUI

date = "2019-11-29"  # @param {type: "date"}
ordernummer = "202005960"  # @param {type: "string"}
# nummering= True  #@param {type: "boolean"}
# Soort_VDP = "Nummers"  #@param ['Nummers', 'Pdf_beelden']

totaal = 50000  # @param {type: "number"}
aantal_per_rol = 2500  # @param {type: "number"}
mes = 5  # @param {type: "number"}
begin_nummer = 1600001  # @param {type: "number"}
posities = 7  # @param {type: "number"}
vlg = 0  # @param {type: "number"}
formaat_hoogte = 130  # @param {type: "number"}
formaat_breedte = 50  # @param {type: "number"}
wikkel = 12  # @param {type: "number"}
etikettenY = 7
postfix = 'MG'
prefix= ''

inloop = etikettenY * 10 - etikettenY

# 22500561000
# 22500681000

path = "tmp/"
path_vdp = "VDP_map/"
path_final = "VDP_final"
try:
    os.mkdir(path_final)
    os.mkdir(path)
    os.mkdir(path_vdp)

except OSError as error:
    print("dirs exist")

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
# ___________________________________________________________________________________


# tuple maken met rolnummer?

begin_nummer_lijst = [
    begin for begin in range(begin_nummer, begin_nummer + totaal - 1, aantal_per_rol)
]
# print(begin_nummer_lijst)
begin_eind_nummer_lijst = [
    [begin, begin + aantal_per_rol - 1] for begin in begin_nummer_lijst
]
# print(begin_eind_nummer_lijst)

belijst = [
    [f"{begin:>{vlg}{posities}};{(begin + aantal_per_rol -1):>{vlg}{posities}}"] for begin in begin_nummer_lijst
]

print(mes)
aantal_rollen = len(begin_nummer_lijst)
combinaties = aantal_rollen // mes

print(f"aantal lege banen = {aantal_rollen%mes}")


def df_csv_rol_builder(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel):

    rol = [
        (f"{getal:>{vlg}{posities}}{postfix}", "", "leeg.pdf")
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
        [["0", f"{begin} t/m {eind}", "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam





losse_csv_rollen_builder = [
    df_csv_rol_builder(begin, posities, vlg, aantal_per_rol, wikkel).to_csv(
        f"{path}/tmp{begin:>{0}{6}}.csv", index=0
    )
    for begin in begin_nummer_lijst
]

csvs = [x for x in os.listdir(path_vdp) if x.endswith(".csv")]
print(csvs)

for file in csvs:
    naam = f"{path_vdp}{file}"  # /content/tmp
    if os.path.exists(naam):
        os.remove(naam)
    else:
        print("empty")


df_rollen_builder = [
    df_csv_rol_builder(begin, posities, vlg, aantal_per_rol, wikkel)
    for begin in begin_nummer_lijst
]

csv_files_in_tmp = [x for x in os.listdir(path) if x.endswith(".csv")]
sorted_files = sorted(csv_files_in_tmp)
combinatie_binnen_mes = []
print(combinatie_binnen_mes)
print(combinaties)

begin = 0
eind = mes

for combinatie in range(combinaties):
    combinatie_binnen_mes.append(sorted_files[begin:eind])
    begin += mes
    eind += mes


print(len(combinatie_binnen_mes) * mes)


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

        file_1 = pd.read_csv(f"{path}{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"{path}{d}", ",", dtype="str")

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
            f"{path_vdp}{ordernummer}_{color_1}nieuw.csv", ";", encoding="utf-8"
        )

def wikkel_4_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"{path_vdp}/{file_naam}", "r", encoding="utf-8") as target:
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

        file_1 = pd.read_csv(f"{path}{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"{path}{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"{path}{e}", ",", dtype="str")

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
            f"{path_vdp}{ordernummer}_{color_1}.csv", ";", encoding="utf-8"
        )


def wikkel_5_baans_tc(input_vdp_lijst):
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


def mes_6(lissst, ordernum):
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
        f = lissst[index][5]

        color_1 = f"Baan_{index + 1:>{0}{3}}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"{path}{a}", ",", dtype="str")
        file_2 = pd.read_csv(f"{path}{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}{c}", ",", dtype="str")
        file_4 = pd.read_csv(f"{path}{d}", ",", dtype="str")

        file_5 = pd.read_csv(f"{path}{e}", ",", dtype="str")
        file_6 = pd.read_csv(f"{path}{f}", ",", dtype="str")

        combinatie_samenvoegen = pd.concat(
            [file_1, file_2, file_3, file_4, file_5, file_6], axis=1
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
            "num_5",
            "omschrijving_5",
            "pdf_5",
            "num_6",
            "omschrijving_6",
            "pdf_6",
        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        combinatie_samenvoegen.to_csv(
            f"{path_vdp}{ordernummer}_{color_1}nieuw.csv", ";", encoding="utf-8"
        )


def stapel_df_baan(lijstin, ordernummer):
    stapel_df = []
    for index in range(len(lijstin)):
        print(lijstin[index])
        to_append_df = pd.read_csv(
            f"{path_vdp}{lijstin[index]}", ";", dtype="str", index_col=0
        )
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{path_final}/VDP_{ordernummer}.csv", ";")


#     pd.concat(stapel_df, axis = 0).to_excel(f"{ordernummer}.xlsx",";")

if mes == 4:
    mes_4(combinatie_binnen_mes, ordernummer)

    VDP_final = [x for x in os.listdir(path_vdp) if x.endswith(".csv")]
    # print(VDP_final)
    wikkel_4_baans_tc(VDP_final)

elif mes == 5:
    mes_5(combinatie_binnen_mes, ordernummer)

    combinatie = sorted([x for x in os.listdir(path_vdp) if x.endswith(".csv")])
    # print(combinatie)
    stapel_df_baan(combinatie, ordernummer)

    VDP_final = [x for x in os.listdir(path_final) if x.endswith(".csv")]
    # print(VDP_final)
    wikkel_5_baans_tc(VDP_final)

elif mes == 6:
    mes_6(combinatie_binnen_mes, ordernummer)



import pandas as pd
import os
from paden import *


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

        file_1 = pd.read_csv(f"{path}/{a}", ",", dtype="str")

        file_2 = pd.read_csv(f"{path}/{b}", ",", dtype="str")

        file_3 = pd.read_csv(f"{path}/{c}", ",", dtype="str")

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
            "pdf_3"
        ]
        # kolomnamen_samenvoegen = (";").join([f"'omschrijving_{num}','pdf_{num}'" for num in range(1,mes+1)])

        # samengevoeg_3.fillna({'pdf_1':"stans.pdf",'pdf_2':"stans.pdf",'pdf_3':"stans.pdf"}, inplace=True)

        return combinatie_samenvoegen.to_csv(
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

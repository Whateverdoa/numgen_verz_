import pandas as pd


def rest():
    """geeft de variabele totaal terug voor aantal etiketten in restrollen"""

    def rest_rollen_uitrekenen(mes, totaal, aantal_per_rol):
        """het totaal delen door de aantal per rol  de restwaarde hievan geeft het aantal rollen dat te kort is"""
        if totaal <= mes * aantal_per_rol:

            # print(f'aantal rest rollen = {abs((mes * aantal_per_rol - totaal) // aantal_per_rol)} uit if')
            return abs((mes * aantal_per_rol - totaal) // aantal_per_rol) * aantal_per_rol


        elif (totaal // aantal_per_rol) % mes == 0:
            return 0
            # print(f'aantal rest rollen = {rest_rollen} uit else')
        else:
            return (mes - (totaal // aantal_per_rol) % mes) * aantal_per_rol

    return rest_rollen_uitrekenen


rest_uitrekenen = rest()


def rol_num_dikt(begin, vlg, totaal, aantal_per_rol, rol_nummer=0):
    """"maak twee lijsten nummers en rolnummers voeg samen tot dikt"""
    rollen_metbegin_nummers = {}

    beginnummers = [f'{begin:>{0}{vlg}}' for begin in range(begin, begin + totaal, aantal_per_rol)]

    # beginnummers
    aantal_rollen = len(beginnummers)
    getallenvoorrol = len(str(aantal_rollen))

    # rolnummers
    rolnummers = [f'Rol {rolnummer:>{0}{getallenvoorrol}}' for rolnummer in
                  range(rol_nummer + 1, rol_nummer + aantal_rollen + 1)]
    rollen_metbegin_nummers = {rolnummers[i]: beginnummers[i] for i in range(aantal_rollen)}
    # rollen_metbegin_nummers
    return rollen_metbegin_nummers


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
        [(f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "stans.pdf") for getal in range(2)],
        columns=["num", "omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [(f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "stans.pdf") for getal in range(wikkel)],
        columns=["num", "omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", f"{rolnummer} {begin} t/m {eind}",
          "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def df_lege_csv_rol_builder_met_rolnummer(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix,
                                          postfix,
                                          rolnummer, veelvoud=1):
    rol = [
        (f"{prefix}{getal:>{vlg}{posities}}{postfix}", "", "stans.pdf")
        for getal in range(
            begin_nummer_uit_lijst, (begin_nummer_uit_lijst + aantal_per_rol))
        for i in range(veelvoud)
    ]
    df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol * veelvoud) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [(f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(2)],
        columns=["num", "omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [(f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", "", "stans.pdf") for x in range(wikkel)],
        columns=["num", "omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{prefix}{begin_nummer_uit_lijst:>{vlg}{posities}}{postfix}", f"{rolnummer} blanco's",
          "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam

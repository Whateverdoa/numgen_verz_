from num_gen_2019 import begin_nummer, vlg, posities, begin_eind_nummer_lijst
import pandas as pd

totaal = 10000  # @param {type: "number"}
aantal_per_rol = 1000  # @param {type: "number"}

aantal_rollen = totaal//aantal_per_rol


# mydict = {k: v for k, v in iterable}
#


rol_nummers = [f'Rol {rolnummer}' for rolnummer in range(1, aantal_rollen + 1)]
print(rol_nummers)

begin_nummer_lijst = [
    begin for begin in range(begin_nummer, begin_nummer + totaal - 1, aantal_per_rol)
]

d = dict((rol_nummers, begin_nummer_lijst) for (rol_nummers, begin_nummer_lijst) in zip(rol_nummers, begin_nummer_lijst))

begin = d[rol_nummers[0]]
print(begin)
key_list = list(d.keys())
rolnr = key_list[0]
val_list = list(d.values())

# list out keys and values separately


rol: object = [
        (f"{getal:>{vlg}{posities}}", "", "leeg.pdf")
        for getal in range(
            begin, (begin + aantal_per_rol)
        )
    ]
df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf"])

sluitstuk = pd.DataFrame(
        [["0", f"{begin} t/m eind {rolnr}", "stans.pdf"]],
        columns=["num", "omschrijving", "pdf"],
    )


for i in range(len(begin_nummer_lijst)):
    print(key_list[i])
    print(val_list[i])



# Creating an empty dictionary
myDict = {}

# Adding list as value
# myDict["key1"] = [1, 2]
# myDict["key2"] = ["Geeks", "For", "Geeks"]



for i in range(1,len(begin_eind_nummer_lijst)):
    key= f'Rol {i}'
    myDict[key]= begin_eind_nummer_lijst[i]

print(myDict)

beginnummer_uit_dict = myDict["Rol 1"][0]
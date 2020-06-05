"""deze summary komt niet uit de form"""

import pandas as pd
import os
from pathlib import Path

# todo kan dit betger gewoon in main form zetten zetten

# from num_gen_2019 import begin_eind_nummer_lijst, belijst, ordernummer, sumlijst
#
#
# beg_eind_lijst_df = pd.DataFrame(sumlijst, dtype ="str")
#
#
# beg_eind_lijst_df.to_csv(f"summary/{ordernummer}_sum.csv",  index=0)

# todo css

def html_sum_form_writer(titel="summary", **kwargs):
    """"build a html file for summary purposes with  *kwargv
    search jinja and flask
    css link toevoegen
    """
    for key, value in kwargs.items():
        print(key, value)

    naam_html_file = f'summary/{titel}_.html'
    with open(naam_html_file, "w") as f_html:

        #         for key, value in kwargs.items():
        #             print(key, value)

        print("<!DOCTYPE html>\n", file=f_html)
        print('<html lang = "en">\n', file=f_html)
        print("     <head>\n", file=f_html)
        print("<meta charset='UTF-8>'\n", file=f_html)
        print(f"<title>{titel.capitalize()}</title>\n", file=f_html)
        print("     </head>", file=f_html)
        print("         <body>", file=f_html)
        for key, value in kwargs.items():
            print(f' <p><b>{key}</b> : {value}<p/>', file=f_html)

        print("         </body>", file=f_html)
        print(" </html>", file=f_html)
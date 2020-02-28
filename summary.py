import pandas as pd
import os
from pathlib import Path

from num_gen_2019 import begin_eind_nummer_lijst, belijst, ordernummer, sumlijst


beg_eind_lijst_df = pd.DataFrame(sumlijst, dtype ="str")


beg_eind_lijst_df.to_csv(f"summary/{ordernummer}_sum.csv",  index=0)



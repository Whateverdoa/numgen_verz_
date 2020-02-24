import pandas as pd
import os
from pathlib import Path

from num_gen_2019 import begin_eind_nummer_lijst, belijst, ordernummer


beg_eind_lijst_df = pd.DataFrame(belijst, dtype ="str")


beg_eind_lijst_df.to_csv(f"summary\{ordernummer}_sum.csv",  index=0)

print(beg_eind_lijst_df.head())

summary = [x for x in os.listdir("tmp") if x.endswith(".csv")]
print(summary)

sum_lijst_vert = []
count = 0

# for naam in summary:
#     df = f'df{count}'
#     print(df)
#     df = pd.read_csv(f'tmp/{naam}', dtype="str", encoding="utf-8")
#     #     df2 = pd.DataFrame([[f'{ordernummer}_baan_{count+1}']], dtype="str")
#     df2 = pd.DataFrame([[f'{ordernummer}_baan_{count + 1}']], dtype="str")
#     sum_lijst_vert.append(df2)
#     sum_lijst_vert.append(df)
#
#     count += 1
#
#     sam2 = pd.concat(sum_lijst_vert, axis=0, sort=True).to_csv(f"{ordernummer}_v_sum.csv", ";", )
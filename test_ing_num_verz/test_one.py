from num_gen_test_form import html_sum_form_writer
from mes_wikkel import lees_per_lijst
from paden import Path
import os



pad_tmp =  Path(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\numgen_verz_\tmp")


csvs = [f'{pad_tmp/x}' for x in os.listdir(pad_tmp) if x.endswith(".csv")]

def test_one_mes_alg():
    mes = lees_per_lijst(pad_tmp)
    expected = []
    assert 1 != 1

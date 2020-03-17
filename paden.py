

from pathlib import Path

wdir = Path.cwd()
pad_summary = wdir / "summary/"
file = "VDP_map"
print(pad_summary.is_dir())

path_vdp = wdir / file
path_final =  wdir / "VDP_final"
path = wdir / "tmp"

# print(path_vdp)
# print(path_final)

def paden_maker(dirname):
    """"maak dirs"""
    path = Path(wdir / dirname)
    print(path)
    return path.mkdir(parents=True, exist_ok=True)


def paden_vernietiger(dirname):
    """'verwijderd dirs dit ligt wat gevoeliger:) dan path.rmdir()"""
    pass


# # path = Path(pad_summary_2)
# path.parent.mkdir(parents=True, exist_ok=True)
#
# path.rmdir()

paden_maker("VDP_final")

# todo fix het paden verhaal
# todo maak in nieuw projekt
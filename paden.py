

from pathlib import Path

wdir = Path.cwd()
pad_summary = wdir / "summary/"
file = r"VDP_map"
print(pad_summary.is_dir())

path_vdp = wdir / file
path_final =  wdir / "VDP_final"
path = wdir / "tmp"

# print(path_vdp)
# print(path_final)
testpad = Path(r"C:\Users\mike\PycharmProjects\ numgen_verz_\VDP_map\VDP_202007992.csv")
testpad.is_file()


# # path = Path(pad_summary_2)
# path.parent.mkdir(parents=True, exist_ok=True)
#
# path.rmdir()
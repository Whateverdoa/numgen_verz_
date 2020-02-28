

from pathlib import Path

wdir = Path.cwd()
pad_summary = wdir / "summary"
pad_summary_2 = wdir / "summary_2"
print(pad_summary.is_dir())



path = Path(pad_summary_2)
path.parent.mkdir(parents=True, exist_ok=True)

path.rmdir()
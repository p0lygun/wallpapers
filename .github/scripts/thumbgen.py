import pathlib
import subprocess
import os
from datetime import datetime
root = pathlib.Path(__file__).parents[2]

with open(root / ".github" / "README_BASE.md", 'r') as FILE:
    readme = FILE.read()

wallpapers = (root / "wallpapers").glob("*")
time_mapping = []

for wallpaper in wallpapers:
    git_cmd = ["git", "log", "--diff-filter=A", "--follow", "--format=%aD", "-1", "--", f"wallpapers/{wallpaper.name}"]
    # gives # Mon, 18 Oct 2021 18:53:41 +0000
    git_out = subprocess.run(git_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    t = datetime.strptime(git_out, "%a, %d %b %Y %H:%M:%S %z")
    time_mapping.append([wallpaper.relative_to(root), t])
time_mapping.sort(key=lambda x: x[1], reverse=True)

# print(time_mapping)
for wallpaper in time_mapping:
    readme += f'<img src="{wallpaper[0].as_posix()}" width="250">'

with open(root / "README.md", 'w') as FILE:
    FILE.write(readme)

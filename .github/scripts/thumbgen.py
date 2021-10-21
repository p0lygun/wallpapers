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
    git_cmd = [*("git log -1 --pretty=format:%ci".split(' ')), f"wallpapers/{wallpaper.name}"]
    # gives # Mon, 18 Oct 2021 18:53:41 +0000
    git_out = subprocess.run(git_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    t = datetime.strptime(git_out, "%Y-%m-%d  %H:%M:%S %z")
    time_mapping.append([wallpaper.relative_to(root), t])
time_mapping.sort(key=lambda x: x[1], reverse=True)

readme += f"> Total wallpapers {len(time_mapping)}  \n" \
          f"> Last wallpaper added [{time_mapping[0][0].name}]({time_mapping[0][0].as_posix()})  \n\n"

# print(time_mapping)
# print(readme)

for wallpaper in time_mapping:
    readme += f'<img src="{wallpaper[0].as_posix()}" width="250">'

with open(root / "README.md", 'w') as FILE:
    FILE.write(readme)

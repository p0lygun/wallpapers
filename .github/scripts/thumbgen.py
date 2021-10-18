import pathlib
with open('README_BASE.md', 'r') as FILE:
    readme = FILE.read()

wallpapers = pathlib.Path("wallpapers/").glob("*")
for wallpaper in wallpapers:
    readme += f'<img src="{wallpaper.as_posix()}" width="250">'

with open('README.md', 'w') as FILE:
    FILE.write(readme)

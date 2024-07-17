"""import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())


import shutil

shutil.make_archive("output", "zip", "files") """

import webbrowser

user_term = input("Enter a search term: ")

webbrowser.open(f"https://google.com/search?q={user_term}")
from coloring import Coloring
import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace("logic", "resources")

os.chdir(dir)

cl = Coloring("file.txt", "index.html")
cl.create_html()
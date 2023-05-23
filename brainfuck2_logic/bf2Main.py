from bf2Translator import BF2Translator
import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = dir.replace("brainfuck2_logic", "resources")

os.chdir(dir)

tr = BF2Translator("bf2file.txt", "output.c")
tr.translate()
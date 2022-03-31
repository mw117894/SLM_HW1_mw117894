import bz2
import os
import pandas
from urllib.request import urlopen

link = "https://database.lichess.org/lichess_db_puzzle.csv.bz2"
filename = "puzzles.csv.bz2"
header = ["PuzzleId", "FEN", "Moves",
          "Rating", "RatingDeviation",
          "Popularity", "NbPlays",
          "Themes", "GameUrl"]

decompressed_filename = "puzzles.csv"

if os.path.isfile(filename):
    print("File {} was already downloaded. Decompressing...".format(filename))

else:
    print("Downloading {} file from {}".format(filename, link))

    with urlopen(link) as content, open(filename, "wb") as file:
        file.write(content.read())
    print("{} downloaded successfully! Decompressing...".format(filename))

if(os.path.isfile(decompressed_filename)):
    print("File was already decompressed into {}".format(decompressed_filename))

else:
    with bz2.open(filename,"rt") as file, open(decompressed_filename,"w") as decompressed_file:
        decompressed_file.write(file.read())
    print("{} successfully decompressed into {}!".format(filename, decompressed_filename))
puzzles = pandas.read_csv(decompressed_filename,names=header)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)
print(puzzles.head())
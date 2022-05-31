import os
import time
from urllib.request import urlopen
import zipfile
import pandas as pd
import networkx
git_zip = "git_web_ml.zip"
link = "https://snap.stanford.edu/data/git_web_ml.zip"

if not os.path.isfile(git_zip):
    print("Downloading zip file...")
    with urlopen(link) as content, open(git_zip, "wb") as file:
        file.write(content.read())
if not os.path.isdir(git_zip):
    print("Unpacking zip file")
    with zipfile.ZipFile(git_zip,'r') as zip:
        zip.extractall("")
print("File unpacked")

print("Reading csv")
edges_df = pd.read_csv("git_web_ml/musae_git_edges.csv")
classes_df = pd.read_csv("git_web_ml/musae_git_target.csv")

print("Creating graph")
graph = networkx.Graph()
graph.add_nodes_from(classes_df["id"])
for index, row in edges_df.iterrows():
    graph.add_edge(row["id_1"],row["id_2"])

print("Counting excecution time of deg_class function")
start_time = time.time()
deg_ml = [0]*len(classes_df)
deg_web = [0]*len(classes_df)
ml_target = classes_df["ml_target"].tolist()

for edge in graph.edges():
    edge_src, edge_dst = edge[0], edge[1]
    if ml_target[edge_dst] == 1:
        deg_ml[edge_src] = 1
    else:
        deg_web[edge_src] = 1

    if ml_target[edge_src] == 1:
        deg_ml[edge_dst] = 1
    else:
        deg_web[edge_dst] = 1

print("Excecution has taken %s seconds"%(time.time()-start_time))

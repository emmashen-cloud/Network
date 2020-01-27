#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:18:47 2018

@author: Mengxi Shen
"""
import operator
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

nutrients = pd.read_csv("nutrients.csv", header=None)
df1 = nutrients.iloc[:37]
df1.columns=["nutrients","products"]
df2 = nutrients.iloc[37:47]
df2.columns=["products","nutrients"]
df3 = nutrients.iloc[47:50]
df3.columns=["nutrients","products"]
df4 = nutrients.iloc[50:60]
df4.columns=["products","nutrients"]
df5 = nutrients.iloc[60:64]
df5.columns=["nutrients","products"]
df6 = nutrients.iloc[64:71]
df6.columns=["products","nutrients"]
df7 = nutrients.iloc[71:72]
df7.columns=["nutrients","products"]
df8 = nutrients.iloc[72:74]
df8.columns=["products","nutrients"]

nutrients=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])

edges = nutrients.values.tolist()
nu_nodes = list(set(nutrients["nutrients"].values.tolist()))
pro_nodes = list(set(nutrients["products"].values.tolist()))

B = nx.Graph()
B.add_nodes_from(nu_nodes, bipartite=0) 
B.add_nodes_from(pro_nodes, bipartite=1)
B.add_edges_from(edges)

pos = {}
pos.update((n, (1, i)) for i, n in enumerate(nutrients["nutrients"])) 
pos.update((n, (2, i)) for i, n in enumerate(nutrients["products"])) 
nx.draw_networkx(B, pos=pos, with_label=True)
plt.savefig("nutrients.png", dpi=200)

print(max(nx.degree_centrality(B).items(), key=operator.itemgetter(1))[0])
print(max(nx.betweenness_centrality(B).items(), key=operator.itemgetter(1))[0])
print(max(nx.eigenvector_centrality(B).items(), key=operator.itemgetter(1))[0])
print(max(nx.nx.closeness_centrality(B).items(), key=operator.itemgetter(1))[0])




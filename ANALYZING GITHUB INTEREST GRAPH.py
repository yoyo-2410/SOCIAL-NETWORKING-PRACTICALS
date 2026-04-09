# pip install requests networkx matplotlib

import requests, networkx as nx, matplotlib.pyplot as plt
from itertools import combinations

users = ["FluffyPal0", "HeyFang", "VipRascal"]

data = {
    u: [r["full_name"] for r in requests.get(
        f"https://api.github.com/users/{u}/starred?per_page=100",
        headers={"User-Agent": "InterestGraph"}
    ).json()]
    for u in users
}

G, labels = nx.Graph(), {}

for u1, u2 in combinations(data, 2):
    common = set(data[u1]) & set(data[u2])
    if common:
        G.add_edge(u1, u2)
        labels[(u1, u2)] = "\n".join(list(common)[:2])

pos = nx.spring_layout(G, k=1)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

plt.title("GitHub Interest Graph")
plt.show()

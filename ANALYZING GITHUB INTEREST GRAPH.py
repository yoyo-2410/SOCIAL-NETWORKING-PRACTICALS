# pip install requests networkx matplotlib

import requests, networkx as nx, matplotlib.pyplot as plt
from itertools import combinations

users = ["FluffyPal0", "HeyFang", "VipRascal"]

def get_repos(u):
    r = requests.get(
        f"https://api.github.com/users/{u}/starred?per_page=100",
        headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "InterestGraph"}
    )
    return [repo["full_name"] for repo in r.json()] if r.status_code == 200 else []

data = {u: get_repos(u) for u in users}

G, labels = nx.Graph(), {}

for u1, u2 in combinations(data, 2):
    common = set(data[u1]) & set(data[u2])
    if common:
        G.add_edge(u1, u2)
        labels[(u1, u2)] = "\n".join(list(common)[:2])

# 🔥 FIXED VISUAL SECTION (this is what you were missing)
plt.figure(figsize=(10, 7))  # restore canvas size
pos = nx.spring_layout(G, k=1)  # same spacing as old code

nx.draw(G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=10)

nx.draw_networkx_edge_labels(G, pos,
                            edge_labels=labels,
                            font_size=8)

plt.title("GitHub Interest Graph")
plt.show()

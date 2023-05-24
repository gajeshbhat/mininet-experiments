# Visualization import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt

def visualize_topology(topology, output_file='topology.png'):
    G = nx.Graph()

    # Add nodes
    for node in topology.nodes():
        G.add_node(str(node))

    # Add edges
    for src, dst in topology.links():
        G.add_edge(str(src), str(dst))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[G.nodes[n].get('color', 'lightblue') for n in G.nodes], font_size=8, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(str(u), str(v)): f'{u}-{v}' for u, v in topology.links()}, font_size=8)

    plt.savefig(output_file)
    plt.show()
import random
import matplotlib.pyplot as plt


def generate_data(num: int = 100):
    nodes = [f'Node{i}' for i in range(1, num + 1)]
    data = {}
    several = 0

    for node in nodes:
        if several < num*0.8:
            connections = random.sample(nodes, k=random.randint(3, 4))
            several += 1
        else:
            connections = random.sample(nodes, k=1)
            while connections[0] == node:
                connections = random.sample(nodes, k=1)

        connections = [conn for conn in connections if conn != node]
        data[node] = connections
    return data


random_data = generate_data()


def build_graph(data):
    text = []

    for node, connections in data.items():
        text.append(f"{node} -> {', '.join(connections)}")

    return "\n".join(text)


print(build_graph(random_data))


def draw_graph(data):
    positions = {node: (10*random.random(), 10*random.random()) for node in data}

    plt.figure(figsize=(10, 8))

    for node, (x, y) in positions.items():
        plt.scatter(x, y, s=200, color='lightblue')
        plt.text(x, y, node[4:], va='center', ha='center')

    for node, connections in data.items():
        x1, y1 = positions[node]
        for conn in connections:
            x2, y2 = positions[conn]
            plt.plot([x1, x2], [y1, y2], color='black', lw=0.5, ls='dashed')

    plt.show()


draw_graph(random_data)

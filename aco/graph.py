import numpy as np

class graph:
    def __init__(self):
        self.graph_size = 100
        self.node_num = 28
        self.tau0 = 1.0
        self.rho = 0.5

        # Generate random node coordinates
        np.random.seed(1222) # Generate same coordinates in all runs
        # Care not to gererate nodes with same coord
        # Not checking duplicate because it's rare case
        self.coord_x = np.random.randint(0, 99, self.node_num)
        self.coord_y = np.random.randint(0, 99, self.node_num)
        self.coords = np.stack([self.coord_x, self.coord_y], 1)

        # Calculate distance of each edge
        self.d = np.zeros((self.node_num, self.node_num))
        for i in range(self.node_num):
            for j in range(i):
                distance = np.linalg.norm(self.coords[i]-self.coords[j])
                self.d[i][j] = distance
                self.d[j][i] = distance

        # Initialize pheromone level of each edge
        self.tau = np.full((self.node_num, self.node_num), self.tau0)

    def total_distance(self, path):
        D = 0
        for index, node in enumerate(path[:-1]):
            D += self.d[node][path[index+1]]
        return D

    def update_pheromone(self, delta_tau):
        for i in range(self.node_num):
            for j in range(i):
                next_tau = (1-self.rho) * self.tau[i][j] + delta_tau[i][j]
                self.tau[i][j] = next_tau
                self.tau[j][i] = next_tau

if __name__ == '__main__':
    g = graph()
    print(g.d)

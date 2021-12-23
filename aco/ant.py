import numpy as np

class ant:
    def __init__(self, graph, alpha, beta):
        self.graph = graph
        self.alpha = alpha
        self.beta = beta
        self.list_unvisited = np.array(list(range(0, self.graph.node_num)))
        self.list_visited = np.empty(0, dtype='int')
        self.D = 99999
        self.delta_tau = np.zeros((self.graph.node_num, self.graph.node_num))

    def travel(self):
        np.random.seed()
        self.start = np.random.randint(0, self.graph.node_num, 1)
        self.__visit(self.start)

        for _ in range(self.graph.node_num - 1):

            present = self.list_visited[-1]

            # Calculate numerators of each destination selection probabilities
            list_numerators = np.empty(0)
            for destination in self.list_unvisited:
                eta = 1 / self.graph.d[present][destination]
                numerator = (self.graph.tau[present][destination]**self.alpha) * (eta**self.beta)
                list_numerators = np.append(list_numerators, numerator)

            # Calculate destination selection probabilites and make cumulative sum list
            list_cumsum = np.zeros(1)
            denominator = np.sum(list_numerators)
            for numerator in list_numerators:
                prob = numerator / denominator
                list_cumsum = np.append(list_cumsum, list_cumsum[-1] + prob)
            list_cumsum = np.delete(list_cumsum, 0)

            # Select destination
            r = np.random.rand()
            destination = self.list_unvisited[np.min(np.where(list_cumsum > r))]
            self.__visit(destination)

        # Append goal
        self.list_visited = np.append(self.list_visited, self.start)

        # Calculate total distance
        self.D = self.graph.total_distance(self.list_visited)

        # Calculate delta_tau, addition of pheromone
        delta_tau = 1 / self.D
        for index, node in enumerate(self.list_visited[:-1]):
            self.delta_tau[node][self.list_visited[index+1]] = delta_tau
            self.delta_tau[self.list_visited[index+1]][node] = delta_tau

    # Append and delete visited node from lists
    def __visit(self, node):
        self.list_visited = np.append(self.list_visited, node)
        self.list_unvisited = np.delete(
            self.list_unvisited,
            np.where(self.list_unvisited == node)
        )


if __name__ == '__main__':
    from graph import graph
    g = graph()
    a = ant(g, 1, 1)
    a.travel()

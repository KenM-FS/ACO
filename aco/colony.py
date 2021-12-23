from aco.ant import ant
import numpy as np

class colony:
    def __init__(self, graph, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.ant_num = 20
        self.graph = graph
        self.best_path_d = 99999
        self.best_path = np.empty(0, dtype='int')
        self.delta_tau = np.zeros((self.graph.node_num, self.graph.node_num))

    def update_colony(self):
        for _ in range(self.ant_num):
            a = ant(self.graph, self.alpha, self.beta)
            a.travel()
            if a.D < self.best_path_d:
                self.best_path_d = a.D
                self.best_path = a.list_visited

            self.delta_tau += a.delta_tau 
        
        self.graph.update_pheromone(self.delta_tau)

if __name__ == '__main__':
    from graph import graph
    g = graph()
    c = colony(g, 1, 1)
    c.update_colony()

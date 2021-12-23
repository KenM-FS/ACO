from aco.graph import graph
from aco.colony import colony
from aco.plot import plot
import numpy as np

class aco:
    def __init__(self, alpha, beta, name):
        self.alpha = alpha
        self.beta = beta
        self.try_max = 300
        self.BOTB_d = 99999
        self.BOTB_path = np.empty(0, dtype='int')
        self.graph = graph()
        self.colony = colony(self.graph, self.alpha, self.beta)
        self.plot_step = np.array([1,5,10,20,50,100,200,300])
        self.plot = plot(name)
        self.d_record = np.empty(0, dtype='float')

    def run_aco(self):
        for step in range(self.try_max):
            self.colony.update_colony()
            self.d_record = np.append(self.d_record, self.colony.best_path_d)
            if self.colony.best_path_d < self.BOTB_d:
                self.BOTB_d = self.colony.best_path_d
                self.BOTB_path = self.colony.best_path

            if np.any(self.plot_step == step+1):
                self.plot.add_ax(
                    step,
                    self.graph,
                    self.colony.best_path,
                    self.colony.best_path_d,
                    self.BOTB_d
                )

if __name__ == '__main__':
    aco = aco(1.5, 2)
    aco.run_aco()
    print(aco.best_of_the_best)

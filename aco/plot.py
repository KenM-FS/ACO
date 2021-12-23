import matplotlib.pyplot as plt
import numpy as np

class plot():
    def __init__(self, name):
        self.fig = plt.figure(figsize=(5.7,9))
        self.ax_index = 1
        self.name = name

    def add_ax(self, step, graph, best_path, best_path_d, BOTB_d):
        ax = self.fig.add_subplot(4,2,self.ax_index)
        ax.set_aspect('equal')
        ax.tick_params(
            labelbottom=False,
            labelleft=False,
            bottom=False,
            left=False,
        )
        for index, node in enumerate(best_path[:-1]):
            x = np.array([graph.coord_x[node], graph.coord_x[best_path[index+1]]])*10
            y = np.array([graph.coord_y[node], graph.coord_y[best_path[index+1]]])*10
            width = graph.tau[node][best_path[index+1]]
            if width > 2:
                width = 2
            if width < 0.15:
                width = 0.15
            ax.plot(x, y, color='m', lw=width, zorder=1)
        ax.scatter(graph.coord_x*10, graph.coord_y*10, marker='s', s=5, zorder=2)
        ax.text(-50, 900, "Step:", ha='right')
        ax.text(-50, 800, step+1, ha='right')
        ax.text(-50, 600, "d_min:", ha='right')
        ax.text(-50, 500, round(best_path_d,2), ha='right')
        # ax.text(-50, 300, "D_min:", ha='right')
        # ax.text(-50, 200, round(BOTB_d, 2), ha='right')
        self.fig.tight_layout()
        self.fig.savefig("./figures/" + self.name + ".png")

        self.ax_index += 1

    def d_plot(d, alpha, beta, name):
        fig = plt.figure()
        ax = fig.add_subplot(
            1,1,1,
            title= r'$\alpha$='+str(alpha)+','+r'$\beta$='+str(beta),
            xlabel='Step',
            ylabel='D_min'
        )
        colorlist = ['r', 'g', 'b']
        color_index = 0
        x = np.linspace(0, 300, 300)
        for trial in d:
            plt.plot(x, trial, color=colorlist[color_index])
            color_index += 1
        fig.savefig("./figures/"+ name + ".png")

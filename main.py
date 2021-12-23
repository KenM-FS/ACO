from aco.aco import aco
from aco.plot import plot
import numpy as np

# alpha=2, beta=1
## trial 1
a2b1_1 = aco(2, 1, "a2b1_1")
a2b1_1.run_aco()
a2b1_ds = np.array([a2b1_1.d_record])
## trial 2
a2b1_2 = aco(2, 1, "a2b1_2")
a2b1_2.run_aco()
a2b1_ds = np.append(a2b1_ds, [a2b1_2.d_record], axis=0)
## trial 3
a2b1_3 = aco(2, 1, "a2b1_3")
a2b1_3.run_aco()
a2b1_ds = np.append(a2b1_ds, [a2b1_3.d_record], axis=0)
plot.d_plot(a2b1_ds, 2, 1, "a2b1")

# alpha=1, beta=1
## trial 1
a1b1_1 = aco(2,1, "a1b1_1")
a1b1_1.run_aco()
a1b1_ds = np.array([a1b1_1.d_record])
## trial 2
a1b1_2 = aco(2,1, "a1b1_2")
a1b1_2.run_aco()
a1b1_ds = np.append(a1b1_ds, [a1b1_2.d_record], axis=0)
## trial 3
a1b1_3 = aco(2,1, "a1b1_3")
a1b1_3.run_aco()
a1b1_ds = np.append(a1b1_ds, [a1b1_3.d_record], axis=0)
plot.d_plot(a1b1_ds, 1, 1, "a1b1")

# alpha=1.5, beta=2
## trial 1
a15b2_1 = aco(1.5, 1, "a15b2_1")
a15b2_1.run_aco()
a15b2_ds = np.array([a15b2_1.d_record])
## trial 2
a15b2_2 = aco(1.5, 1, "a15b2_2")
a15b2_2.run_aco()
a15b2_ds = np.append(a15b2_ds, [a15b2_2.d_record], axis=0)
## trial 3
a15b2_3 = aco(1.5, 1, "a15b2_3")
a15b2_3.run_aco()
a15b2_ds = np.append(a15b2_ds, [a15b2_3.d_record], axis=0)
plot.d_plot(a15b2_ds, 1.5, 2, "a15b2")

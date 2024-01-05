# reports and plots the convergence characteristics

from BFGS import *
from SteepestDescent import *
from NonlinearCG import *
from LBFGS import *
from NewtonCG import *
from NewtonsMethod import *
from SeparableFunctions import *

bfgs = BFGS()
sf = SeparableFunctions()
sd = SteepestDescent()
cg = NonlinearCG()
lbfgs = LBFGS()
ncg = NewtonCG()
nm = NewtonsMethod()




## first order methods (ideal conditions)
# sd.report()
# cg.report()
# sd.plot_cost()
# cg.plot_cost()
# plt.title('First order methods under ideal conditions')
# plt.legend()
# plt.show()

## second order methods (ideal conditions)
# nm.report()
# bfgs.report()
# lbfgs.report()
# ncg.report()
# nm.plot_cost()
# bfgs.plot_cost()
# lbfgs.plot_cost()
# ncg.plot_cost()
# plt.title('Second order methods under ideal conditions')
# plt.legend()
# plt.show()


## first order methods (ill-conditioned)
# sd.report()
# cg.report()
# sd.plot_cost()
# cg.plot_cost()
# plt.title('First order methods ill-conditioned')
# plt.legend()
# plt.show()

# # second order methods (ill-conditioned)
# nm.report()
# bfgs.report()
# lbfgs.report()
# ncg.report()
# nm.plot_cost()
# bfgs.plot_cost()
# lbfgs.plot_cost()
# ncg.plot_cost()
# plt.title('Second order methods ill-conditioned')
# plt.legend()
# plt.show()

# # first order methods (flat curvature)
# sd.report()
# cg.report()
# sd.plot_cost()
# cg.plot_cost()
# plt.title('First order methods flat curvature')
# plt.legend()
# plt.show()


# # second order methods (flat curvature)
# nm.report()
# bfgs.report()
# lbfgs.report()
# ncg.report()
# nm.plot_cost()
# bfgs.plot_cost()
# lbfgs.plot_cost()
# ncg.plot_cost()
# plt.title('Second order methods flat curvature')
# plt.legend()
# plt.show()

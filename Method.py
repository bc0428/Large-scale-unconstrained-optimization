from DERIVATIVES import *

class Method:
    def __init__(self, tolerance = convergence_tolerance, alpha = backtracking_alpha, beta = backtracking_beta, t0 = backtracking_t0):
        """
        :param tolerance: tolerance parameter for termination of the algorithm
        :param alpha: backtracking line search parameter
        :param beta: backtracking line search parameter
        :param t0: backtracking line search parameter
        """
        self.tolerance = tolerance
        self.alpha = alpha
        self.beta = beta
        self.t0 = t0

        self.cost = []

    def __str__(self):
        """
        name of algorithm
        :return:
        """
        pass

    def solve(self):
        """
        main funtion for solving the problem
        :return:
        """
        pass

    def plot_cost(self):
        """
        plot the cost vs step curve
        :return:
        """
        plt.plot(*zip(*enumerate(self.cost)), label = self.__str__())
        plt.xlabel('Steps')
        plt.ylabel('Cost')

    def report(self):
        """
        output convergence characteristics, that is runtime, cost, and steps
        :return:
        """
        start = time.time()
        solution, cost = self.solve()
        end = time.time()
        runtime = end - start

        print(f"{self.__str__()}\nRuntime: {runtime}\nCost: {cost}\nSteps: {len(self.cost)}\n")

        return runtime, len(self.cost), solution, cost
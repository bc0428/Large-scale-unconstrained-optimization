from Method import *
class NonlinearCG(Method):
    def __str__(self):
        return "Nonlinear CG"

    def solve(self) -> np.ndarray:
        x = x0
        gradient_x = gradient(x)
        p = -gradient_x

        while True:
            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)

            # backtracking to determine step size
            t = self.t0
            bound = self.alpha * t * np.inner(np.transpose(gradient_x), p)
            while f(x + t * p) > fx + t * bound:
                t *= self.beta

            # Fletcher-Reeves update
            x1 = x + t * p
            gradient_x1 = gradient(x1)

            beta = (gradient_x1 @ gradient_x1) / (gradient_x @ gradient_x)
            p = -gradient_x1 + beta * p
            gradient_x = gradient_x1
            x = x1

if __name__ == "__main__":
    cg = NonlinearCG()
    runtime, steps, solution, cost = cg.report()
    # nm.plot_cost()
    # plt.show()
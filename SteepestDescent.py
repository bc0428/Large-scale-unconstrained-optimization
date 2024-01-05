from Method import *
class SteepestDescent(Method):
    def __str__(self):
        return "Steepest descent"

    def solve(self):
        x = x0

        while True:
            gradient_x = -gradient(x)

            t = self.t0
            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)

            # backtracking line search
            bound = self.alpha * t * np.inner(np.transpose(gradient_x), gradient_x)
            while f(x + t * gradient_x) > fx + bound * t:
                t *= self.beta

            # step update
            x = x + t * gradient_x

if __name__ == "__main__":
    sd = SteepestDescent()
    runtime, steps, solution, cost = sd.report()
    # nm.plot_cost()
    # plt.show()

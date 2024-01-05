from Method import *
class SeparableFunctions(Method):
    def __str__(self):
        return "Separable functions"

    def solve(self) -> np.ndarray:
        x = x0
        for i in range(n):                  # solve 1-dimensional problem for n times
            xi = x[i]

            cost_i = []
            while True:                     # based on newton's method
                fxi = f(xi, i)
                if len(cost_i) and abs(fxi - cost_i[-1]) <= self.tolerance:
                    x[i] = xi
                    break
                cost_i.append(fxi)
                self.cost.append(f(x))

                gradient_xi = gradient(xi, i)
                inverse_hessian = 1 / (hessian(xi, i))

                # newton step
                dx_nt = -inverse_hessian * gradient_xi


                # backtracking line search
                t = self.t0
                bound = self.alpha * t * gradient_xi * dx_nt
                while f(xi + t * dx_nt, i) > fxi + t * bound:
                    t *= self.beta

                # update
                xi = xi + t * dx_nt

        return x, f(x)


if __name__ == "__main__":
    sf = SeparableFunctions()
    runtime, steps, solution, cost = sf.report()
    # nm.plot_cost()
    # plt.show()
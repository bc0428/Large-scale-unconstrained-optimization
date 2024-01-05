from Method import *
class NewtonCG(Method):
    def __str__(self):
        return "Line search Newton CG"

    def solve(self) -> np.ndarray:
        x = x0

        while True:

            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)

            gradient_x = gradient(x)
            hessian_x = hessian(x)
            gradient_norm = np.linalg.norm(gradient_x)
            CG_tolerance = min(0.5, np.sqrt(gradient_norm)) * gradient_norm

            p = None

            # inner subproblem variables
            z = 0               # final direction (cumulative)
            r = gradient_x      # residual
            d = -r              # direction of each iterates

            j = 0
            while True:                 # inner subproblem using CG to solve descent direction
                Bd = hessian_x @ d
                dBd = d.T @ Bd

                if dBd <= 0:
                    if j == 0:
                        p = d
                        break
                    else:
                        p = z
                        break

                rTr = r.T @ r
                alpha = (rTr) / dBd
                z = z + alpha * d
                r1 = r + alpha * Bd

                if np.linalg.norm(r1) < CG_tolerance:
                    p = z
                    break

                beta = (r1.T @ r1) / rTr
                d = -r1 + beta * d
                r = r1

                j+=1

            # backtracking to determine step size
            t = self.t0
            bound = self.alpha * t * np.inner(np.transpose(gradient_x), p)
            while f(x + t * p) > fx + t * bound:
                t *= self.beta

            # update
            x = x + t * p

if __name__ == "__main__":
    ncg = NewtonCG()
    runtime, steps, solution, cost = ncg.report()
    # ncg.plot_cost()
    # plt.show()
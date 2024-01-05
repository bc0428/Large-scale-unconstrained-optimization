from Method import *

class BFGS(Method):
    def __str__(self):
        return "BFGS"

    def solve(self) -> np.ndarray:
        x = x0

        gradient_x = gradient(x)
        hessian_x = hessian(x)
        Hx = np.linalg.inv(hessian_x)

        while True:
            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)

            # compute search direction
            p = -Hx @ gradient_x

            # backtracking to determine step size
            t = self.t0
            bound = self.alpha * t * np.inner(np.transpose(gradient_x), p)
            while f(x + t * p) > fx + t * bound:
                t *= self.beta

            x1 = x + t * p

            s = x1-x
            gradient_x1 = gradient(x1)
            y = gradient_x1 - gradient_x

            # compute next inverted hessian
            rho = 1 / (y @ s)
            I = np.eye(n)
            H1 = (I - rho * s @ y.T) @ Hx @ (I - rho * y @ s.T) + rho * s @ s

            # update
            Hx, x, gradient_x = H1, x1, gradient_x1

if __name__ == "__main__":
    bfgs = BFGS()
    runtime, steps, solution, cost = bfgs.report()
    # nm.plot_cost()
    # plt.show()
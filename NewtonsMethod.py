from Method import *
class NewtonsMethod(Method):
    def __str__(self):
        return "Newton's Method"

    def solve(self) -> np.ndarray:
        x = x0

        while True:
            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)
            # print(fx)

            gradient_x = gradient(x)
            inverse_hessian = np.linalg.inv(hessian(x))

            # newton step
            dx_nt = -inverse_hessian @ gradient_x

            # backtracking line search
            t = self.t0
            bound = self.alpha * t * gradient_x @ dx_nt
            while f(x + t * dx_nt) > fx + t * bound:
                t *= self.beta

            # update
            x = x + t * dx_nt

if __name__ == "__main__":
    nm = NewtonsMethod()
    runtime, steps, solution, cost = nm.report()
    # nm.plot_cost()
    # plt.show()
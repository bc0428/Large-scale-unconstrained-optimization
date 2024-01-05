from Method import *

class LBFGS(Method):
    m=5         # m most recent (s,y) pairs

    def __str__(self):
        return "L-BFGS"

    def solve(self) -> np.ndarray:
        x = x0

        gradient_x = gradient(x)
        hessian_x = hessian(gradient_x)
        Hx = np.linalg.inv(hessian_x)

        k=0
        queue_sy = []      # queue for (s,y) pairs
        queue_alpha = []   # queue for alpha (two loop recursion, not step size)

        while True:
            fx = f(x)
            if len(self.cost) and abs(fx - self.cost[-1]) <= self.tolerance:
                return x, fx
            self.cost.append(fx)



            # two loop recursion for inverse hessian approximation
            q = gradient_x
            for i in range(len(queue_sy)):
                s,y = queue_sy[i]
                rho = 1 / (y @ s)
                alpha = rho * (s @ q)
                if len(queue_sy) > len(queue_alpha):
                    queue_alpha.insert(0, alpha)
                q = q - alpha * y

            r = Hx @ q

            for i in range(len(queue_sy)-1, -1, -1):
                s, y = queue_sy[i]
                rho = 1 / (y @ s)
                beta = rho * (y @ r)
                r = r + s * (queue_alpha[i] - beta)

            p = -r





            # backtracking to determine step size
            t = self.t0
            bound = self.alpha * t * np.inner(np.transpose(gradient_x), p)
            while f(x + t * p) > fx + t * bound:
                t *= self.beta

            x1 = x + t * p

            # discard (s,y) pair from storage
            if k >= self.m:
                queue_sy.pop()
                queue_alpha.pop()


            s = x1-x
            gradient_x1 = gradient(x1)
            y = gradient_x1 - gradient_x

            # include most recent (s,y) pair
            queue_sy.insert(0, (s,y))

            # update
            x, gradient_x = x1, gradient_x1
            Hx = ((s @ y) / (y @ y)) * np.eye(n)
            k+=1

if __name__ == "__main__":
    lbfgs = LBFGS()
    runtime, steps, solution, cost = lbfgs.report()
    # nm.plot_cost()
    # plt.show()
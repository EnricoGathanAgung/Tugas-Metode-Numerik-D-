
# NIM: 21120123140127


import math

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def newton_no_numpy(x0, y0, tol=1e-6, max_iter=100):
    x, y = x0, y0
    print(f"{'Iter':<6}{'x':>14}{'y':>14}{'Δx':>12}{'Δy':>12}")
    print(f"{0:<6}{x:14.6f}{y:14.6f}{0.0:12.6f}{0.0:12.6f}")

    for k in range(1, max_iter + 1):
       
        F1 = f1(x, y)
        F2 = f2(x, y)

      
        J11 = 2*x + y
        J12 = x
        J21 = 3*y**2
        J22 = 1 + 6*x*y

      
        det = J11 * J22 - J12 * J21
        if abs(det) < 1e-12:
            print("Determinannya hampir nol. Iterasi dihentikan.")
            break

      
        dx = (-F1 * J22 + F2 * J12) / det
        dy = (-J11 * F2 + J21 * F1) / det


        x += dx
        y += dy

        print(f"{k:<6}{x:14.9f}{y:14.9f}{abs(dx):12.6e}{abs(dy):12.6e}")

        if abs(dx) < tol and abs(dy) < tol:
            print("\nSolusi konvergen.")
            return x, y, k, True

    print("\nIterasi maksimum tercapai.")
    return x, y, max_iter, False


if __name__ == "__main__":
    result = newton_no_numpy(1.5, 3.5)
    print("\nResult:", result)


# NIM: 21120123140127 (dua digit terakhir 27 -> NIMx mod4 = 3 -> g1B & g2B)
import math

def f1(x,y): return x*x + x*y - 10.0
def f2(x,y): return y + 3.0*x*y*y - 57.0

def g1B(x,y):
    disc = y*y + 40.0
    return (-y + math.sqrt(disc)) / 2.0

def g2B(x,y):
    if abs(x) < 1e-14:
        return y
    disc = 1.0 + 684.0 * x
    if disc < 0:
        return y
    return (-1.0 + math.sqrt(disc)) / (6.0 * x)

def jacobi(x0,y0,tol=1e-6,maxit=200):
    x, y = x0, y0
    print(f"{'Iter':<6}{'x':>14}{'y':>14}{'dx':>12}{'dy':>12}")
    print(f"{0:<6}{x:14.6f}{y:14.6f}{0.0:12.6f}{0.0:12.6f}")
    for k in range(1, maxit+1):
        x_new = g1B(x,y)
        y_new = g2B(x,y)
        dx = abs(x_new - x)
        dy = abs(y_new - y)
        print(f"{k:<6}{x_new:14.9f}{y_new:14.9f}{dx:12.6e}{dy:12.6e}")
        x, y = x_new, y_new
        if dx < tol and dy < tol:
            print("\nSolusi konvergen.")
            return x,y,k,True
    print("\nIterasi maksimum tercapai.")
    return x,y,maxit,False

if __name__ == '__main__':
    x0,y0 = 1.5,3.5
    sol = jacobi(x0,y0)
    print('\nResult:', sol)



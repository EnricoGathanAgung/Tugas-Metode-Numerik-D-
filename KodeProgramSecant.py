
# NIM: 21120123140127


import math

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def broyden_no_numpy(x0, y0, tol=1e-6, max_iter=100):
   
    x = x0
    y = y0

   
    B11, B12, B21, B22 = 1.0, 0.0, 0.0, 1.0

    print(f"{'Iter':<6}{'x':>14}{'y':>14}{'||F||':>14}")
    F1 = f1(x, y)
    F2 = f2(x, y)
    print(f"{0:<6}{x:14.6f}{y:14.6f}{max(abs(F1), abs(F2)):14.6e}")

    for k in range(1, max_iter + 1):
       
        detB = B11 * B22 - B12 * B21
        if abs(detB) < 1e-12:
            print("Error: Determinan B mendekati nol.")
            break

        s1 = (-F1 * B22 + F2 * B12) / detB
        s2 = (-B11 * F2 + B21 * F1) / detB

       
        x_new = x + s1
        y_new = y + s2

       
        F1_new = f1(x_new, y_new)
        F2_new = f2(x_new, y_new)

    
        y1 = F1_new - F1
        y2 = F2_new - F2

        denom = s1**2 + s2**2
        if denom == 0:
            break

      
        B11 += ((y1 - (B11 * s1 + B12 * s2)) * s1) / denom
        B12 += ((y1 - (B11 * s1 + B12 * s2)) * s2) / denom
        B21 += ((y2 - (B21 * s1 + B22 * s2)) * s1) / denom
        B22 += ((y2 - (B21 * s1 + B22 * s2)) * s2) / denom

      
        x, y = x_new, y_new
        F1, F2 = F1_new, F2_new

        normF = max(abs(F1), abs(F2))
        print(f"{k:<6}{x:14.9f}{y:14.9f}{normF:14.6e}")

        if normF < tol:
            print("\nSolusi konvergen.")
            return x, y, k, True

    print("\nIterasi maksimum tercapai.")
    return x, y, max_iter, False


if __name__ == "__main__":
    result = broyden_no_numpy(1.5, 3.5)
    print("\nResult:", result)

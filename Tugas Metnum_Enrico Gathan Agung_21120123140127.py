import math
import numpy as np

# --- Konfigurasi ---
TOLERANCE = 1e-6
MAX_ITERATIONS = 100
INITIAL_X = 1.5
INITIAL_Y = 3.5

# Fungsi Iterasi: g1B dan g2B
def g1(x, y):
    if y == 0:
        raise ZeroDivisionError("Pembagian dengan nol pada g1.")
    return (10 - x**2) / y

def g2(x, y):
    return 57 - 3 * x * y**2

def solve_jacobi(initial_x, initial_y, tolerance, max_iterations):
    print("--- IT - JACOBI (g1B: x=(10-x^2)/y, g2B: y=57-3xy^2) ---")
    print(f"{'Iterasi':<8} {'x':<15} {'y':<15} {'Galat Maks':<15}")
    
    x, y = initial_x, initial_y
    print(f"{0:<8} {x:<15.6f} {y:<15.6f} {0.0:<15.6f}")

    for i in range(1, max_iterations + 1):
        prev_x, prev_y = x, y
        
        try:
            # Perhitungan Jacobi
            next_x = g1(prev_x, prev_y)
            next_y = g2(prev_x, prev_y)
        except (ZeroDivisionError, OverflowError):
            print("\nError: Iterasi gagal (Divergen).")
            break

        change_x = abs(next_x - prev_x)
        change_y = abs(next_y - prev_y)
        max_error = max(change_x, change_y)
        
        x, y = next_x, next_y

        print(f"{i:<8} {x:<15.6f} {y:<15.6f} {max_error:<15.6f}")

        if max_error < tolerance:
            print("\nSolusi konvergen.")
            return x, y
        
        if max_error > 1e10: 
            print("\nDivergen: Galat meledak.")
            break

    print("\nIterasi maksimum tercapai atau Divergen.")
    return x, y

if __name__ == "__main__":
    solve_jacobi(INITIAL_X, INITIAL_Y, TOLERANCE, MAX_ITERATIONS)
import numpy as np
import math

def function_tabulation(a, b, h):
    x_values = np.arange(a, b + h, h)
    result = []
    
    for x in x_values:
        if x < 4:
            f = math.log((x + math.sin(x)), 3)
        elif 4 <= x < 5:
            f = math.log10(math.exp(x) + 4)
        elif x >= 5:
            f = math.log(math.log10(x))
        result.append((x, f))
    
    return result

a = 3
b = 6
h = 0.2

result = function_tabulation(a, b, h)

for x, f in result:
    print(f"x = {x:.2f}, f(x) = {f}")

def tabulate_series_custom(a, b, h, d):
    results = []
    x = a
    while x <= b:
        sum_series = 0
        n = 0
        term = float('inf')
        
        while abs(term) > d:
            term = (-1)**n * x**(2*n + 3) / ((2*n + 1)*(2*n + 3))
            sum_series += term
            n += 1
        
        results.append((x, sum_series))
        x += h
    
    return results

a = 0
b = 1
h = 0.1
d = 0.0001

tabulated_values = tabulate_series_custom(a, b, h, d)

print()
for x, value in tabulated_values:
    print(f"x = {x:.2f}, f(x) ≈ {value:.5f}")
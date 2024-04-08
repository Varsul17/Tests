from Simpson_method import simpsons_rule
import math

def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


if __name__ == '__main__':
    print("Part 1")
    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [3.5095, 3.6984, 3.9043, 4.1293, 4.3756]
    x_interpolate = 1.55  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print("Interpolated value at x =", x_interpolate, "is y =", y_interpolate)
    x_interpolate = 1.35  # The x-value where you want to interpolate
    y_interpolate = lagrange_interpolation(x_data, y_data, x_interpolate)
    print("Interpolated value at x =", x_interpolate, "is y =", y_interpolate,"\n\n")

    f = lambda x: (math.sin(x ** 2 + 5*x + 6)) / (2 * math.e ** (-x))
    n = 70
    a = 3.8
    b = 4.2

    print(f"Division into n={n} sections ")
    integral1 = simpsons_rule(f, a, b, n)
    print(f"Numerical Integration of definite integral in range [{a},{b}] is {integral1}")

    print(f"Division into n={n + 20} sections ")
    integral2 = simpsons_rule(f, a, b, n + 20)
    print(f"Numerical Integration of definite integral in range [{a},{b}] is {integral2}")



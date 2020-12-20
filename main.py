# Script for least squares method (IMO, theorem 5.11)
# x_0 optimal solution to min|b-Ax|^2, if solution to (A^TA)x = A^Tb
import math
import numpy as np


points = np.array([[1, 2], [2, 2], [3, 1], [4, 1]])
points2 = np.array([[-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2]])
points3 = np.array([[0, 2], [0, 3], [2, 0], [3, 1]])


def build_A_matrix(points, degree):
    rows = points.shape[0]
    A = np.zeros(shape=(rows, degree + 1))
    return A


def build_b_matrix(points):
    rows = points.shape[0]
    b = np.zeros(shape=(rows, 1))
    for i in range(rows):
        b[i] = points[i, 1]
    return b


def calculations(A, b):
    print("A matrix")
    print(A)
    print()

    print("b matrix")
    print(b)
    print()

    A_tranposed = A.transpose()
    print("A^T")
    print(A_tranposed)
    print()

    A_transposed_A = A_tranposed.dot(A)
    print("A^TA")
    print(A_transposed_A)
    print()

    A_tranposed_b = A_tranposed.dot(b)
    print("A^Tb")
    print(A_tranposed_b)
    print()

    A_transposed_A_inverse = np.linalg.inv(A_transposed_A)
    print("A^TA^-1")
    print(A_transposed_A_inverse)
    print()

    # solution = A_tranposed_b.dot(A_transposed_A_inverse)
    solution = A_transposed_A_inverse.dot(A_tranposed_b)
    print("Solution")
    print(solution)
    print()
    return solution


def least_squares_linear(points):
    A = build_A_matrix(points, 1)
    b = build_b_matrix(points)

    # Inserting values into A
    for i in range(A.shape[0]):
        A[i, 0] = points[i, 0]
        A[i, 1] = 1

    # All calculations performed on the matrices
    calculations(A, b)


def least_squares_quadratic(points):
    A = build_A_matrix(points, 2)
    b = build_b_matrix(points)

    # Inserting values into A
    for i in range(A.shape[0]):
        xi = points[i, 0]
        A[i, 0] = xi**2
        A[i, 1] = xi
        A[i, 2] = 1

    # All calculations performed on the matrices
    calculations(A, b)


def least_squares_circle(points):
    A = build_A_matrix(points, 2)
    b = build_b_matrix(points)

    # Inserting values into A
    for i in range(A.shape[0]):
        A[i, 0] = 2 * points[i, 0]
        A[i, 1] = 2 * points[i, 1]
        A[i, 2] = 1

    # Inserting values into b
    for i in range(A.shape[0]):
        b[i] = points[i, 0]**2 + points[i, 1]**2

    # All calculations performed on the matrices
    solution = calculations(A, b)

    # Transforms the values for a, b and c into radius r
    a = solution[0]
    b = solution[1]
    c = solution[2]
    radius = math.sqrt(c + a**2 + b**2)

    print("a")
    print(a)
    print()

    print("b")
    print(b)
    print()

    print("Radius")
    print(radius)


least_squares_circle(points3)
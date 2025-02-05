import numpy as np

def ArrayChallenge(arr):
    """
    Calculates the updated values of a and b using gradient descent.

    Args:
        arr: A list of four numbers representing the input array.

    Returns:
        A tuple containing the updated values of a and b.
    """

    x, y, a, b = arr

    # Calculate the predicted value of y
    y_pred = 1.0 / (1.0 + np.exp(-(a * x + b)))

    # Calculate the gradients
    da = (y_pred - y) * x
    db = y_pred - y

    # Update a and b using gradient descent with learning rate 1
    a_new = a - da
    b_new = b - db

    return a_new, b_new

# Test cases
result1 = ArrayChallenge([1, 1, 1, 1])

print("{:.3f}:{:.3f}".format(result1[0], result1[1]))
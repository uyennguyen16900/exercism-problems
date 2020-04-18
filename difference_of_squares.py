# Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

def difference_of_squares(n):
    # if n % 2 == 1:
    #     median = (n + 1) / 2
    #     num_pairs = (n - 1) / 2
    # else:
    #     median = 0
    #      num_pairs = n / 2
    #
    # square_of_sum = (n + 1) * num_pairs + median

    square_of_sum = (n * (n + 1) / 2) ** 2
    sum_of_square = (n * (n + 1) * (2 * n + 1)) / 6

    difference = abs(square_of_sum - sum_of_square)
    return difference

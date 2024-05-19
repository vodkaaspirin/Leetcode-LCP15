def calculate_cross_product(A, B, C):
    # Calculate the cross product of vectors AB and BC
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

def is_turn(A, B, C, direction):
    cross_product = calculate_cross_product(A, B, C)
    if direction == 'L':
        return cross_product > 0
    else:  # direction == 'R'
        return cross_product < 0

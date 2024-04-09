import numpy as np

def hungarian_algorithm(cost_matrix):
    num_rows, num_cols = cost_matrix.shape
    mask_matrix = np.zeros_like(cost_matrix, dtype=bool)
    row_covered = np.zeros(num_rows, dtype=bool)
    col_covered = np.zeros(num_cols, dtype=bool)

    def _step1(cost_matrix):
        min_val = np.min(cost_matrix)
        cost_matrix -= min_val

    def _step2(cost_matrix, mask_matrix, row_covered, col_covered):
        for i in range(num_rows):
            for j in range(num_cols):
                if cost_matrix[i, j] == 0 and not row_covered[i] and not col_covered[j]:
                    mask_matrix[i, j] = True
                    row_covered[i] = True
                    col_covered[j] = True

    def _step3(cost_matrix, mask_matrix, row_covered, col_covered):
        cols_covered = np.any(mask_matrix, axis=0)
        while not np.all(cols_covered):
            uncovered_zeros = np.logical_and(~cols_covered, cost_matrix == 0)
            row_indices, col_indices = np.where(uncovered_zeros)
            if row_indices.size > 0: # Check if row_indices is not empty
                row_index = row_indices[0]
                col_index = col_indices[0]
                mask_matrix[row_index, col_index] = True
                cols_covered[col_index] = True
                row_covered[row_index] = True
                col_covered[col_index] = True
            else:
                break # Exit the loop if no uncovered zeros are found
            cols_covered = np.any(mask_matrix, axis=0)

    def _step4(cost_matrix, mask_matrix, row_covered, col_covered):
        min_uncovered_val = np.min(cost_matrix[~row_covered, :][:, ~col_covered])
        cost_matrix[~row_covered, ~col_covered] -= min_uncovered_val
        row_zeros = np.zeros(num_rows, dtype=bool)
        col_zeros = np.zeros(num_cols, dtype=bool)
        row_indices, col_indices = np.where(cost_matrix == 0)
        row_zeros[row_indices] = True
        col_zeros[col_indices] = True
        uncovered_zeros = np.logical_and(~row_covered, ~col_zeros)
        if np.any(uncovered_zeros): # Ensure there are uncovered zeros before proceeding
            row_indices, col_indices = np.where(uncovered_zeros)
            if row_indices.size > 0: # Check if row_indices is not empty
                row_index = row_indices[0]
                col_index = col_indices[0]
                mask_matrix[row_index, col_index] = True
                cols_covered = np.any(mask_matrix, axis=0)
                while np.any(cols_covered):
                    col_index = np.where(cols_covered)[0][0]
                    row_index = np.where(mask_matrix[:, col_index])[0][0]
                    mask_matrix[row_index, col_index] = False
                    cols_covered = np.any(mask_matrix, axis=0)

    def _step5(cost_matrix, mask_matrix, row_covered, col_covered):
        min_uncovered_val = np.min(cost_matrix[~row_covered, :][:, ~col_covered])
        cost_matrix[row_covered, col_covered] += min_uncovered_val
        cost_matrix[~row_covered, ~col_covered] -= min_uncovered_val

    _step1(cost_matrix)
    _step2(cost_matrix, mask_matrix, row_covered, col_covered)
    _step3(cost_matrix, mask_matrix, row_covered, col_covered)
    _step4(cost_matrix, mask_matrix, row_covered, col_covered)
    _step5(cost_matrix, mask_matrix, row_covered, col_covered)

    return np.argwhere(mask_matrix)


def get_cost_matrix_from_user():
    num_rows = int(input("Enter the number of workers: "))
    num_cols = int(input("Enter the number of tasks: "))
    print("Enter the cost matrix (separate elements by space):")
    cost_matrix = []
    for i in range(num_rows):
        row = list(map(int, input().split()))
        if len(row) != num_cols:
            raise ValueError("Invalid input. Number of elements in each row must match the number of tasks.")
        cost_matrix.append(row)
    return np.array(cost_matrix)

# Example usage:
cost_matrix = get_cost_matrix_from_user()
assignments = hungarian_algorithm(cost_matrix)
print("Optimal assignments:")
for assignment in assignments:
    print(f"Worker {assignment[0]} is assigned to Task {assignment[1]} with cost {cost_matrix[assignment[0], assignment[1]]}.")

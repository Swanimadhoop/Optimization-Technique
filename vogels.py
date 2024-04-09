import numpy as np

def vogel_approximation_method(supply, demand, cost):
    m = len(supply)  # Number of sources
    n = len(demand)  # Number of destinations

    # Create copies of input lists to avoid modifying the original data
    sup = np.copy(supply)
    dem = np.copy(demand)
    cost_mat = np.copy(cost)

    # Initialize the basic feasible solution matrix and total cost
    allocation = np.zeros((m, n), dtype=int)
    total_cost = 0

    # Perform VAM iterations
    while np.sum(sup) > 0 and np.sum(dem) > 0:
        # Find the row/column with the maximum penalty
        row_pen = np.min(cost_mat, axis=1) - np.min(cost_mat)
        col_pen = np.min(cost_mat, axis=0) - np.min(cost_mat, axis=0)
        max_pen = max(np.max(row_pen), np.max(col_pen))

        # Allocate as much as possible to the cell with the maximum penalty
        row_idx, col_idx = np.unravel_index(np.argmin(cost_mat), cost_mat.shape)
        quantity = min(sup[row_idx], dem[col_idx])
        allocation[row_idx, col_idx] = quantity
        total_cost += cost_mat[row_idx, col_idx] * quantity

        sup[row_idx] -= quantity
        dem[col_idx] -= quantity

        # Remove the allocated row or column if supply/demand is zero
        if sup[row_idx] == 0:
            cost_mat = np.delete(cost_mat, row_idx, axis=0)
            sup = np.delete(sup, row_idx)
        if dem[col_idx] == 0:
            cost_mat = np.delete(cost_mat, col_idx, axis=1)
            dem = np.delete(dem, col_idx)

    return allocation, total_cost

def modi_method(costs, allocation):
    supply, demand = allocation.shape

    # Calculate initial potentials
    u = np.zeros(supply)
    v = np.zeros(demand)

    # Iterate until optimality is reached
    while True:
        # Calculate reduced costs
        reduced_costs = costs - u.reshape(-1, 1) - v

        # Find the entering variable
        min_reduced_cost = np.min(reduced_costs)
        if min_reduced_cost >= 0:
            break  # Optimality reached

        entering_index = np.unravel_index(np.argmin(reduced_costs), reduced_costs.shape)

        # Perform cycle to find leaving variable
        cycle = [(entering_index[0], entering_index[1])]
        while True:
            i, j = cycle[-1]
            if (i, j) in cycle[:-1]:
                break
            else:
                row_indices = np.where(allocation[i] > 0)[0]
                col_indices = np.where(allocation[:, j] > 0)[0]
                next_indices = [(r, j) for r in row_indices] + [(i, c) for c in col_indices]
                next_index = next_indices[1] if next_indices[0] == cycle[-2] else next_indices[0]
                cycle.append(next_index)

        # Compute theta
        thetas = [allocation[i][j] / reduced_costs[i][j] for i, j in cycle[1::2]]
        theta = min(thetas)

        # Update potentials
        non_basic_indices = [(i, j) for i in range(supply) for j in range(demand) if (i, j) not in cycle[::2]]
        for i, j in cycle[::2]:
            u[i] += theta
            v[j] -= theta
        for i, j in non_basic_indices:
            reduced_costs[i][j] -= theta

        # Update allocation
        allocation[cycle[0]] = theta
        for i, j in cycle[1::2]:
            allocation[i][j] -= theta

    return allocation

# Example usage
supply = [300, 400, 500]
demand = [250, 350, 400, 200]
cost_matrix = np.array([[3, 1, 7, 4],
                        [2, 6, 5, 9],
                        [8, 3, 3, 2]])

# Obtain initial solution using VAM
initial_solution, initial_cost = vogel_approximation_method(supply, demand, cost_matrix)

# Apply MODI method to obtain optimal solution
optimal_solution = modi_method(cost_matrix, initial_solution)

# Calculate the cost of the optimal solution
optimal_cost = np.sum(optimal_solution * cost_matrix)

print("Initial Basic Feasible Solution (Vogel's Approximation Method):")
print(initial_solution)
print("Total Cost:", initial_cost)
print("\nOptimal Solution (MODI Method):")
print(optimal_solution)
print("Total Cost:", optimal_cost)

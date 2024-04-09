import numpy as np

def least_cost_cell(cost_matrix, supply, demand, m, n):
    # m, n = cost_matrix.shape
    allocation = np.zeros((m, n))
    available_supply = np.copy(supply)
    available_demand = demand.copy()

    while np.sum(available_supply)>0 and np.sum(available_demand)>0:
        min_cost = np.inf
        min_i, min_j = -1, -1
        for i in range(m):
            for j in range(n):
                if allocation[i, j] == 0 and available_supply[i] > 0 and available_demand[j] > 0 and cost_matrix[i, j] < min_cost:
                    min_cost = cost_matrix[i, j]
                    min_i, min_j = i, j

        if min_i == -1 and min_j == -1:
            break

        quantity = min(available_supply[min_i], available_demand[min_j])
        allocation[min_i, min_j] = quantity
        available_supply[min_i] -= quantity
        available_demand[min_j] -= quantity

    return allocation

def calculate_total_cost(allocation, cost_matrix):
    total_cost = np.sum(allocation * cost_matrix)
    return total_cost

# Example problem
m=3
n=3
cost_matrix = np.zeros((m,n))
for i in range(m):
  for j in range(n):
    cost_matrix[i][j]=int(input("Enter cost matrix : "))

supply = np.array([200, 300, 500])
demand = np.array([200, 400, 400])

# Apply the Least Cost Cell Method
allocation = least_cost_cell(cost_matrix, supply, demand, m, n)
print("Allocation Matrix:\n", allocation)

# Calculate and print the minimum cost
min_cost = calculate_total_cost(allocation, cost_matrix)
print("\n\nMinimum Cost:", min_cost)
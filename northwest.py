import numpy as np

def northwest_corner(cost_matrix, supply, demand, m, n):
    allocation = np.zeros((m, n))
    available_supply = np.copy(supply)
    available_demand = np.copy(demand)

    for i in range(m):
        for j in range(n):
            quantity = min(available_supply[i], available_demand[j])
            allocation[i,j] = quantity
            available_supply[i] -= quantity
            available_demand[j] -= quantity

            if available_supply[i] == 0 and np.sum(available_demand) == 0:
                break

    return allocation

def calculate_total_cost(allocation, cost_matrix):
    total_cost = np.sum(allocation * cost_matrix)
    return total_cost

# Example problem
m = 3
n = 3
cost_matrix = np.zeros((m, n))
for i in range(m):
    for j in range(n):
        cost_matrix[i][j] = int(input(f"Enter cost matrix for ({i}, {j}): "))

supply = np.array([200, 300, 500])
demand = np.array([200, 400, 400])

# Apply the Northwest Corner Method
allocation = northwest_corner(cost_matrix, supply, demand, m, n)
print("Allocation Matrix:\n", allocation)

# Calculate and print the total cost
total_cost = calculate_total_cost(allocation, cost_matrix)
print("\n\nTotal Cost:", total_cost)



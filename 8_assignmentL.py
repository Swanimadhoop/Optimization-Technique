import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment_problem(cost_matrix):

    worker_indices, task_indices = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[worker_indices, task_indices].sum()
    return worker_indices, task_indices, total_cost

# Example usage

cost_matrix=np.zeros((3,3))
for i in range(3):
  for j in range(3):
    cost_matrix[i,j]=int(input("Enter the value : "))
# cost_matrix = np.array([[10, 20, 30],
#                         [40, 50, 60],
#                         [70, 80, 90]])

worker_indices, task_indices, total_cost = solve_assignment_problem(cost_matrix)

print("Worker Indices:", worker_indices)
print("Task Indices:", task_indices)
print("Total Cost:", total_cost)
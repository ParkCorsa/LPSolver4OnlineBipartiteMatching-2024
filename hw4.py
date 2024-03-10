import matplotlib.pyplot as plt
import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model()
model.setParam('Threads', 16)

# Define the decision variables
n = 3200  # Number of variables
step = 1.0/n
g = [model.addVar(name=f"g{i}", lb=0, ub=1) for i in range(n+1)]
gs = [model.addVar(name=f"gs{i}", lb=0, ub=1) for i in range(n+1)] #prefix sum
r = model.addVar(name='r', lb=0)

# Set the objective function
model.setObjective(r, GRB.MAXIMIZE)

# Add constraints
for i in range(n):
    model.addConstr(g[i] <= g[i+1], f"gc{i}")
    
for i in range(n):
    model.addConstr(gs[i+1] == gs[i] + g[i] * step, f"gsc{i+1}")
model.addConstr(gs[0] == 0, f"gsc{0}")

for i in range(n):
    for j in range(n):
        model.addConstr(r <= gs[i] + gs[j] + (1-g[i+1]) * (1-(j+1)*step), f"c{i}{j}")

model.addConstr(r <= gs[n], "c")

# Optimize the model
model.optimize()

# Retrieve the solution
if model.status == GRB.OPTIMAL:
    print("Optimal solution found!")
    print("Objective value: ", model.objVal)
    # g = model.getAttr('x', model.getVars())
    g_values = [var.x for var in g]
    x = range(len(g_values))
    plt.plot(x, g_values)
    plt.xlabel('x-axis')
    plt.ylabel('g')
    plt.title('Plot of g[]')
    plt.show()
else:
    print("No solution found.")

# Dispose of the model
model.dispose()
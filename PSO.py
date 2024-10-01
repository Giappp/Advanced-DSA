import random


def f(variables):
    x, y, z, q = variables
    return abs(3 * round(x) + 2 * round(y) + round(z) + round(q) - 34)


n_particles = 10
num_iterations = 100
c1 = c2 = 1.5
w = 0.7

lower_bound = 1
upper_bound = 20

# Khoi tao swarm
swarms = [[random.uniform(lower_bound, upper_bound) for _ in range(4)] for _ in range(n_particles)]
# Khoi tao toc do cua particle
velocities = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(n_particles)]
personal_best_positions = swarms[:]
personal_best_values = [f(swarm) for swarm in swarms]

global_best_position = personal_best_positions[personal_best_values.index(min(personal_best_values))]
# Chay thuat toan PSO
for iteration in range(num_iterations):
    for i in range(n_particles):
        for j in range(4):
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            # Tinh toan toc do o particle thu i
            velocities[i][j] = ((w * velocities[i][j]) +
                                c1 * r1 * (personal_best_positions[i][j] - swarms[i][j]) +
                                c2 * r2 * (global_best_position[j] - swarms[i][j]))
        # Di chuyen cac particle den vi tri moi
        for j in range(4):
            swarms[i][j] += velocities[i][j]
            swarms[i][j] = max(min(swarms[i][j], upper_bound), lower_bound)

    fitness_value = f(swarms[i])

    if fitness_value < personal_best_values[i]:
        personal_best_positions[i] = swarms[i][:]
        personal_best_values[i] = fitness_value

    current_global_best_value = min(personal_best_values)
    # Cap nhat gia tri tot nhat neu gia tri hien tai tot hon gia tri toan cuc
    if current_global_best_value < f(global_best_position):
        global_best_position = personal_best_positions[personal_best_values.index(current_global_best_value)]
    if f(global_best_position) == 0:
        break

# Output the best solution found
print(
    f"Best solution found: x = {global_best_position[0].__round__()}, y = {global_best_position[1].__round__()}, z = {global_best_position[2].__round__()}, q = {global_best_position[3].__round__()}")
print(f"Objective function value: {f(global_best_position)}")

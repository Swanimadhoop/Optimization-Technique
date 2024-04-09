import random
numofelems =   15

items = random.sample(range(1,16),numofelems)


target_sum = random.randint(1, sum(items))

def generate_population(size):
    population = []
    for _ in range(size):
        chromosome = [random.choice([0,   1]) for _ in range(len(items))]
        population.append(chromosome)
    return population

def calculate_fitness(chromosome):
    subset_sum = sum(item * bit for item, bit in zip(items, chromosome))
    if subset_sum == target_sum:
        return  1  
    elif subset_sum > target_sum:
        return  0  
    else:
        return subset_sum / target_sum  


def select_chromosomes(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]
    parent1 = random.choices(population, weights=fitness_values, k=1)[0]
    parent2 = random.choices(population, weights=fitness_values, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(items)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(items)-1)
    chromosome[mutation_point] =   1 - chromosome[mutation_point]
    return chromosome

def get_best(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    return population[max_index]

population_size =   10
mutation_probability =   0.2
generations =  200000

population = generate_population(population_size)
for _ in range(generations):
    parent1, parent2 = select_chromosomes(population)
    child1, child2 = crossover(parent1, parent2)
    if random.uniform(0,  1) < mutation_probability:
        child1 = mutate(child1)
    if random.uniform(0,  1) < mutation_probability:
        child2 = mutate(child2)
    
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    min_fitness_indexes = sorted(range(len(fitness_values)), key=lambda x: fitness_values[x])[:2]
    population[min_fitness_indexes[0]] = child1
    population[min_fitness_indexes[1]] = child2


best = get_best(population)

subset_sum = sum(item * bit for item, bit in zip(items, best))

print("Items matrix:", items)
print("Target sum:", target_sum)
print("Elements that give the target sum:", [item for item, bit in zip(items, best) if bit ==  1])
print("Sum = ",sum([item for item, bit in zip(items, best) if bit ==  1]))
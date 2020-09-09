# CREATED BY SHADMAN RAKIB
# onikuspedu.github.io

import random, string
def generate(len):
    letters = string.printable
    return ''.join(random.choice(letters) for i in range(len))

def init_pop(pop_size, len):
    population = []
    for person in range(pop_size):
        population.append(generate(len))
    return population

def score(person, goal):
    score = 0
    for i in range(len(person)):
        if person[i] == goal[i]:
            score += 1
    return(score)

def fitness(population, goal):
    fitness = []
    for person in population:
        fitness.append(score(person, goal))
    return fitness

def select(population, fitness):
    sorted_pop = [x for _,x in sorted(zip(fitness,population))]
    return sorted_pop[::-1][0], sorted_pop[::-1][1]

def mate(parent1, parent2, pc):
    child = list(parent1)
    for i in range(len(parent1)):
        if random.random() <= pc:
            child[i] = list(parent2)[i]
    return ''.join(child)

def crossover(parent1, parent2, pop_size, pc):
    population = []
    for person in range(pop_size):
        population.append(mate(parent1, parent2, pc))
    return population

def mutate(population, pm):
    pop = []
    letters = string.printable
    for person in population:
        for index in range(len(person)):
            if random.random() <= pm:
                if len(person) != 0:
                    person = person[:index] + random.choice(letters) + person[index + 1:]
                else:
                    person = random.choice(letters)

        pop.append(person)
    return pop

def genetic(goal, pop_size, pc, pm):
    population = init_pop(pop_size, len(goal))
    iteration = 0
    reached = False
    length = len(goal)
    best = ''.join(' ' for i in range(length))
    while not reached:
        iteration += 1
        fit = fitness(population, goal)
        parent1, parent2 = select(population, fit)
        print('Iteration:', iteration, '\n==========================\n',parent1)
        if score(parent1, goal) > score(best, goal):
            best = parent1
            if score(parent2, goal) < score(best, goal):
                parent2 = best
        else:
            parent2 = parent1
            parent1 = best
        if parent1 == goal: 
            reached = True
        else:
            population = mutate(crossover(parent1, parent2, pop_size, pc), pm)
    return("Best:", best)

goal = input('Desired String (Characters can be any letters, digits, and punctuation):')
pop_size = input('Population Size (Larger populations are better):')
probability_mutation = input('Probability Mutation (Lower values like 0.05 or 0.1 work best):')

print(genetic(goal, int(pop_size), 0.5, float(probability_mutation)))
import numpy as np
import math

# Griewank Function
def Griewank(x):
    function = 1
    s = 1

    for i in range(len(x)):
        function += x[i] ** 2 / 4000
        s *= math.cos(x[i] / (i + 1) ** 0.5)

    function -= s
    return function

# rastrigin function
def fitness_rastrigin(position):
  fitnessVal = 0.0
  for i in range(len(position)):
    xi = position[i]
    fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
  return fitnessVal

# check if a point is within the bounds of the search
def in_bounds(point, bounds):
    # enumerate all dimensions of the point
    for d in range(len(bounds)):
        # check if out of bounds for this dimension
        if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
            return False
    return True

"""# (Mu, Lambda)"""

# evolution strategy (mu, lambda) algorithm
def es_comma(objective, bounds, n_iter, step_size, mu, lam):
    global bestss
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = list()
    for _ in range(lam):
        candidate = None
        while candidate is None or not in_bounds(candidate, bounds):
            candidate = bounds[:, 0] + np.random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        population.append(candidate)
    # perform the search
    for epoch in range(n_iter):
        # evaluate fitness for the population
        scores = [objective(c) for c in population]
        bestss.append(scores[epoch])
        # rank scores in ascending order
        ranks = np.argsort(np.argsort(scores))
        # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] < mu]
        # create children from parents
        children = list()
        for i in selected:
            # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                best, best_eval = population[i], scores[i]
#                 print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
            # create children for parent
            for _ in range(n_children):
                child = None
                while child is None or not in_bounds(child, bounds):
                    child = population[i] + np.random.rand(len(bounds)) * step_size
                children.append(child)
        # replace population with children
        population = children
    print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
    return [best, best_eval]

def es_plus(objective, bounds, n_iter, step_size, mu, lam):
    min = 0
    global bestss2
    best, best_eval = None, 1e+10
    # calculate the number of children per parent
    n_children = int(lam / mu)
    # initial population
    population = list()
    for _ in range(lam):
        candidate = None
        while candidate is None or not in_bounds(candidate, bounds):
            candidate = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
        population.append(candidate)
    # perform the search
    for epoch in range(n_iter):
        # evaluate fitness for the population
        scores = [objective(c) for c in population]
        bestss2.append(scores[epoch])
        # rank scores in ascending order
        ranks = argsort(argsort(scores))
        # select the indexes for the top mu ranked solutions
        selected = [i for i,_ in enumerate(ranks) if ranks[i] < mu]
        # create children from parents
        children = list()
        for i in selected:
            # check if this parent is the best solution ever seen
            if scores[i] < best_eval:
                best, best_eval = population[i], scores[i]
            # keep the parent
            children.append(population[i])
            # create children for parent
            for _ in range(n_children):
                child = None
                while child is None or not in_bounds(child, bounds):
                    child = population[i] + randn(len(bounds)) * step_size
                children.append(child)
        # replace population with children
        population = children
    print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
    return [best, best_eval]
    
if __name__=='__main__':

    np.random.seed(1)
    bounds = np.asarray([[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],\
    [-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],\
    [-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],\
    [-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0]])
    n_iter = 200
    step_size = 0.15
    mu = 10
    lam= 100

    bestss = []
    best, score = es_comma(Griewank, bounds, n_iter, step_size, mu, lam)
    
    np.random.seed(1)
    bounds = np.asarray([[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0],\
    [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],\
    [-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0]])
    n_iter = 100
    step_size = 0.3
    mu = 20
    lam = 100
    bestss2 = []
    # mu plus lamba
    best, score = es_plus(Griewank, bounds, n_iter, step_size, mu, lam)
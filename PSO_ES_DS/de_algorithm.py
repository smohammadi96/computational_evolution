import numpy as np
import math
import matplotlib.pyplot as plt
 
 
# define objective function (Rastrigin)
def obj(position):
  fitnessVal = 0.0
  for i in range(len(position)):
    xi = position[i]
    fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
  return fitnessVal
 
 
# define mutation operation
def mutation(x, F):
    return x[0] + F * (x[1] - x[2])
 
 
# define boundary check operation
def check_bounds(mutated, bounds):
    mutated_bound = [np.clip(mutated[i], bounds[i, 0], bounds[i, 1]) for i in range(len(bounds))]
    return mutated_bound
 
 
# define crossover operation
def crossover(mutated, target, dims, cr):
    # generate a uniform random value for every dimension
    p = np.random.rand(dims)
    # generate trial vector by binomial crossover
    trial = [mutated[i] if p[i] < cr else target[i] for i in range(dims)]
    return trial

 
def differential_evolution(pop_size, bounds, iter, F, cr):
    global bestss
    # initialise population of candidate solutions randomly within the specified bounds
    pop = bounds[:, 0] + (np.random.rand(pop_size, len(bounds)) * (bounds[:, 1] - bounds[:, 0]))
    # evaluate initial population of candidate solutions
    obj_all = [obj(ind) for ind in pop]
    # find the best performing vector of initial population
    best_vector = pop[np.argmin(obj_all)]
    best_obj = np.min(obj_all)
    prev_obj = best_obj
    # run iterations of the algorithm
    for i in range(iter):
        # iterate over all candidate solutions
        for j in range(pop_size):
            # choose three candidates, a, b and c, that are not the current one
            candidates = [candidate for candidate in range(pop_size) if candidate != j]
            a, b, c = pop[np.random.choice(candidates, 3, replace=False)]
            # perform mutation
            mutated = mutation([a, b, c], F)
            # check that lower and upper bounds are retained after mutation
            mutated = check_bounds(mutated, bounds)
            # perform crossover
            trial = crossover(mutated, pop[j], len(bounds), cr)
            # compute objective function value for target vector
            obj_target = obj(pop[j])
            # compute objective function value for trial vector
            obj_trial = obj(trial)
            # perform selection
            if obj_trial < obj_target:
                # replace the target vector with the trial vector
                pop[j] = trial
                # store the new objective function value
                obj_all[j] = obj_trial
        # find the best performing vector at each iteration
        best_obj = np.min(obj_all)
        # store the lowest objective function value
        if best_obj < prev_obj:
            best_vector = pop[np.argmin(obj_all)]
            prev_obj = best_obj
        bestss.append(best_obj)
    return [best_vector, best_obj]
 
if __name__=='__main__':
    # define population size
    pop_size = 10
    # define lower and upper bounds for every dimension
    bounds = np.asarray([[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0],[-5.0, 5.0], [-5.0, 5.0]])
    # define number of iterations
    
    iter = 100
    F = 0
    cross_over = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    
    best_solution = []
    best_cr = []
    best_F = []
    #result = []
    for F in cross_over:
        print(F)
        result = []
        cr_value = []
        for cr in cross_over:
            print(cr)
            bestss = []
            solution = differential_evolution(pop_size, bounds, iter, F, cr)
            result.append(solution[1])
            cr_value.append([cr, F])
            cr = cr + 0.1
        min_result_index = result.index(min(result))
        best_solution.append(min(result))
        best_cr.append(cr_value[min_result_index])   
        F = F + 1
        
    list_1 = []
    for i in range(len(result)):
        list_1.append(i)
    
    cr_list = []
    F_list = []
    for t in best_cr:
        cr_list.append(t[0])
        F_list.append(t[1])
   
    #plt.title('DE')
    #plt.plot(list_1, result, color="blue")
    #plt.savefig('DE.png')
    #plt.show()
    ax = plt.axes(projection='3d')
    ax.plot3D(cr_list, F_list, best_solution, 'gray')
    plt.show()
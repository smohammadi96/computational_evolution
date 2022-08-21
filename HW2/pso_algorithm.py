import random
import math    
import copy  
import sys    
import matplotlib.pyplot as plt
import numpy as np
import pyswarms as ps
from matplotlib import cm 
import argparse
from mpl_toolkits.mplot3d import Axes3D 
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Designer
from pyswarms.utils.plotters.formatters import Mesher


def schwefel( x1,x2):  
    return 418.9829*2 - x1 * np.sin(np.sqrt( abs( x1 )))-x2*np.sin(np.sqrt(abs(x2)))

def fitness_rastrigin(position):
  fitnessVal = 0.0
  for i in range(len(position)):
    xi = position[i]
    
    fitnessVal += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
  return fitnessVal

class Particle:
  def __init__(self, fitness, dim, minx, maxx, seed):
    self.rnd = random.Random(seed)

    # initialize position of the particle with 0.0 value
    self.position = [0.0 for i in range(dim)]

     # initialize velocity of the particle with 0.0 value
    self.velocity = [0.0 for i in range(dim)]

    # initialize best particle position of the particle with 0.0 value
    self.best_part_pos = [0.0 for i in range(dim)]

    # loop dim times to calculate random position and velocity
    # range of position and velocity is [minx, max]
    for i in range(dim):
      self.position[i] = ((maxx - minx) *
        self.rnd.random() + minx)
      self.velocity[i] = ((maxx - minx) *
        self.rnd.random() + minx)

    # compute fitness of particle
    self.fitness = fitness(self.position) # curr fitness

    # initialize best position and fitness of this particle
    self.best_part_pos = copy.copy(self.position)
    self.best_part_fitnessVal = self.fitness # best fitness

# particle swarm optimization function
def pso(fitness, max_iter, n, dim, minx, maxx, W=0.729, phi_one=1.49445, phi_two=1.49445):
  # hyper parameters
  w =  W   # inertia
  c1 = phi_one  # cognitive (particle)
  c2 = phi_two # social (swarm)
  rnd = random.Random(0)
  # create n random particles
  swarm = [Particle(fitness, dim, minx, maxx, i) for i in range(n)]
  # compute the value of best_position and best_fitness in swarm
  best_swarm_pos = [0.0 for i in range(dim)]
  best_swarm_fitnessVal = sys.float_info.max # swarm best
  # computer best particle of swarm and it's fitness
  for i in range(n): # check each particle
    if swarm[i].fitness < best_swarm_fitnessVal:
      best_swarm_fitnessVal = swarm[i].fitness
      best_swarm_pos = copy.copy(swarm[i].position)
  # main loop of pso
  Iter = 0
  while Iter < max_iter:
    for i in range(n): 
      for k in range(dim):
        r1 = rnd.random()    # randomizations
        r2 = rnd.random()

        swarm[i].velocity[k] = (
                                 (w * swarm[i].velocity[k]) +
                                 (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) +
                                 (c2 * r2 * (best_swarm_pos[k] -swarm[i].position[k]))
                               )
        if swarm[i].velocity[k] < minx:
          swarm[i].velocity[k] = minx
        elif swarm[i].velocity[k] > maxx:
          swarm[i].velocity[k] = maxx
      # compute new position using new velocity
      for k in range(dim):
        swarm[i].position[k] += swarm[i].velocity[k]
      # compute fitness of new position
      swarm[i].fitness = fitness(swarm[i].position)
      # is new position a new best for the particle?
      if swarm[i].fitness < swarm[i].best_part_fitnessVal:
        swarm[i].best_part_fitnessVal = swarm[i].fitness
        swarm[i].best_part_pos = copy.copy(swarm[i].position)
      # is new position a new best overall?
      if swarm[i].fitness < best_swarm_fitnessVal:
        best_swarm_fitnessVal = swarm[i].fitness
        best_swarm_pos = copy.copy(swarm[i].position)
    Iter += 1
  return best_swarm_pos


if __name__=='__main__':                                  
    
    dim = 20
    fitness = fitness_rastrigin
    num_particles = 50
    max_iter = 100
    
    #args = parser.parse_args()
    #print(args.accumulate(args.integers))
    # rastrigin plot
    X = np.linspace(-5.12, 5.12, 100)     
    Y = np.linspace(-5.12, 5.12, 100)     
    X, Y = np.meshgrid(X, Y) 

    Z = (X**2 - 10 * np.cos(2 * np.pi * X)) + \
    (Y**2 - 10 * np.cos(2 * np.pi * Y)) + 20
 
    fig = plt.figure() 
    ax = fig.gca(projection='3d') 
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.nipy_spectral, linewidth=0.08, antialiased=True)    
    plt.savefig('rastrigin_graph.png')
    plt.show()
    
    # schwefel plot
    x1=np.linspace(-500,500)
    x2=np.linspace(-500,500)
    r_min,r_max=-500,500

    x1,x2=np.meshgrid(x1,x2)
    results=schwefel(x1,x2)
    figure=plt.figure()
    axis=figure.gca(projection='3d')
    axis.plot_surface(x1,x2,results,color='green')
    axis.plot_wireframe(x1,x2,results,color='rgb')
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Z')
    plt.savefig('schwefel_graph.png')
    plt.show()
    
    k = 0
    s = 0
    w = 0.4
    
    list_1 = []
    for i in range(15):
        list_1.append(i)
    
    best_solution = []
    phi1 = []
    phi2 = []
    while s < 3:
        s = s + 0.2
        phi_1 = s
        
        while k < 3:
            k = k + 0.2
            phi_2 = k
            best_position = pso(fitness, max_iter, num_particles, dim, -10.0, 10.0, w, phi_1, phi_2)
            fitnessVal = fitness(best_position)
            #list_1.append((phi_1, phi_2))
            phi1.append(phi_1)
            phi2.append(phi_2)
            best_solution.append(fitnessVal)
            print(f'Best solution {fitnessVal}')
    
    plt.title(str(w))
    plt.plot(list_1, best_solution, color="blue")
    plt.savefig(f'{phi_1}.png')
    plt.show()
    ax = plt.axes(projection='3d')
    ax.plot3D(phi1, phi2, best_solution, 'gray')
    plt.show()
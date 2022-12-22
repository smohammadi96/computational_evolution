## Solve TSP Problem by Genetic algorithm

## Steps

- Create initial population
  methods:
  - Random
  
- Select Parents 
  methods:
  - roulette
  
- Recombination (Crossover)
  methods:
  - Random
  - Uniform
  
- Mutation
  methods:
    - Swap
    - Flip

- Remaining selection
 methods:
    - All generations
    - New generation
    
## Experiments

**1. Crossover: n points, Mutation: Swap**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/swap_n_points.png)

**2. Crossover: n points, Mutation: Flip**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/Flip_n_points.png)

**3. Crossover: Uniform, Mutation: Flip**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/uniform_flip.png)

**4. Crossover: Uniform, Mutation: Swap**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/uniform_swap.png)

### **Result:** Experiment --> better performance.

**5. Population = 2**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/2.png)

**6. Population = 4**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/4.png)

**7. Population = 6**

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW1/images/6.png)

### **Result:** Experiments 6 and 7 --> better performance.

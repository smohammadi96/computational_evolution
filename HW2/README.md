### Comparison between PSO, ES and DS


## Test Functions

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW2/images/Rastrigin.PNG)

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW2/images/Schwefel.PNG)

## PSO
The following graphs compare the responses of the pso algorithm parameters on the Rastrigina cost function, which is displayed in two-dimensional and three-dimensional form. The horizontal axis of the two-dimensional graph indicates the test number, and the vertical axis shows the algorithm's response. The number of the test is based on ascending, starting from zero, each time the value of 0.2 is added to phi1 and phi2. The best value for w is 0.4, which improves by increasing the value of phi1 and phi2.

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW2/images/0.4.PNG)

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW2/images/0.6.PNG)

![alt text](https://github.com/smohammadi96/computational_evolution/blob/main/HW2/images/0.8.PNG)


## DS
DS is presented to overcome the main defect of genetic algorithm, i.e. the lack of local search in this algorithm. the main difference between genetic algorithms and DE is in selection operators. In the GA selection operator, the chance of selecting an answer as one of the parents depends on its superiority value, but in the DE algorithm, all answers have an equal chance to be selected. That is, the chance of their selection does not depend on their superiority value, after a new answer is generated using a self-adjusting mutation operator and crossover operator, the new answer is compared with the previous value and replaced if it is better.


The purpose of this exercise is to compare and find the best parameters for mutation probability and F value. The two graphs below show the comparison of the values ​​of these parameters. The horizontal axis in the two-dimensional graph indicates the test number and the vertical axis indicates the best answer. The three-dimensional graph also shows the x-axis of the chance of mutation, the y-axis shows the F values, and the z-axis shows the best answer.
By increasing the number of iterations, the process improves, and the best parameters for the mentioned complex cost pan are the use of the mutation value of 0.4 and the F value of 0.5.

## ES
ES is one of the evolutionary methods. which starts with an initial population, in this method, after selecting the parents, reproduction methods are used to produce a new generation, which is used in the current programs using the Discrete Recombination method. mutation also helps in finding new places and better searching the search space. The horizontal axis of the two graphs below shows the number of iterations and the vertical axis shows the best answer. The first graph shows mu, lamda and the second graph shows mu + lamda. The first chart has a better result than the second one.

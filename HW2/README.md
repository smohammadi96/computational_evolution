## Comparison between PSO, ES and DS

The following graphs compare the responses of the pso algorithm parameters on the Rastrigina cost function, which is displayed in two-dimensional and three-dimensional form. The horizontal axis of the two-dimensional graph indicates the test number, and the vertical axis shows the algorithm's response. The number of the test is based on ascending, starting from zero, each time the value of 0.2 is added to phi1 and phi2. The best value for w is 0.4, which improves by increasing the value of phi1 and phi2.


Algorithm (DE) is presented to overcome the main defect of genetic algorithm, i.e. the lack of local search in this algorithm. the main difference between genetic algorithms and DE is in selection operators. In the GA selection operator, the chance of selecting an answer as one of the parents depends on its merit value, but in the DE algorithm, all answers have an equal chance to be selected. That is, the chance of their selection does not depend on their merit value, after a new answer is generated using a self-adjusting mutation operator and crossover operator, the new answer is compared with the previous value and replaced if it is better.


The purpose of this exercise is to compare and find the best parameters for mutation probability and F value. The two graphs below show the comparison of the values ​​of these parameters. The horizontal axis in the two-dimensional graph indicates the test number and the vertical axis indicates the best answer. The three-dimensional graph also shows the x-axis of the chance of mutation, the y-axis shows the F values, and the z-axis shows the best answer.
By increasing the number of iterations, the process improves, and the best parameters for the mentioned complex cost pan are the use of the mutation value of 0.4 and the F value of 0.5.


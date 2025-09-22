# ev-charging-assignment
Assign electric vehicles (EVs) to charging stations to minimize total travel and waiting time while respecting each station’s capacity constraints. Solutions are implemented using exact methods (OR-Tools, CPLEX) and metaheuristics (Random, Greedy, Genetic Algorithm).

\## 1–14: Imports
Lines 1–3: `numpy` and `random` for numerical operations and random number generation.  
Line 4: `time` to measure execution duration.

\## 16–23: Random Assignment (initA, random\_assignment)
Lines 16–18: `initA(M, N)` initializes an MxN assignment matrix with zeros.  
Lines 20–33: `random\_assignment(M, N, cap, costs)` randomly assigns each vehicle to a station:  
\- Each vehicle is assigned \*\*exactly once\*\*.  
\- Station capacities are respected by decrementing `cap\[j]` when a vehicle is assigned.  

\## 35–50: Greedy Assignment (greedy\_assignment)
Lines 35–47: `greedy\_assignment(M, N, cap, costs)` assigns each vehicle to the \*\*available station with the minimum cost\*\*:  
\- Costs are sorted for each vehicle.  
\- The first station with remaining capacity is chosen.  
\- Ensures each vehicle is assigned once and respects station capacities.

\## 52–118: Genetic Algorithm (GA)

Lines 52–61: Population Initialization

Lines 52–54: `init\_population(pop\_size, M, N)` generates a population of random solutions.  

Lines 63–78: Repair Solution

Lines 63–78: `repair\_solution(solution, cap)` ensures that station capacities are not exceeded by adjusting assignments.  

Lines 80–92: Fitness Function

Lines 80–92: `fitness(solution, costs, cap)` computes the total cost of a solution, adding a large \*\*penalty\*\* if any station exceeds its capacity.  

Lines 94–118: GA Main Function

Lines 94–118: `genetic\_algorithm(costs, cap, pop\_size, generations, mutation\_rate)` implements the genetic algorithm:  

\- \*\*Selection\*\*: random sampling of parents.  

\- \*\*Crossover\*\*: uniform crossover between two parents.  

\- \*\*Mutation\*\*: random changes with small probability.  

\- \*\*Repair\*\*: ensures solutions respect station capacities.  

\- Tracks the \*\*best solution\*\* over generations.  

\## 120–152: Main Execution

Lines 120–152: The main script executes the three methods:  

\- Lines 123–128: Generate random capacities and cost matrix.  

\- Lines 131–138: \*\*Random approach\*\*: assign vehicles randomly, print total cost and execution time.  

\- Lines 141–148: \*\*Greedy approach\*\*: assign vehicles greedily, print total cost and execution time.  

\- Lines 151–152: \*\*Genetic Algorithm\*\*: optimize assignments, print total cost and execution time.  

\## Summary

\- Lines 16–33: Random assignment method.  

\- Lines 35–47: Greedy assignment method.  

\- Lines 52–118: Genetic Algorithm method.  

\- Lines 120–152: Main execution, printing assignments, total cost, and execution time for all three approaches.  




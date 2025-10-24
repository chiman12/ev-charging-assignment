# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 09:41:32 2025

@author: chaim
"""

import numpy as np
import random
import time

# --------------------------
# Random Assignment
# --------------------------
def initA(M, N):
    """Initialize MxN assignment matrix with zeros."""
    return np.zeros((M, N))

def random_assignment(M, N, cap, costs):
    """
    Random assignment of vehicles to stations.
    M: number of vehicles
    N: number of stations
    cap: station capacities
    costs: cost matrix (M x N)
    """
    A = np.zeros((M, N))
    for i in range(M):
        while np.sum(A[i, :]) != 1:
            j = random.randint(0, N - 1)
            if cap[j] >= 1:
                A[i, j] = 1
                cap[j] -= 1
    return A

# --------------------------
# Greedy Assignment
# --------------------------
def greedy_assignment(M, N, cap, costs):
    """
    Greedy assignment: assign each vehicle to the station with the minimum cost available.
    """
    B = np.zeros((M, N))
    for i in range(M):
        sorted_indices = np.argsort(costs[i])
        for j in sorted_indices:
            if cap[j] >= 1:
                B[i, j] = 1
                cap[j] -= 1
                break
    return B

# --------------------------
# Genetic Algorithm
# --------------------------
def init_population(pop_size, M, N):
    """Initialize a population of random solutions."""
    return [np.random.randint(0, N, M) for _ in range(pop_size)]

def repair_solution(solution, cap):
    """Repair solution if any station exceeds its capacity."""
    used = np.zeros_like(cap)
    for s in solution:
        used[s] += 1
    for j, u in enumerate(used):
        while u > cap[j]:
            idx = random.choice([i for i, x in enumerate(solution) if x == j])
            new_j = random.choice([k for k in range(len(cap)) if used[k] < cap[k]])
            solution[idx] = new_j
            u -= 1
            used[new_j] += 1
    return solution

def fitness(solution, costs, cap):
    """Calculate total cost with penalty if capacities exceeded."""
    total_cost = sum(costs[i, s] for i, s in enumerate(solution))
    used = np.zeros_like(cap)
    for s in solution:
        used[s] += 1
    penalty = sum(max(0, used[j] - cap[j]) * 1e5 for j in range(len(cap)))
    return total_cost + penalty

def genetic_algorithm(costs, cap, pop_size=50, generations=100, mutation_rate=0.01):
    M, N = costs.shape
    population = init_population(pop_size, M, N)
    best_solution = None
    best_cost = float('inf')
    
    for gen in range(generations):
        fitnesses = [fitness(sol, costs, cap) for sol in population]
        gen_best_idx = np.argmin(fitnesses)
        if fitnesses[gen_best_idx] < best_cost:
            best_solution = population[gen_best_idx].copy()
            best_cost = fitnesses[gen_best_idx]
        
        new_population = [best_solution]
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(population, 2)
            child = np.array([parent1[i] if random.random() < 0.5 else parent2[i] for i in range(M)])
            # Mutation
            for i in range(M):
                if random.random() < mutation_rate:
                    child[i] = random.randint(0, N-1)
            child = repair_solution(child, cap)
            new_population.append(child)
        population = new_population
    
    return best_solution, best_cost

# --------------------------
# Main execution
# --------------------------
if __name__ == '__main__':
    M = 1000  # number of vehicles
    N = 10    # number of stations
    
    # Random capacities and costs
    capacities = np.random.randint(10, 50, size=N)
    costs = np.random.randint(1, 100, size=(M, N))
    
    # Random approach
    start = time.time()
    random_solution = random_assignment(M, N, list(capacities), costs)
    end = time.time()
    print("Random approach total cost:", np.sum(random_solution * costs))
    print("Random approach time: {:.4f} s\n".format(end-start))
    
    # Greedy approach
    start = time.time()
    greedy_solution = greedy_assignment(M, N, list(capacities), costs)
    end = time.time()
    print("Greedy approach total cost:", np.sum(greedy_solution * costs))
    print("Greedy approach time: {:.4f} s\n".format(end-start))
    
    # Genetic algorithm approach
    start = time.time()
    ga_solution, ga_cost = genetic_algorithm(costs, list(capacities), pop_size=30, generations=50)
    end = time.time()
    print("Genetic Algorithm total cost:", ga_cost)
    print("Genetic Algorithm time: {:.4f} s".format(end-start))


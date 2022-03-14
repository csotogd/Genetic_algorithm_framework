import pandas as pd
from matplotlib import pyplot as plt

# df = pd.read_csv(r'TSP_results_cycle_crossover.csv')
# df = pd.read_csv(r'TSP_results_order_one_crossover_method.csv')
df = pd.read_csv(r'Knapsack_results_calculate_fitness_linear_violated.csv')

# diagram of aggregated by mutation rate, to see the overall best mutation rate for all of our runs
mean_df = df.groupby('mutation_rate').agg('mean')

# same as above but line per iteration number
line_per_iteration_10 = df.loc[df['iterations_number'] == 10].groupby(['mutation_rate', 'iterations_number']).agg(
    'mean')
line_per_iteration_100 = df.loc[df['iterations_number'] == 100].groupby(['mutation_rate', 'iterations_number']).agg(
    'mean')
line_per_iteration_200 = df.loc[df['iterations_number'] == 200].groupby(['mutation_rate', 'iterations_number']).agg(
    'mean')
line_per_iteration_10['mut_rate'] = line_per_iteration_10.index.get_level_values(0)
line_per_iteration_100['mut_rate'] = line_per_iteration_100.index.get_level_values(0)
line_per_iteration_200['mut_rate'] = line_per_iteration_200.index.get_level_values(0)

plt.plot(line_per_iteration_10['mut_rate'], line_per_iteration_10['average_solution_distance'], marker='o', label="10 iter")
plt.plot(line_per_iteration_100['mut_rate'], line_per_iteration_100['average_solution_distance'], marker='<', label ="100 iter")
plt.plot(line_per_iteration_200['mut_rate'], line_per_iteration_200['average_solution_distance'], marker='+', label = '200 iter')
plt.plot(mean_df.index, mean_df['average_solution_distance'], marker='*', label = 'aggregated')
plt.title('Mutation rate vs fitness by iteration parameter')
plt.xlabel('Mutation rate')
plt.ylabel('Fitness score')
plt.legend()
plt.show()


# same as above but line per population size

line_per_iteration_10 = df.loc[df['population_size'] == 10].groupby(['mutation_rate', 'population_size']).agg(
    'mean')
line_per_iteration_100 = df.loc[df['population_size'] == 100].groupby(['mutation_rate', 'population_size']).agg(
    'mean')
line_per_iteration_200 = df.loc[df['population_size'] == 200].groupby(['mutation_rate', 'population_size']).agg(
    'mean')
line_per_iteration_10['mut_rate'] = line_per_iteration_10.index.get_level_values(0)
line_per_iteration_100['mut_rate'] = line_per_iteration_100.index.get_level_values(0)
line_per_iteration_200['mut_rate'] = line_per_iteration_200.index.get_level_values(0)

plt.plot(line_per_iteration_10['mut_rate'], line_per_iteration_10['average_solution_distance'], marker='o', label="population 10")
plt.plot(line_per_iteration_100['mut_rate'], line_per_iteration_100['average_solution_distance'], marker='<', label ="population 100")
plt.plot(line_per_iteration_200['mut_rate'], line_per_iteration_200['average_solution_distance'], marker='+', label = 'population 200')
plt.plot(mean_df.index, mean_df['average_solution_distance'], marker='*', label = 'aggregated')
plt.title('Mutation rate vs fitness by population size parameter')
plt.xlabel('Mutation rate')
plt.ylabel('Fitness score')
plt.legend()
plt.show()


import gym
import numpy as np
from matplotlib import pyplot as plt

class EvolOrg:
  def __init__(self):
    self.fitness = 1

    # You can use either neural network or a GP to solve this! 
    self.brain = None

  def run_step(self, observation):
    #observation is our input
    #return an action vector
    input_vector = observation[0:13]

    #self.brain.eval/execute (input_vector)
    action_vector = np.random.uniform(-1,1,4)
    return action_vector

  def update_fitness(self, gym_reward):
    self.fitness = gym_reward

  def mutate(self):
    # TODO: Implement This!
    # make sure to return a new org (deepcopy)
    return self;
  
  def recombine(self, other_org):
    # TODO: Implement This (maybe)!
    # make sure to return a new org (deepcopy)
    return self;

class EvolPop:
  def __init__(self, num_orgs):
    self.pop_size = num_orgs
    self.generation = 0
    self.gym_environment = gym.make("BipedalWalker-v3")
    self.population = [EvolOrg() for _ in range(num_orgs)]

  def evaluate_orgs(self, num_env_steps=500, render=False):
    for org in self.population:
      #Get our initial observation
      observation = self.gym_environment.reset()
      org_fitness = 0
      for _ in range(num_env_steps):

        #Draw the world if we say to
        if(render):
          self.gym_environment.render()

        #Step the environment, updating our observations
        #and use our evolorg to decide what to do next! 
        observation, reward, done, info = self.gym_environment.step(org.run_step(observation))

        #update the fitness with this step's reward
        org_fitness += reward

        #triggers when the robot falls over -- best to save these CPU cycles! 
        if done:
          break

      org.update_fitness(org_fitness)

  def select_org(self):
    #TODO: Implement a better selection operation
    return np.random.choice(self.population)

  def do_evolution_timestep(self, mut_prob, recomb_prob=0.0):
    self.evaluate_orgs()
    new_pop = []
    for i in range(self.pop_size):
      new_org = self.select_org()

      if np.random.rand() < mut_prob:
        new_org.mutate()
      new_pop.append(new_org)
      
      #maybe do recombination, too...

    self.population = new_pop
    self.generation += 1
  
  def get_mean_fitness(self):
    return np.mean([org.fitness for org in self.population])

# Driver Code
my_pop = EvolPop(num_orgs=20)
for i in range(20):
  my_pop.do_evolution_timestep(mut_prob=0.5)
  print("Generation: {0}, Mean Fitness: {1}".format(i, my_pop.get_mean_fitness()))

#Let's watch the last generation of organisms!
#When these actually have brains, it'll hopefully be much more interesting to watch! 
my_pop.evaluate_orgs(render=True)
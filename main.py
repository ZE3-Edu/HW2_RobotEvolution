import gym
import numpy as np

eval_steps = 500

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
    return
  
  def recombine(self, other_org):
    # TODO: Implement This!
    pass

class EvolPop:
  def __init__(self, num_orgs):
    self.pop_size = num_orgs
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
      org.update_fitness(org_fitness)

  def select_org(self):
    #TODO: Implement this
    return np.random.choice(self.population)
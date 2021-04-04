# HW2 - Evolving Robot Controllers!

## Overview
In this homework assignment, you'll be taking everything we've learned so far and applying it to a fun challenging problem -- evolving a simple [bipedal robot](https://gym.openai.com/envs/BipedalWalker-v2/) that needs to balance (at least in 2d) and move through its world. 

![](https://raw.githubusercontent.com/ZE3-Edu/HW2_RobotEvolution/master/biped.png?token=AAAUTB23XSAJYVYIUER6RKLANEA46)


You can use our simple neural network class we've been building up (you'll have to re-scale the output to be in the range of -1 to 1 instead of 0 to 1 -- e.g., scale_x(x)=x*2-1). You could also use our Genetic Programing tools, with a slight modification to make sure you are within that same -1 to 1 range, and have the right number of outputs (4 in this case). 

Most of this assignment is combining things you've already done, but you could also use it as an excuse to pull in some more advanced approaches like NEAT or HyperNEAT if you want! You might also need to use some more advanced techniques (like Islands, Fitness Sharing, Recombination, etc.,) since this problem is a bit more challenging. 

## Grading
If you solve the problem using either neuroevolution or genetic programing, you'll get full points. 

If you get the neuroevolution/gp working, but not solving the problem you'll earn 90% of the final points. You can round off those last 10 percentage points by implementing more advanced evolutionary computation approaches, or by using NEAT/HyperNEAT libraries.

## Group Work
You are welcome to work together in groups, but everyone should turn in their own code and a short explanation of how the group worked together and collectively contributed to the homework assignment. 

## Some Notes
We're using the OpenAI Gym environment in this assignment, which has some nice standardized features. I'll describe some features of this specific environment, but once you wrap your head around the approach, you'll be able to try out many different types of environments if you wanted. The Repl.it you start should automatically install all the neccesary packages when you hit run for the first time. It might take a minute or two. For folks interested, this is a great walk through of [OpenAI Gym](https://gym.openai.com/docs/). 

In this world, the robot is controlled by passing in 4 values that represent the desired force to apply to 4 joints -- 2 knees and 2 hips. These should be a value between -1 and 1. Each timestep, which is very short, these 4 values are used to update the robot, and then a new set of state variables (**inputs**) is returned, and the process is continued for some number of evaluation ticks. Each tick, Gym also returns a reward, which we just accumulate and use as a fitness value for our individual. There is also a flag `done` that we'll use to stop the simulation if the robot falls over. This is a pretty computationally intensive simulation, so the less time we have to spend running robots that aren't moving, the better!  

In this environment, the inputs are a whole laundry list of angles and velocities of different parts of the robot, as well as sensors that say whether the robots feet are on the ground or not. There are even lidar sensor values that are useful in some more challenging maps. Here, we can probably just ignore them and focus on the first 14 values. You can look up what all these values are, but since we're letting ***evolution*** figure out how to control this robot, you really don't have to! 

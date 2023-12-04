# MDP
Programming Assignment 3: Solving MDPs

created by Montserrat Molina & Andrea Ulloa

## Getting Started

To clone this repo, run `https://github.com/andreapaola2018/MDP.git`

## Running our Project

In the project directory, you can run:

`python3 main.py <algorithm initials>`

## Features

Given a Markov Decision Process which models the life of a student and the decisions one must make to both have a good time and remain in good academic standing, decision making is simulated by using different basic algorithms for solving MDPs. 

Algorithms for solving MDPs are: Monte Carlo (MC), Value Iteration (VI), and Q-Learning (QL). 

### Monte Carlo (MC)
This method performs Monte Carlo First Visit method using an alpha (learning rate) of 0.1 to iterate through the MDP and returns the values of all of the states at the end of episode simulation. By default, the method will run 50 episodes.

### Value Iteration
This method performs value iteration using a discount rate (lambda) of 0.99 to iterate through the MDP and compute the value functions of each state and the final optimal policy of each state. 

### Q-Learning
The Q-learning method runs episodes repeatedly until the maximum change in any Q-value of a state-action pair is less than 0.001. The learning rate that was used was 0.2 and a discount rate (lambda) of 0.99 was also used. This is all used to find the optimal policy for the MDP. 


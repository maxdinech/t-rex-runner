# T-Rex Runner - Neural Network AI


## Needed variables

This project's goal is to create an AI to beat Chromium's T-Rex Runner game.

The needed variables for the AI are :
- The current T-Rex's **speed**
- The **distance** to the nearest obstacle
- The **width** of the nearest obstacle.

*(At first, there will be no pterodactyl management. This could be fixed by getting the height of the next obstacle)*

And to evaluate an IA's performance:
- The number of **passed** obstacles.

*(As the obstacle apparition rate is random, the ran distance is not a good evaluation criter)*

Those variables are displayed in real time on this debugged T-Rex Runner game, below the score:

![T-Rex Running](images/doc2.png)


## Coding the AI

### 1. The naive way

    file AI/naive.py

The simplest way to proceed is to make the dino jump when the nearest obstacle is clos(about 150px away). This works, but not for long : I have not yet managed to reach a score over 1k using this method.

### 2. The analytic way

    file AI/analytic.py

Another possibility is to find an application taking in parameters the speed, dist, width, and returning 1 (UP) or 0 (nothing), i.e

    f: R^3 -> {0, 1}

The problem is in determining the parameters' coefficient, and the function type (linear? polynomial?)

### 3. Genetic Algorithm

    file AI/genetic.py

To determine such coefficients, a genetic algorithm (GA) could be a good solution. We fix the fuction type as multilinear, i.e.

    f(s, d, w) = a0*s + a1*d + a2*w)

This seems a good solution but fixing the function type can be a problem in more complicated examples

### 4. Neural Networks

Bla-bla-bla
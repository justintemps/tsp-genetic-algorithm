# TSP Genetic Algorithm

**Justin Smith - MET CS 767 - Assignment 5**

## Description

This application implements a Genetic Algorithm to solve the Travelling Salesman Problem. It implements a solution for crossover proposed by Professor Eric Braude, Boston University.

## Installation

1. Clone this repository

2. Start a Python environment

```bash
python3 -m venv .env
```

3. Activate the environment

```bash
source .env/bin/activate
```

4. Install requirements

```bash
pip3 install -r requirements.txt
```

## What's inside

### App

- Runs the algorithm with randomly generated cities
- Create a line chart showing the algorithm's progress after successive generations
- Parameters for altering the data and hyperparameters for modyfing the algorithm are
  available as constants listed at the top of the file
- City distances are calculated automatically from lat/long coordinates

From the project root:

```bash
python3 app.py
```

## Resources

- [Evolution of a salesman: A complete genetic algorithm tutorial for Python](https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35)

- [How the Genetic Algorithm Works](https://www.mathworks.com/help/gads/how-the-genetic-algorithm-works.html)

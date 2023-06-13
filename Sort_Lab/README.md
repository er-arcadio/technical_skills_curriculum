# TITLE

[![Run on Repl.it](https://repl.it/badge/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)](https://repl.it/github/upperlinecode/<INSERT_GITHUB_EXTENSION>)

## Contents

- [Intro](#intro)
- [The Lab](#the-lab)
- [Hints & Resources](#hints--resources)
- [Extensions](#extensions)

## Intro

If you haven't already, take a couple of minutes to familiarize yourself with the ["Sort the Cards" app](https://sortinggame.emmanuelrodri23.repl.co/). Notice how as you attempt to sort the cards in order from least to greatest, the 'observations', 'cycles', and 'moves' counters go up. Sorting items can be costly in different ways which means the algorithm we use to sort them will vary based on the demands.

In this lab, you will be asked to code up algorithms you create that must cater to a range of demands. 

## The Lab

For the following challenges, a price will be put on each counter in the Sort the Cards app. Your goal is to come up with an algorithm to keep the cost as low as possible. 

**Low Moving**

- Come up with a strategy to sort the cards while keeping the **"moves"** number as low as possible. Then, write the code that follows the same algorithm.
    - Observations = $1
    - Cycles = $2
    - Moves = $8
    - Storage = $0

- Teacher note: Best algorithm here is Insertion or Selection sort depending on the state of the original array.

<details>
<summary>One Solution to "Low Moving"</summary>

```py
# One way to code Selection Sort
sample_list = [5, 2, 1, 3, 4]

for i in range(len(sample_list) - 1):
    smallest_idx = i

    for j in range(i+1, len(sample_list)):
        if sample_list[j] < sample_list[smallest_idx]:
            smallest_idx = j
    
    # Note the swap outside the inner for loop; N=5 swaps
    if smallest_idx != i:
        (sample_list[smallest_idx], sample_list[i]) = (sample_list[i], sample_list[smallest_idx])
```
</details>
<br>

**Low Observations & Cycles**

- Observations and Cycles are sort of connected. Come up with a strategy to sort the cards while keeping these counters as low as possible. Then, write the code that follows the same algorithm.
    - Observations = $2
    - Cycles = $8
    - Moves = $1
    - Storage = $0

    For this challenge, check the More Storage checkbox at the top of the page!

- Teacher note: Best algorithm here is Quick sort. Other good ones are Radix and Merge sort. Both are tricky to conceptualize and code. Consider having students share their algorithms instead of sharing this one.

<details>
<summary>One Solution to "Low Cycles"</summary>

```py
#Radix Sort
import random

# list of 20 random numbers between 0-999
sample_list = random.sample(range(1000), 20)
print(sample_list)


# find the max # of digits / place values
max_num = sample_list[0]
for num in sample_list:
    max_num = max(max_num, num)
    
digits = 0
while max_num:
    digits += 1
    max_num = max_num // 10
print(digits)
    
# For every place value, group by place value then combine again
for place in range(digits):
    counter = [[] for i in range(10)]
    for num in sample_list:
        digit = num // 10**place % 10
        counter[digit].append(num)
    print(f"Grouped by {10**place}'s place", counter)
    sample_list = []
    for nums in counter:
        sample_list += nums
        
    print("Combined", sample_list)
```
</details>
<br>

## Extensions

Your list now represents a train track full of large train cars. Each number represents the weight of a car in 1,000 kilograms. There's several things you can do to ultimately sort the cars from lightest to heaviest. You can:
- **Weigh** a car - lift it from the tracks using the fork lift's built in scale
- Remove a car from the tracks and **hold** it off to the side using the forklift
- **Insert** the held car back onto the tracks
- Slide or **shift** the car over one space to the left or right. (Positively to the right, or negatively to the left) 

You have heavy machinery to help you do these things, but the machinery costs money!

**Mild**
- Manually print the 1st element in the list of `train_cars`
- Use the `weigh(idx)` function to print the weight of the 100th train car
- Hold the 50th train car using the `hold(idx)` function and print the `forklift` variable to show that car.

**Medium**
- Use any one of the sorting algorithms you've already used to sort the `train_cars` using only the 4 functions in the file. _HINT: use lots of print statements to see what's happening_
- Notice how each function has the line `total_cost += 0`. Add a cost of $100 to each function. Then, run your sort and see how much money it costs.

**Spicy**

- Change the costs to the following 4 scenarios, and write a new sorting function that minimizes cost. Compare with your other functions. ALSO: give yourself a `floor_space`, 1 variable that can hold a train car while your `forklift` is moving another. 

1. Moving the forklift costs gas and time both of which is on a surge:
    - Weigh = $100
    - Hold = $200
    - Insert = $200
    - Shift = $100

2. The scale is new technology. The new technology is pricy! At least gas prices are down.
    - Weigh = $400
    - Hold = $75
    - Insert = $75
    - Shift = $50

3. We need to hire more people to help shift the cars because our forklift no longer can do that:
    - Weigh = $200
    - Hold = $150
    - Insert = $150
    - Shift = $400

## Hints & Resources

- Use the [Sort the Cards](https://sortinggame.emmanuelrodri23.repl.co/) app to help visualize things when they get too hard to conceptualize.
- With the train cars, you can look up these "in-place" sorting algorithms to help you get started. In order from east to hard: bubble sort, selection sort, insertion sort, and quicksort sort.
"""
Car Fleet

There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it.
It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed.
A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination,
then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1

Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet,
meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3

Explanation: The cars starting at 4 and 7 become a fleet at position 10.
The cars starting at 1 and 0 never catch up to the car ahead of them.
Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.
"""
import heapq


# Slower execution speed due to heap and higher space complexity due to stack
def car_fleet (target, position, speed):
    # Change the priority
    for i in range(len(position)):
        position[i] = (target - position[i], speed[i])

    heapq.heapify(position)

    stack = []

    for i in range(len(position)):
        p, s = heapq.heappop(position)
        p = target - p
        t = (target - p) / s
        if len(stack) == 0:
            stack.append((p, t))
            continue

        if (stack[-1][1] >= t):
            continue
        stack.append((p, t))

    return len(stack)


# Faster execution speed
# Using Zip + Sort, instead of using heapify
def car_fleet (target, position, speed):
    # Pair up position and speed, then sort by position in descending order
    cars = sorted(zip(position, speed), reverse=True)

    fleets = 0
    time_to_reach_target = 0

    for p, s in cars:
        t = (target - p) / s  # Time for the current car to reach the target

        # If the current car's time to reach target is greater than the last recorded time,
        # it forms a new fleet.
        if t > time_to_reach_target:
            fleets += 1
            time_to_reach_target = t

    return fleets


# target = 10
# position = [4,1,0,7]
# speed = [2,2,1,1]
# op = car_fleet(target, position, speed)
# print(op)

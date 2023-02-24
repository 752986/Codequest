# Problem 183 : Calling All Firefighters

**Difficulty:** Hard

**Author:** Dr. Leon Clark, Melbourne, Victoria, Australia

**Originally Published:** Code Quest 2022

---

## Problem Background

In a disaster situation, maintaining open lines of communication with everyone involved - both first responders and regular civilians caught in the disaster - is important to limit casualties and the amount of damage. Unfortunately, geographic features like mountains can make communication difficult. Many modern means of communication rely on radio signals, which can be blocked by large mountains or other features that block a direct line of sight between a signal tower and a communication device.

## Problem Description

Lockheed Martin is working with the Australian Defence Force to set up a means of quickly establishing new communication relays in the event of another round of disastrous wildfires. The ADF plans to provide Lockheed Martin with a cross-section of a topographical map showing the layout of terrain in the impacted area. This map will include numbers showing the proposed locations of a communications tower (marked with a number 0) and several command posts (marked with numbers 1 through 9). Your team has been asked to design an algorithm which can determine which of the command posts are viable, based on the location of the communications tower.

The map is extremely low resolution, and so each cell within the map represents a one square kilometer area. Each area is considered to be completely filled either with solid ground (#) or open air (a space or number). In order for a command post to be in a viable location, firefighters must be able to raise a communications antenna in the center of that location; this antenna must have a direct, unobstructed line of sight to the tower. The transmitters for both antenna and tower will be located in the exact center of their respective areas (half a kilometer from the edges of the cell drawn on the map). If a straight line drawn from those two points comes into contact with the ground at any point, the signal from the tower will be at least partially blocked, which will interfere with communications

## Sample Input

The first line of your program's input, received from the standard input channel, will contain a positive integer representing the number of test cases. Each test case will include:

- A line containing three positive integers, separated by spaces, as follows:
    - `H`, representing the height of the map in rows (minimum 4)
    - `W`, representing the width of the map in characters (minimum 30)
    - `C`, representing the number of command posts that will be displayed on the map (minimum 2)
- `H` lines, each containing up to `W` characters, representing a cross section of a topographical map. Each line may contain any of the following characters:
    - A #, representing solid ground, which blocks radio signals.
    - A space, representing open air. Note that input lines will not contain trailing whitespace; if a line contains fewer than `W` characters, you may assume that any missing characters after the last visible character are intended to be spaces.
    - A number 0 (zero), representing the proposed location of a communication tower. There will be exactly one 0 in each test case.
    - Any number from 1 to `C` inclusive, representing the proposed location of a command post. There will be exactly one of each relevant number in each test case.

```
2
6 45 4
                                  4
             0                  ####
           ####                #######
    #############   2       ############
    3 ################   ################  1
#############################################
5 45 4
             1                 4####
           ####                #######
    #############   2       ############
    3 ################   ################  0
#############################################
```

## Sample Output

For each test case, your program must print a single line, as follows:

- If at least one command post is in a viable location, print the list of the numbers representing those locations, in increasing order, separated by spaces.
- If no command posts are in viable locations, print the phrase "No viable locations".
```
2 4 
No viable locations
```
# TRAINS!

The local commuter railroad services a number of towns in Pythonland.
Because of monetary concerns, all the tracks are ‘one-way.’
That is, a route from Distoia to Tupleling does not imply the existence of a route from Tupleling to Distoia.
In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

## Problem

The purpose of this problem is to help the railroad provide its customers with information about the routes.
In particular, you will compute the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

## Questions

1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3 stops. In the sample data, there are two such trips: C-D-C (2 stops) and C-E-B-C (3 stops)
7. The number of trips starting at A and ending at C with exactly 4 stops, with the last stop being the destination. In the sample data, there are two such trips: ABCDC,  ADCDC and ADEBC.
8. The total distance of the shortest route from A to C.
9. The total distance of the shortest route from B to B.
10. The number of different routes from C to C with a distance of less than 30. In the sample data, the trips are: CDC, CDCEBC, CDEBC, CEBC, CEBCDC, CEBCEBC, CEBCEBCEBC.

## Input

A directed graph where a node represents a town and an edge represents a route between two towns.
The weighting of the edge represents the distance between the two towns.
A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.

### Test Input 01
For the test input, the towns are named using the first few letters of the alphabet from A to E. A route between two towns (A to B) with a distance of 5 is represented as AB5.

Input Graph: **AB5, AD5, AE7, BC4, CD8, CE2, DC8, DE6, EB3**

## Output

The answer for questions in order as they appear.
For test input 1 through 5, if no such route exists, output **‘NO SUCH ROUTE’**.
Otherwise, follow the route as given without making any extra stops!

## Expected Output for test input 01

1. 9
2. 5
3. 13
4. 22
5. NO SUCH ROUTE
6. 2
7. 3
8. 9
9. 9
10. 7
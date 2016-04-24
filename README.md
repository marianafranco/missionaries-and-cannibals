
# Missionaries and Cannibals Problem

Solutions for the [Missionaries and Cannibals Problem](https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem).


> In this problem, three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board. And, in some variations, one of the cannibals has only one arm and cannot row. [source: Wikipedia]

## Solutions

The problem was solved using three different languages: Java, Python and Prolog:

### Java

A `State` class saves the current state of the problem, that is, how many missionaries and cannibals are in each side of the river and where is the boat (left or right).

The `generateSuccessors` method checks the actions (e.g. cross a two missionaries from left to right) that can be applied to a particular state and returns the valid successor states.

The initial state of the problem is passed as input to the bread first search algorithm (class `BreadthFirstSearch`) that returns the solution to the problem.

The Java solution can be found in the [java](https://github.com/marianafranco/missionaries-and-cannibals/tree/master/java) folder. You can use the jar executable file to run it:

```
java -jar missionaries_and_cannibals.jar
```

### Prolog

First was defined the 10 rules that determine which are the possible successor states for each possible action. Then a recursive rule `path` is responsible for find the solution of the problem.

Running the Prolog code in [SWI-Prolog](http://www.swi-prolog.org/):

```
?- ['missionaries_and_cannibals.pl'].
?- find.
```

### Python

The Python solution is similar to the Java one. A `State` class saves the current state of the problem. The `successors` method checks the actions that can be applied to each state. And the `breadth_first_search` method returns the solution to the problem.

Running the Python solution:

```
python missionaries_and_cannibals.py
```

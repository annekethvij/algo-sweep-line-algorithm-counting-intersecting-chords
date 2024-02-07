# algo-sweep-line-algorithm-counting-intersecting-chords

## Overview
This Python program calculates the total number of intersections among chords within a circle. It utilizes a sorting and counting approach to efficiently determine how many times chords intersect based on their radian measures and identifiers.

## Understanding the Basics

If you're already familiar with chords and radian measures, Please feel free to skip ahead!

- **Chords**: In geometry, a chord is a line segment whose endpoints lie on a circle's circumference. When you draw a straight line from one point on the edge of a circle to another, you've got yourself a chord.
- **Radian Measures**: A radian is a way of measuring angles based on the radius of a circle. It is the angle created at the center of a circle by an arc whose length is equal to the radius of the circle. The total circumference of a circle is 2π radians, which equates to 360 degrees. Thus, radian measures in this context define the position of chord endpoints on the circle's circumference.

## Algorithm Description
The algorithm follows these steps:
1. Parse the input tuple into radian measures and identifiers for chord endpoints.
2. Create a list of chord events, marking each as either a 'start' or an 'end' along with its radian measure.
3. Sort these chord events first by radian measure and then by event type ('start' before 'end') to maintain chronological order.
4. Iterate through sorted chord events, counting intersections based on the number of currently active chords each time a new chord starts.

## Complexity Analysis
- **Sorting**: The sort operation has a Big O complexity of `O(n log n)`, with `n` being the total number of chord endpoints.
- **Iteration**: The single pass through the sorted chord events for counting intersections is `O(n)`.
Overall, the program operates with a Big O complexity of `O(n log n)` due to the sorting step.

## Running the Program
Ensure Python is installed on your system to execute the program.

1. Copy the provided Python code into a file, e.g., `chord_intersections.py`.
2. Prepare input data in the following format: `([radian_measures], ["identifiers"])`, where `radian_measures` is a list of chord endpoints' radian measures, and `identifiers` indicate whether each endpoint is a start or an end of a chord.
3. Execute the script via a command line or terminal:
    ```bash
    python chord_intersections.py
    ```
4. The script outputs the count of unique intersections among the chords.

### Example
```python
input_data = ([0.78, 1.47, 1.77, 3.92], ["s_1", "s_2", "e_1", "e_2"])
print(calculate_chord_intersections_count(input_data))
```

This example calculates the number of intersections for chords defined by the given radian measures and identifiers, outputting the result to the console.

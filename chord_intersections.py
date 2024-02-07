def calculate_chord_intersections_count(input_data):
    """
    Calculates the total number of intersections between chords in a circle.

    Parameters:
    - input_data (tuple): First element is a list of radian measures (floats) for chord radian measures,
      and the second element is a list of corresponding start ('s_') and end ('e_') identifiers (strings).

    Returns:
    - int: Count of unique intersections among the chords.
    """
    # print("entering function: calculate_chord_intersections_count") # Debug statement
    # print("input_data: ", input_data) # Debug statement
    radian_measures, identifiers = input_data
    # print("radian_measures: ", radian_measures) # Debug statement
    # print("identifiers: ", identifiers) # Debug statement
    # Create chord_events for all start and end points
    chord_events = []
    for idf in identifiers:
        num = idf.split('_')[1]
        if 's' in idf:
            start_measure = radian_measures[identifiers.index(idf)]
            chord_events.append((start_measure, 'start', int(num)))

        else:
            end_measure = radian_measures[identifiers.index(idf)]
            chord_events.append((end_measure, 'end', int(num)))

    # print("chord_events before sorting: ", chord_events) # Debug statement
    # Sorting the chord_events by the radian measure and
    # ensuring that the start chord_events are considered before ends in case of any ties
    chord_events.sort(key=lambda x: (x[0], x[1]))
    # print("chord_events after sorting: ", chord_events) # Debug statement
    active_chords = 0
    intersections = 0

    for measure, event_type, num in chord_events:
        if event_type == 'start':
            # Each active chord will intersect with this new chord
            intersections += active_chords
            active_chords += 1
            # print(f"Starting chord {num} at {measure}, active chords now: {active_chords}, intersections: {intersections}")

        else:
            active_chords -= 1
            # print(f"Ending chord {num} at {measure}, active chords now: {active_chords}")  # Debug statement

    # print(f"exiting function: calculate_chord_intersections_count, returning intersections: {intersections}")# Debug statement
    return intersections

input_data = ([0.78, 1.47, 1.77, 3.92], ["s_1", "s_2", "e_1", "e_2"])
print(calculate_chord_intersections_count(input_data))

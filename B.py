def grouped_median(class_intervals, frequencies):
    if len(class_intervals) != len(frequencies):
        raise ValueError("Class intervals and frequencies should have the same length.")

    total_frequency = sum(frequencies)
    median_position = total_frequency / 2

    cumulative_frequency = 0
    for i, frequency in enumerate(frequencies):
        cumulative_frequency += frequency
        if cumulative_frequency >= median_position:
            median_class = class_intervals[i]
            break

    lower_boundary = median_class[0]
    class_width = median_class[1] - median_class[0]
    frequency_median_class = frequency

    median = lower_boundary + ((median_position - (cumulative_frequency - frequency)) / frequency) * class_width

    return median

# Example usage:
class_intervals = [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]
frequencies = [5, 8, 12, 7, 3]

result = grouped_median(class_intervals, frequencies)
print(f"Median: {result}")

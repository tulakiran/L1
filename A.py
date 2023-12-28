def grouped_mean(midpoints, frequencies):
    if len(midpoints) != len(frequencies):
        raise ValueError("Midpoints and frequencies should have the same length.")

    total_frequency = sum(frequencies)

    # Calculate the sum of (midpoint * frequency)
    sum_midpoint_frequency = sum(midpoint * frequency for midpoint, frequency in zip(midpoints, frequencies))

    # Calculate the mean
    mean = sum_midpoint_frequency / total_frequency

    return mean

# Example usage:
midpoints = [10, 20, 30, 40, 50]
frequencies = [5, 8, 12, 7, 3]

result = grouped_mean(midpoints, frequencies)
print(f"Mean: {result}")

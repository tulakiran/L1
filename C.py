import math

def grouped_standard_deviation(midpoints, frequencies):
    if len(midpoints) != len(frequencies):
        raise ValueError("Midpoints and frequencies should have the same length.")

    total_frequency = sum(frequencies)
    mean = sum(midpoint * frequency for midpoint, frequency in zip(midpoints, frequencies)) / total_frequency

    sum_squared_deviation = sum((midpoint - mean) ** 2 * frequency for midpoint, frequency in zip(midpoints, frequencies))

    standard_deviation = math.sqrt(sum_squared_deviation / total_frequency)

    return standard_deviation

# Example usage:
midpoints = [10, 20, 30, 40, 50]
frequencies = [5, 8, 12, 7, 3]

result = grouped_standard_deviation(midpoints, frequencies)
print(f"Standard Deviation: {result}")

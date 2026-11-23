
numbers = [10, 20, 30, 40, 50, 20, 30]


def sum_numbers(numbers):
    total = sum(numbers)
    return total


def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


def calculate_median_mode(numbers):
    from statistics import median, mode

    med = median(numbers)
    mod = mode(numbers)

    return med, mod


print("Numbers:", numbers)
print("Sum:", sum_numbers(numbers))
print("Average:", calculate_average(numbers))

median_value, mode_value = calculate_median_mode(numbers)

print("Median:", median_value)
print("Mode:", mode_value)

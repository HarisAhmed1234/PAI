def analyze_temperatures(temps):
    avg_temp = sum(temps) / len(temps)
    print(f"The average temperature this month is: {avg_temp:.2f}°C")

    max_temp = max(temps)
    min_temp = min(temps)
    print(f"The highest temperature recorded was: {max_temp}°C")
    print(f"The lowest temperature recorded was: {min_temp}°C")

    sort_ascendingorder_temps = sorted(temps)
    print("Temperatures in ascending order:", sort_ascendingorder_temps)

    print("Current list of temperatures:", temps) 

    day = int(input("Enter the day (1-31) to remove its temperature: ")) - 1
    if 0 <= day < len(temps):
        removed_temp = temps.pop(day)  # pop function to remove element
        print(f"Temperature for day {day + 1} ({removed_temp}°C) has been removed.")
    else:
        print("Invalid day. No changes made.")

    print("Updated list of temperatures:", temps)


temperatures = [26.5, 29.2, 33.8, 28.7, 35.3, 31.4, 37.1, 30.0, 27.9, 34.6,
                32.2, 29.8, 36.5, 28.3, 25.9, 39.4, 27.6, 33.1, 31.9, 38.7,
                30.3, 29.0, 34.1, 26.8, 35.7, 28.1, 32.5, 37.9, 30.8, 33.3]

analyze_temperatures(temperatures)

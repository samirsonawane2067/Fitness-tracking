import csv
import os

# File to store fitness tracking data
DATA_FILE = 'fitness_data.csv'


class FitnessTracker:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Activity', 'Duration (minutes)', 'Calories Burned'])

    def add_activity(self, activity, duration, calories):
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([activity, duration, calories])
        print(f'Added: {activity}, Duration: {duration} minutes, Calories: {calories}')

    def view_activities(self):
        if os.stat(DATA_FILE).st_size == 0:
            print("No activities logged yet.")
            return
        
        print(f'\n{"Activity":<20}{"Duration (minutes)":<20}{"Calories Burned":<15}')
        print('-' * 55)

        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                print(f'{row[0]:<20}{row[1]:<20}{row[2]:<15}')
        print()

    def total_calories(self):
        total = 0
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total += int(row[2])
        print(f'Total Calories Burned: {total}')


def main():
    tracker = FitnessTracker()

    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. View Total Calories Burned")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            activity = input("Enter activity (e.g., Running, Cycling): ")
            duration = input("Enter duration (in minutes): ")
            calories = input("Enter calories burned: ")
            tracker.add_activity(activity, duration, calories)

        elif choice == '2':
            tracker.view_activities()

        elif choice == '3':
            tracker.total_calories()

        elif choice == '4':
            print("Exiting Fitness Tracker. Stay healthy!")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()

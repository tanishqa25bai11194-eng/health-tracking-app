import datetime 

# Function to log data into a file 

def log_data(file_name, data):

    with open(file_name, 'a') as f:

        f.write(data + '\n')

# Function to record today's weight 

def record_weight():

    weight = input("Enter your weight (in kg): ")

    log_data('weight_log.txt', f"{datetime.date.today()}: {weight} kg")

    print("Weight recorded successfully!")

# Function to record calories consumed 

def record_calories():

    calories = input("Enter the number of calories consumed today : ")

    log_data('calories_log.txt', f"{datetime.date.today()}: {calories} kg")

    print("Calories recorded successfully!")

# Function to record exercise details 

def record_exercise():

    exercise = input("Enter the type of exercise: ")

    duration = input("Enter the duration of exercise (in minutes): ")

    log_data('exercise_log.txt', f"{datetime.date.today()}: {exercise} minutes")

    print("Exercise recorded succesrfully!")

# Function to view recorded data 

def view_data():

    choice = input("What would you like to view? (1) Weight (2) Calories (3) Exercise: ")

    file_dict = {'1': 'weight_log.txt' ,'2': 'calories_log.txt' ,'3': 'exercise_log.txt'}

    if choice in file_dict:

        try:

            with open(file_dict[choice], 'r') as f:

                print(f.read())

        except FileNotFoundError:

            print("No data recorded yet.")

    else:

        print("Invalid choice!")

 # Main app Loop 

def main():

    print("Welcome to the Health Tracking App!")

    while True:

        print("\nWhat would you like to do?")

        print("1. Record weight")

        print("2. Record calories consumed")

        print("3. Record exercise")

        print("4. View your data")

        print("5.Exit")

        choice = input("Enter your choice (1-5): ")\
        
        if choice == '1':

            record_weight()

        elif choice == '2':

            record_calories()

        elif choice == '3':

            record_exercise()

        elif choice == '4':

            view_data()

        elif choice == '5':

            print("Thank you for using the Health Tracking App. Stay healthy!")

            break 

        else:

            print("Invalid choice, please try again.")

if __name__ == "__main__":

    main()

    
        




        




















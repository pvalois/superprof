import csv
import random

# List of names and surnames for generating triplets
first_names_male = ["John", "David", "Michael", "Chris", "James", "Robert", "William", "Mark", "Andrew", "Paul"]
last_names_male = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Garcia", "Martinez", "Hernandez"]

first_names_female = ["Mary", "Linda", "Patricia", "Jennifer", "Elizabeth", "Susan", "Jessica", "Sarah", "Karen", "Nancy"]
last_names_female = ["Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "King"]

# Function to generate random triplets (name, surname, gender)
def generate_triplet():
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        first_name = random.choice(first_names_male)
        last_name = random.choice(last_names_male)
    else:
        first_name = random.choice(first_names_female)
        last_name = random.choice(last_names_female)
    
    return [first_name, last_name, gender]

# Generate and save 40 files with triplets
for i in range(40):
    file_name = f"triplet_file_{i+1}.csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write 100 triplets to each file
        for _ in range(100):
            writer.writerow(generate_triplet())

import random

print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
x = input("Choose a random number \n")
streets = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Fort Worth', 'Charlotte', 'Indianapolis', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit', 'Nashville', 'Portland', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Cleveland', 'Tulsa', 'Minneapolis', 'Wichita', 'New Orleans', 'Arlington', 'Honolulu', 'Anaheim', 'Santa Ana', 'St. Louis']
pets = ['Bella', 'Max', 'Charlie', 'Lucy', 'Buddy', 'Daisy', 'Rocky', 'Molly', 'Cooper', 'Lola', 'Bear', 'Sadie', 'Duke', 'Ruby', 'Milo', 'Sophie', 'Jack', 'Chloe', 'Toby', 'Zoe', 'Oliver', 'Bella', 'Bailey', 'Stella', 'Teddy', 'Coco', 'Winston', 'Penny', 'Oscar', 'Ginger', 'Jackson', 'Lily', 'Finn', 'Mia', 'Apollo', 'Simba', 'Nala', 'Shadow', 'Hazel', 'Rusty', 'Koda', 'Marley', 'Roxy', 'Sammy', 'Jasper', 'Gracie', 'Zeus', 'Ruby', 'Scout', 'Bandit', 'Annie', 'Sassy']

ans = random.randint(0,abs(int(x)%50))
print("Your band name could be " + street + " " + pet+ "\n")
print("Your random band name based on the number could be " + streets[ans] + " " + pets[ans])


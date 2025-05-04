#Simple Interest Calculator
# This program calculates the simple interest based on user input
# It takes the principal amount, rate of interest, and time period as input
P=input("Enter the principal amount: ")
R=input("Enter the rate of interest: ")
T=input("Enter the time period in years: ")
# Convert the input values to float
P=  int(P)
R=  int(R)
T=  int(T)
# Calculate the simple interest using the formula SI = (P * R * T) / 100
SI=(P*R*T)/100
# Print the calculated simple interest
print("The Simple Interest is: ", SI)
# The program takes the principal amount, rate of interest, and time period as input from the user,
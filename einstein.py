#Code to take user inputted mass number and calculate the energy using Einstein's equation E=mc^2

mass= int(input("Please input a mass number in kilograms: ")) #prompt user for input
c2= 90000000000000000 #speed of light squared
energy= mass*c2 #calculate energy using Einstein's equation
print(f"{energy:,}") #print energy with commas 
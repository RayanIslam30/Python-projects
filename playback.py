#Code to prompt user for input and replace spaces with ellipses

playback = input("Please input a string: ") #prompt user for input
playback = playback.replace(" ","...") #replace spaces with ellipses
print(playback)  #print modified string
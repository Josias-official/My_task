#program to read in the times swimming 
swimming = int(input("Enter time taken for swimming in minutes : "))
print("Time taken for Swimming task: ",swimming)
#program to read in the times cycling
cycling = int(input("Enter time taken for cycling in minutes : "))
print("Time taken for Cycling task: ",cycling)
#program to read in the times running
running = int(input("Enter time taken for running in minutes : "))

#program to award a participant based on the total time 
#calculate and display the total time taken to complete the triathlon 
Total_time = swimming + cycling + running
print("Total time taken for triathlon: ",Total_time)

if (Total_time < 100):
    print("Provincial Colors")
elif (Total_time > 100 and Total_time <=105):
    print("Provincial Half Colors")
elif (Total_time >105 and Total_time <=110):
    print("Provincial Scroll")
else:
    print("No award")
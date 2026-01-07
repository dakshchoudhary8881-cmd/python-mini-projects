# ***************** auto  greets (good morning , afternoon , evening ) according to indian time ****************


import time

current_time = time.strftime("%H:%M:%S")
print(current_time)

#only print hours of the time
hour = int(time.strftime("%H"))
 
if(hour > 4 and hour < 12):
    print("Good Morning Daksh")

elif(hour > 12 and hour < 17 ):
    print("Good Afternoon Daksh")

elif(hour >= 17 and hour < 21):
    print("Good Evening Daksh")
    
else:
    print("Good Night Daksh")


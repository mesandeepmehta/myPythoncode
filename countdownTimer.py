import time
import winsound
Time = int(input("Enter time in seconds: "))
n=0
while Time >= n:
    print (Time,"s")
    Time = Time-1
    time.sleep(1)
print("Your timer is up!")
winsound.Beep(2000,1200)


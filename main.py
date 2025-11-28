import time
import winsound

t = int(input("Focus minutes: "))*60
start = time.time()

print("Focus started...")
time.sleep(t)

end = time.time()
print("Done! Focus for", round((end-start)/60,1),"minutes.")

for _ in range(5):
    winsound.Beep(1000, 500)   # (frequency, duration)
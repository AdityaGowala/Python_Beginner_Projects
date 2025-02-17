# The user sets a time for the alarm.
# The program continuously checks the current time.
# When the set time matches the current time, an alarm sound plays
# (Optional) Add a snooze function..

import datetime
import time

def set_allarm():
    allarm = input("\nSet alarm (HH:MM:SS): ").strip()
    try:
        allarm = datetime.datetime.strptime(allarm ,"%H:%M:%S").time()
        print(f"Alarm set for {allarm}")

        while True:
            current_datetime = datetime.datetime.now().time()
            if current_datetime >= allarm:
                print("\n⏰ ALARM! Time to wake up!")
                break
            time.sleep(1)


    except ValueError:
        print("Invalid time format! Use HH:MM:SS")


def main():
    set_allarm()
main()
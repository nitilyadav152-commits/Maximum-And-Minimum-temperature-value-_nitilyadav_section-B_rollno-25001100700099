import random
import time

# Accept minimum and maximum temperature from user
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

# Validate limits
if min_temp >= max_temp:
    print("Error: Minimum temperature must be less than maximum temperature.")
else:
    print("\nTemperature Monitoring Started...\n")
    
    try:
        while True:
            # Generate random temperature between 0 and 100
            current_temp = random.uniform(0, 100)
            
            print(f"Current Temperature: {current_temp:.2f}°C")
            
            # Compare temperature with limits
            if current_temp > max_temp:
                print("Alert: Temperature is too high!")
            elif current_temp < min_temp:
                print("Alert: Temperature is too low!")
            else:
                print("Temperature is within safe limits.")
            
            print("-" * 40)
            
            # Wait for 2 seconds
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("\nMonitoring Stopped.")
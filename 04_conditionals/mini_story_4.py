device_status = input("Enter device status (active/offline): ")
temperature = int(input("Enter the current temperature in Celsius: "))

if device_status == "active":

    if temperature > 35:
        print("High temperature detected. Activating cooling system.")
    else:
        print("Temperature is within normal range.")

else:
    print("Device is offline.")
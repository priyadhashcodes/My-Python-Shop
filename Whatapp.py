import pywhatkit

phone_no = input("Enter phone number with country code: ")
message = input("Enter your message: ")

time_input = input("Enter time (HH:MM format like 16:12): ")

hour, minute = map(int, time_input.split(":"))

pywhatkit.sendwhatmsg(phone_no, message, hour, minute)

print("Message scheduled successfully!")
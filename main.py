# importing the module
import pywhatkit
import time
while True:
# using Exception Handling to avoid
# unprecedented errors
    try:

        # sending message to receiver
        # using pywhatkit
        pywhatkit.sendwhatmsg("+916296642512",
                        "Hello from GeeksforGeeks",
                        23, 59)
        print("Successfully Sent!")

    except:

        # handling exception
        # and printing error message
        print("An Unexpected Error!")
    time.sleep(86400)

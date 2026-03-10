import serial    # for serial communication
import time      # for delay
import speech_recognition as sr   # for speech recognition
import random    # for generating temporary code
import smtplib  # for sending email
from email.mime.text import MIMEText  # for creating email content

SENDER = "YOURSENDEREMAİL"
SENDERMAILPASSWORD = "YOURAPPLICATIONPASSWORD"  # write the application password of the mail here
RECEIVER = "YOURRECEIVEREMAIL"

def clean_password(text):
    """Extract 4-digit password from recognized text"""
    result = ""
    for ch in text:
        if ch.isdigit():
            result += ch
    if len(result) == 4:
        return result
    else:
        return None

def send_email(code):
    """Send the temporary code via email"""
    msg = MIMEText("Your temporary code: " + code)
    msg["Subject"] = "Lock System"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(SENDER, SENDERMAILPASSWORD)
    s.send_message(msg)
    s.quit()

arduino = serial.Serial("YOUR_PORT", 9600)
time.sleep(2)

r = sr.Recognizer()
mic = sr.Microphone()

password = "1234"
attempts = 3
mode = "normal"
temporary_code: str = ""

print("System Ready")

def listen():
    """Listen to user's voice and recognize text in English"""
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="en-US")
        return text.lower()
    except:
        return ""

while True:
    try:
        if mode == "normal":
            print("Please say your password (4 digits):")
            arduino.write(b"ENTER_PASSWORD\n")
            text = listen()
            entered_password = clean_password(text)

            if entered_password is None:
                print("Invalid format.")
                arduino.write(b"ERROR\n")
                continue

            if entered_password == password:
                print("CORRECT")
                arduino.write(b"CORRECT\n")
                attempts = 3
                text = listen()
                if any(word in text for word in ["close", "lock", "shutdown"]):
                    print("The box is closing...")
                    arduino.write(b"CLOSE\n")
                    continue
            else:
                attempts -= 1
                print("WRONG | Remaining attempts:", attempts)
                arduino.write(b"WRONG\n")

                if attempts == 0:
                    mode = "blocked"
                    temporary_code = str(random.randint(1000, 9999))
                    send_email(temporary_code)
                    print("The box is blocked. A temporary code has been sent to your email.")
                    arduino.write(b"BLOCKED\n")

        elif mode == "blocked":
            print("Please say the temporary code:")
            arduino.write(b"ENTER_CODE\n")
            text = listen()
            code = clean_password(text)

            if code == temporary_code:
                print("The code is correct.")
                arduino.write(b"CODE_OK\n")
                mode = "new_password"
            else:
                print("The code is incorrect.")
                arduino.write(b"CODE_WRONG\n")

        elif mode == "new_password":
            print("Please create your new password (4 digits):")
            arduino.write(b"NEW_PASSWORD\n")
            text = listen()
            new_pass = clean_password(text)
            if new_pass is None:
                print("Invalid password.")
                arduino.write(b"ERROR\n")
                continue
            password = new_pass
            print("New password set:", password)
            attempts = 3
            mode = "normal"
            arduino.write(b"SAVED\n")

    except:
        print("I can't understand, please say again.")

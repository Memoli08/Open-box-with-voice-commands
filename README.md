# 🔐 Voice-Controlled Password Lock System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) 
![Arduino](https://img.shields.io/badge/Arduino-Connected-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A **voice-controlled password lock system** built with **Arduino** and **Python**.  
The system recognizes passwords via voice commands, verifies them, blocks access after multiple failed attempts, and sends an **email notification** with a temporary code if the password is blocked. Users can reset the password by entering the temporary code.

---

## ⚙️ Features

- 🎤 Voice recognition for 4-digit password input  
- ✅ Password verification  
- 🚫 Automatic blocking after 3 incorrect attempts  
- 📧 Email notification with a temporary code when blocked  
- 🔑 Reset password functionality using the temporary code  
- 💻 Works with Arduino hardware and Python scripts  

---

## 🛠 Installation

1. Install **Python 3.x** from [python.org](https://www.python.org/downloads/)  
2. Install required Python packages:

```bash
pip install pyttsx3 SpeechRecognition smtplib
Connect your Arduino board to your computer

Upload the Arduino code to the board

🚀 Usage
Run the Python script:

python main.py
Follow the voice prompts:

Normal mode: Say your 4-digit password.

Blocked mode: If your password is blocked, say the temporary code received via email.

New password mode: After entering the temporary code, create a new 4-digit password.

Voice commands for closing the box: You can say “close”, “lock”, or “shutdown” to trigger the box closing.

🧰 Hardware Requirements
Arduino board (e.g., Uno, Nano)

Microphone

Computer with Python installed

⚡ Configuration
Replace SENDER with your email address

Replace SENDERMAILPASSWORD with your email application password

Replace RECEIVER with the email address to receive temporary codes

Replace YOUR_PORT with the port your Arduino is connected to

arduino = serial.Serial("YOUR_PORT", 9600)
📝 Contributing
Contributions are welcome!

Open an issue for bugs or feature requests

Submit pull requests for improvements

📜 License
This project is licensed under the MIT License.
See the LICENSE file for details

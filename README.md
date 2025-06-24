Real-time Morse Code Translator
Overview
This Python script translates text input into Morse code in real-time, playing audio tones for each Morse code symbol (dot, dash, or gap). It uses the pynput library to capture keyboard input and the sounddevice library to generate and play audio tones. The script supports alphanumeric characters, some punctuation, and spaces, with Morse code output displayed on the console and played as audio.
Features

Real-time Translation: Converts typed text to Morse code instantly.
Audio Feedback: Plays distinct tones for dots (short) and dashes (long).
Interactive Input: Supports backspace to correct input, space for word separation, and Enter to display the full translation.
Exit Option: Press Esc to exit the program gracefully.
Test Audio: Includes a test sound to verify audio functionality on startup.

Prerequisites
To run this script, ensure you have the following installed:

Python 3.6 or higher
Required Python libraries:
pynput (for keyboard input)
sounddevice (for audio playback)
numpy (for generating audio tones)



Installation

Clone the Repository:
git clone https://github.com/Preeeeetham/Morsecode.git
cd Morsecode


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install pynput sounddevice numpy


Verify Audio Setup:Ensure your system has working audio output. The script includes a test sound on startup to confirm audio functionality.


Usage

Run the Script:
python morsecode.py


Instructions:

The script will play a 0.5-second test tone to verify audio.
Start typing any text (letters, numbers, or supported punctuation: ., ,, ?, !).
The console displays the input text and its Morse code translation in real-time.
Audio tones play for each valid character's Morse code:
Dot (.): Short tone (0.2 seconds).
Dash (-): Long tone (0.6 seconds).
Letter Gap: 0.2-second pause between letters.
Word Gap: 1.4-second pause for spaces.


Press Backspace to delete the last character.
Press Enter to display the full translation and continue typing.
Press Esc to exit the program.


Example Output:
Real-time Morse Code Translator
-------------------------------
Playing test sound...
Test sound completed. Did you hear it?
Type any text to translate it to Morse code.
Audio will play for each character.
Press ESC to exit.

hello | Morse: .... . .-.. .-.. --- 



Morse Code Dictionary
The script supports the following characters and their Morse code equivalents:

Letters: A-Z (e.g., A: .-, B: -..., Z: --..)
Numbers: 0-9 (e.g., 0: -----, 1: .----, 9: ----.)
Punctuation: . (.-.-.-), , (--..--), ? (..--..), ! (-.-.--)
Space: / (represents a word gap)

Notes

Audio Issues: If no sound plays, check your audio device and ensure sounddevice is properly installed. Run the script with a connected speaker or headphone.
Windows Users: If using Git Bash or WSL, ensure your audio drivers are compatible with sounddevice.
Case Insensitivity: Input is case-insensitive (converted to uppercase for Morse code).
Unsupported Characters: Characters not in the Morse code dictionary are ignored but displayed in the input text.

Troubleshooting

"No such file or directory" when cloning: Verify the repository URL (https://github.com/Preeeeetham/Morsecode.git) and your GitHub credentials.
No audio output: Ensure numpy and sounddevice are installed, and test your audio device with the initial test sound.
Keyboard input issues: Ensure pynput is installed and that you have permission to capture keyboard events (may require running as administrator on some systems).
Dependency errors: Run pip install pynput sounddevice numpy again or check for compatible versions with your Python installation.

Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Suggestions for new features (e.g., additional symbols, customizable tone frequency) are welcome!
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For issues or suggestions, contact the repository owner at levakupreetham@gmail.com or open an issue on GitHub.

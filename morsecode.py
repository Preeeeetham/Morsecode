import sys
import time
import threading
import queue
from pynput import keyboard
import numpy as np
import sounddevice as sd

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    ' ': '/' 
}

input_queue = queue.Queue()
exit_flag = False

DOT_DURATION = 0.2  
DASH_DURATION = DOT_DURATION * 3
ELEMENT_GAP = DOT_DURATION  
LETTER_GAP = DOT_DURATION * 3  
WORD_GAP = DOT_DURATION * 7  
FREQUENCY = 1000  
SAMPLE_RATE = 44100  

def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
    return ' '.join(morse)

def generate_tone(duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    return 1.0 * np.sin(2 * np.pi * FREQUENCY * t)

def play_morse_sound(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            tone = generate_tone(DOT_DURATION)
            sd.play(tone, SAMPLE_RATE)
            sd.wait()
        elif symbol == '-':
            tone = generate_tone(DASH_DURATION)
            sd.play(tone, SAMPLE_RATE)
            sd.wait()
        elif symbol == ' ':
            time.sleep(LETTER_GAP)
        elif symbol == '/':
            time.sleep(WORD_GAP)
        if symbol in ['.', '-']:
            time.sleep(ELEMENT_GAP)

def on_press(key):
    try:
        char = key.char
        input_queue.put(char)
    except AttributeError:
        if key == keyboard.Key.space:
            input_queue.put(' ')
        elif key == keyboard.Key.backspace:
            input_queue.put('\b') 
        elif key == keyboard.Key.enter:
            input_queue.put('\n')
        elif key == keyboard.Key.esc:
            global exit_flag
            exit_flag = True
            return False

def input_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
def test_audio():
    """Play a test sound to check if audio is working"""
    print("Playing test sound...")
    tone = generate_tone(0.5)
    sd.play(tone, SAMPLE_RATE)
    sd.wait()
    print("Test sound completed. Did you hear it?")

def main():
    """Main function to process input and translate to Morse code"""
    print("Real-time Morse Code Translator")
    print("-------------------------------")
    test_audio()
    
    print("Type any text to translate it to Morse code.")
    print("Audio will play for each character.")
    print("Press ESC to exit.")
    print()
    input_thread = threading.Thread(target=input_listener)
    input_thread.daemon = True
    input_thread.start()
    
    current_text = ""
    morse_text = ""
    
    while not exit_flag:
        try:
            try:
                char = input_queue.get(timeout=0.1)
            except queue.Empty:
                continue
            if char == '\b':  
                if current_text:
                    current_text = current_text[:-1]
                    morse_text = text_to_morse(current_text)
            elif char == '\n':
                current_text += '\n'
                morse_text = text_to_morse(current_text)
                print('\nTranslation:', morse_text)
            else:
                current_text += char
                char_morse = text_to_morse(char.upper())
                morse_text = text_to_morse(current_text)
                sys.stdout.write('\r' + current_text + ' | Morse: ' + morse_text + ' ')
                sys.stdout.flush()
                if char in MORSE_CODE_DICT:
                    play_morse_sound(MORSE_CODE_DICT[char.upper()])
                
        except KeyboardInterrupt:
            break
    
    print("\nExiting...")

if __name__ == "__main__":
    main()
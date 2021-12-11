# Convert text to Morse:
# Users enter a string. e.g: hello world.
# Turn all characters into lowercase.
# Strip all trailing spaces.
# Conver each character into their corresponding morse code.
# Each character is separated by space. Each word is separated by "|".
# e.g, "hello world" can be converted to:
# .... . .-.. .-.. --- | .-- --- .-. .-.. -..
import PySimpleGUI as sg


def to_morse(text: str) -> str:
    """
    ### Conversion steps:
    1. Turn all characters in `text` to lowercase and strip all trailing spaces.
    2. Convert processed `text` into morse code.
    3. Return morse code represents each character in the input `text`. Each word is
    seperated by `|`.
    """
    morse_dict = {
        " ": "|",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        "?": "..--..",
        "!": "-.-.--",
        ".": ".-.-.-",
        ",": "--..--",
        ";": "-.-.-.",
        ":": "---...",
        "+": ".-.-.",
        "-": "-....-",
        "/": "-..-.",
        "=": "-...-",
    }

    text = text.lower().strip()

    word_list = [morse_dict[char] for char in text]

    morse_string = "  ".join(word_list)

    return morse_string


row1 = [sg.Text("Enter your text below:")]
row2 = [sg.Input(key="-INPUT-", do_not_clear=False)]
row3 = [sg.Button("To Morse"), sg.Cancel()]


layout = [
    [
        sg.Frame(
            "Welcome to Text to Morse Converter",
            [row1, row2, row3],
            title_location="n",
        )
    ]
]

window = sg.Window("Text to Morse Converter", layout, font=("Arial", 22, "bold"))

while True:
    event, values = window.read()
    print(event, values)

    if event == "Cancel" or event == sg.WINDOW_CLOSED:
        break
    else:
        morse_string = to_morse(values["-INPUT-"])

        sg.popup(
            morse_string,
            title="Morse code generated from your input",
            font=(
                "Arial",
                22,
                "bold",
            ),
        )

window.close()

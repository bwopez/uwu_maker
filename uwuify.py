import pyperclip

def uwuify(texty_wexty):
    texty_wexty = texty_wexty.lower()
    # texty_wexty = texty_wexty.replace("oh", "owo")
    texty_wexty = texty_wexty.replace("s", "sh")
    texty_wexty = texty_wexty.replace("r", "w")
    texty_wexty = texty_wexty.replace("l", "w")
    texty_wexty = texty_wexty.replace("you", "u")
    texty_wexty = texty_wexty.replace("uck", "ucky wucky")
    return texty_wexty


if __name__ == "__main__":
    # paste contents of clipboard to text variable
    text = pyperclip.paste()

    # edit text variable
    uwu_text = uwuify(text)
    pyperclip.copy(uwu_text)

    # copy text variable back to clipboard
    print(pyperclip.paste())

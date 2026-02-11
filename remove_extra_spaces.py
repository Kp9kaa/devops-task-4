# remove_extra_spaces.py
def clean_spaces(text):
    if not isinstance(text, str):
        return ""
    return " ".join(text.split())

if __name__ == "__main__":
    print(clean_spaces("  Test    string  "))

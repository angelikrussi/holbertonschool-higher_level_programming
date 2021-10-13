#!/usr/bin/python3
"""the write_file function """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return(f.write(text))

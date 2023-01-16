#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_list = dir(hidden_4)
    for names in names_list:
        if (names[:2] != '__'):
            print(names)

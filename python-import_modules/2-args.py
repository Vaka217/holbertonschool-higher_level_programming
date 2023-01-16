#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args == 1:
        print("{} arguments.".format(args - 1))
    elif args == 2:
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

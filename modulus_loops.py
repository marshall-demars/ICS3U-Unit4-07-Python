#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program lists every number from 1000 to 2000

def main():
    # This program lists every number from 1000 to 2000

    counter = 0

    # Process and Output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("")
            print(counter, end=" ")
        else:
            print("{0} ".format(counter), end="")

    print("\nDone.")


if __name__ == "__main__":
    main()

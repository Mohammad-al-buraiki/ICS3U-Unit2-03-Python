#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program calculates the circumference of a circle

import constants


def main():
    # this function calculates the circumference of a circle

    # input
    radius = input("Enter the radius a circle (cm):")

    # process
    circumference = constants.τ*(int(radius))

    # output
    print("The circumference of a circle with radius {0} cm is {1} cm."
          .format(radius, circumference))


if __name__ == "__main__":
    main()

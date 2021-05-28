#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program calculates the volume of a cylinder

import string
import math


def calculate_volume(radius, height):
    # Gets volume

    # Process and output
    volume = math.pi * radius ** 2 * height

    return volume


def main():
    # This function calls calculate_volume

    # Input
    radius_input = str(input("Enter the radius of a cylinder (cm): "))
    height_input = str(input("Enter height (cm): "))

    # Process and output
    try:
        radius_as_float = float(radius_input)
        height_as_float = float(height_input)
        cylinder_volume = calculate_volume(radius_as_float, height_as_float)
        if cylinder_volume > 0:
            print(
                "The volume of the cylinder is {} cm³.".format(cylinder_volume)
            )
        else:
            print("Invalid dimensions")
    except Exception:
        print("Invalid dimensions")
    print("\nDone.")


if __name__ == "__main__":
    main()

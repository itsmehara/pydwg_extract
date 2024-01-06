"""
File: main.py
Description: creating objects in dwg file / extraction of objects from dwg files.
Author: Its Me Hara
Date: Jan 05, 2024
Notes:
    This file is entry point for the entire project..
"""
import sys
from autocad.extractor import extract_parameters
from autocad.dwg_creator import DWGCreator


def create_main(dwg_file):
    creator = DWGCreator()

    # Create a circle
    creator.create_circle(center=(2, 2), radius=1)

    # Create a line
    creator.create_line(start_point=(0, 0), end_point=(1, 1))

    # Create a chair
    creator.create_chair(insertion_point=(4, 0))

    # Save the DWG file
    creator.save_dwg(dwg_file)


def read_main(default_dwg=None):
    # Extract command-line parameters or handle input
    file_path = sys.argv[1] if len(sys.argv) > 1 else default_dwg

    # Call the extractor function
    extract_parameters(file_path)


if __name__ == "__main__":
    dwg_file = "dwg_files/NS_A_102_103-RCP LAYOUT.dwg"
    # create_main(dwg_file)
    read_main(dwg_file)

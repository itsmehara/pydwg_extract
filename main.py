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
# from ezdxfgrabber import readfile # not worked
# from dxfgrabber import DXFGrabber
import ezdxf

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


def verify_dxf(dwg_file):
    # Read the DXF file
    dxf = DXFGrabber(dwg_file)

    # Print information about each entity in the DXF file
    for entity in dxf.entities:
        print(f"Entity Type: {entity.dxftype} | Layer: {entity.layer} | Color: {entity.color}")


def read_dwg_elements(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    for entity in msp.query('*'):  # You can specify entity types or conditions here
        print(f"Type: {entity.dxftype()}, Layer: {entity.dxf.layer}")


def verify_binary_dxf(dwg_file):
    from ezdxf.lldxf.validator import is_dxf_file, is_binary_dxf_file
    print(f"given dwg file:{dwg_file} is dxf : {is_binary_dxf_file(dwg_file)}")
    print(f"given dwg file:{dwg_file} is dxf : {is_dxf_file(dwg_file)}")


if __name__ == "__main__":
    dwg_file100 = "logs/NS_A_100-INTERIOR LAYOUT.dwg"
    dwg_file101 = "logs/NS_A_101-PARTITION MARKING.dwg"
    dwg_file102 = "logs/NS_A_102_103-RCP LAYOUT.dwg"
    dwg_file103 = "logs/HR_A_100_INTERIOR_LAYOUT R7.dxf"
    dwg_file104 = "dwg_files/default.dwg"
    dwg_file105 = "dwg_files/blocks_and_tables.dwf"
    # create_main(dwg_file)
    read_main(dwg_file103)
    # verify_dxf(dwg_file)
    # read_dwg_elements(dwg_file103)
    # verify_binary_dxf(dwg_file100)
    # verify_binary_dxf(dwg_file101)
    # verify_binary_dxf(dwg_file102)
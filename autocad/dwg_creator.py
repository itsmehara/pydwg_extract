"""
File: dwg_creator.py
Description: DWGCreator class for creating circles, lines, and chairs in a DWG file.
Author: Its Me Hara
Date: Jan 05, 2024
Notes:
    This file contains the DWGCreator class with methods to create various geometric entities.
"""
import ezdxf
from utils.logger_utils import get_logger

log = get_logger()

class DWGCreator:
    def __init__(self):
        self.doc = ezdxf.new("R2010")
        self.msp = self.doc.modelspace()

    def create_circle(self, center, radius):
        self.msp.add_circle(center=center, radius=radius)

    def create_line(self, start_point, end_point):
        self.msp.add_line(start=start_point, end=end_point)

    def create_chair(self, insertion_point):
        log.info("Creating chair")
        chair_block = self.doc.blocks.new(name='Chair')
        chair_block.add_lwpolyline(points=[(0, 0), (1, 0), (1, 0.5), (0.5, 1), (0, 0.5)], close=True)

        self.msp.add_blockref('Chair', insert=insertion_point)

    def save_dwg(self, file_path):
        self.doc.saveas(file_path)
        log.info(f"dwg file saved to {file_path}")


if __name__ == "__main__":
    creator = DWGCreator()

    # Create a circle
    creator.create_circle(center=(2, 2), radius=1)

    # Create a line
    creator.create_line(start_point=(0, 0), end_point=(1, 1))

    # Create a chair
    creator.create_chair(insertion_point=(4, 0))

    # Save the DWG file
    creator.save_dwg("dwg_files/output.dwg")

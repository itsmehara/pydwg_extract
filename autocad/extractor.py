"""
File: extractor.py
Description: Extracts the attributes if the dwg file is dxf format.
Author: Its Me Hara
Date: Jan 05, 2024
Notes:
    This file contains the implementation of extracting dxf format dwg file. usually dwg file is autocad dwg file.
"""
import ezdxf
from utils.logger_utils import get_logger

log = get_logger()


def extract_parameters(file_path):
    try:
        # Logic for extracting parameters from AutoCAD DWG files
        doc = ezdxf.readfile(file_path)

        # Sample: Extract and log layers
        for layer in doc.layers:
            log.info("Layer Name: %s", layer.dxf.name)

        # Add more extraction logic based on your project's requirements

    except Exception as e:
        log.error("Error extracting parameters: %s", str(e))

"""
File: logger_utils.py
Description: Logging module.
Author: Its Me Hara
Date: Jan 05, 2024
Notes:
    This file contains the logging related methods to generate log file.
"""
import logging
import os

LOG_FORMAT = "%(asctime)s:%(levelname)s %(filename)s %(lineno)d: %(message)s"


def get_logger():
    logger_name = "pydwg_extract"
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter(LOG_FORMAT)

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        logger.addHandler(ch)

        # Optionally, add a file handler for logging to a file
        log_file_path = os.path.join("logs", "autocad_extractor.log")
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

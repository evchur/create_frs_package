#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- IMPORTANT: You have to add all your functions here:
__all__ = [
    'setup_custom_logger',
]

"""
Program description:
    

Program contains functions:
    a.
    b.
    c.

Program autors: Evgenii Churiulin (evgenii.churiulin@kit.edu), Hendrik Feldmann,
                Patrik Ludwig, Cusinato, Eleonora and Joaquim Pinto
                
Acknowledgements:
    a.
    b.
    
    
Current Code Owner: Karlsruhe Institute of Technology (KIT)
                    Institute of Meteorology and Climate Research (IMK)
                    Department Troposphere Research (IMK-TRO)

Contact information:
    Evgenii Churiulin
    E-mail: evgenii.churiulin@kit.edu
    Phone: +49 721 608 23277
    Address: Hermann-von-Helmholtz-Platz 1
             Building 435, Room 502
             76344 Eggenstein-Leopoldshafen, Germany
    
History:
Version    Date       Name
---------- ---------- ----
   1.1     Tue Sep 10 11:46:57 2024   Evgenii Churiulin, IMKTRO
                      Initial realise 
"""
# test_logger.py
import logging
import sys

def setup_custom_logger(name, filename=None):

    logger = logging.getLogger(name)

    # Clear existing handlers to avoid duplicate log entries
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)  # Set the minimum log level
    
    # File handler
    if filename:
        handlerFile = logging.FileHandler(filename, mode='w', encoding=None, delay=False)
        formatter_file = logging.Formatter("%(asctime)s - %(levelname)-6s - %(message)s")
        handlerFile.setFormatter(formatter_file)
        handlerFile.setLevel(logging.DEBUG)  # Ensure file captures all levels

        logger.addHandler(handlerFile)

    # Console handler
    handlerStdout = logging.StreamHandler(sys.stdout)
    formatter_stdout = logging.Formatter("\n %(message)s")
    handlerStdout.setFormatter(formatter_stdout)
    # Set to CRITICAL (or higher) to suppress non-critical messages in console
    handlerStdout.setLevel(logging.CRITICAL)  

    logger.addHandler(handlerStdout)

    return logger

# Set up the logger once at the module level
#logger = setup_custom_logger('root', 'test_logger.txt')
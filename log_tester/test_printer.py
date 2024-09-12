#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__all__ = [
    'Printer',
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
   1.1     Tue Sep 10 11:49:30 2024   Evgenii Churiulin, IMKTRO
                      Initial realise 
"""

import logging

class Printer:
    def __init__(self):
        self.logger = logging.getLogger('root')  # Use the existing logger setup
        self.logger.info(f"Initializing Printer")
        
    def print_my_data(self, text: str):
        if isinstance(text, str) and len(text) > 0:
            self.logger.info('Text was printed')
        else:
            self.logger.error('There is no available text for printing')
            self.logger.debug(f'Text variable is "{text}"')
            
        
    
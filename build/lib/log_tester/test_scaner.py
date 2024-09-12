#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = [
    'Scaner',
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
   1.1     Tue Sep 10 11:49:53 2024   Evgenii Churiulin, IMKTRO
                      Initial realise 
"""
import logging

class Scaner:
    def __init__(self):
        self.logger =  logging.getLogger('root')
        self.logger.info(f"Initializing Scaner")
        
    def scan_my_data(self, text:str):
        print(text)
        if isinstance(text, str) and len(text) > 0:
            self.logger.info('Text was scanned')
        else:
            self.logger.error('There is no available text for scanning')
            self.logger.debug(f'Text variable is "{text}"')
            #raise ValueError('Text variable is incorrect')
        
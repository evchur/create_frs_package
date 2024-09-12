#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
   1.1     Tue Sep 10 11:49:08 2024   Evgenii Churiulin, IMKTRO
                      Initial realise 
"""

"""
import test_printer
import test_scaner
from test_logger import setup_custom_logger


class Get_my_docs:
    def __init__(self, lprinter:bool, lscaner:bool):
        self.printer = lprinter
        self.scaner = lscaner
        self.logger = setup_custom_logger('root', 'test_logger.txt')
        
    def main(self, text:str):
        if self.printer and not self.scaner:
            self.logger.info('Go print')
            pr_object = test_printer.Printer()
            pr_object.print_my_data(text)
            self.logger.info('Print is done')
        elif self.scaner and not self.printer:
            self.logger.info('Go scan')
            sc_object = test_scaner.Scaner()
            sc_object.scan_my_data(text)
            self.logger.info('Scan is done')

        elif self.printer and self.scaner:
            self.logger.info('I printed and scaned my data')
            pr_object = test_printer.Printer()
            sc_object = test_scaner.Scaner()
            pr_object.print_my_data(text)
            sc_object.scan_my_data(text)
            
        else:
            self.logger.debug('No manipilations with data')
            
if __name__ == '__main__':
    gmd = Get_my_docs(True, True)
    gmd.main(text = '')
"""

from log_tester import (
    setup_custom_logger,
    test_printer,
    test_scaner,
)

import logging


# Class using the already configured logger
class Get_my_docs:
    def __init__(self, lprinter: bool, lscaner: bool, logger: logging.Logger):
        self.printer = lprinter
        self.scaner = lscaner
        self.logger = logger  # Use the logger configured globally
        
    def main(self, text: str):
        if self.printer and not self.scaner:
            self.logger.info('Go print')
            pr_object = test_printer.Printer()
            pr_object.print_my_data(text)
            self.logger.info('Print is done')
        elif self.scaner and not self.printer:
            self.logger.info('Go scan')
            sc_object = test_scaner.Scaner()
            sc_object.scan_my_data(text)
            self.logger.info('Scan is done')
        elif self.printer and self.scaner:
            self.logger.info('I printed and scanned my data')
            pr_object = test_printer.Printer()
            sc_object = test_scaner.Scaner()
            pr_object.print_my_data(text)
            sc_object.scan_my_data(text)
        else:
            self.logger.debug('No manipulations with data')

if __name__ == '__main__':
    logger = setup_custom_logger('root', 'test_logger.txt')
    
    gmd = Get_my_docs(True, True, logger)
    gmd.main(text='a')            

            
            
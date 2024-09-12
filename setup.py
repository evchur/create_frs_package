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
   1.1     Wed Sep 11 10:24:56 2024   Evgenii Churiulin, IMKTRO
                      Initial realise 
"""

from setuptools import find_packages, setup


with open("log_tester/Readme.md", "r") as f:
    long_description = f.read()
    
setup(
    name="log_tester",
    version="0.0.1",
    description="simple example for testing user logger",
    packages=["log_tester"],  # No need to specify package_dir
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author_email="evgenii.churiulin@kit.edu",
    license="LICENSE",
    classifiers=[
        "License :: OSI Approved :: GNU License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)

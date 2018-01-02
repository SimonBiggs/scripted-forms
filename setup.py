LICENCE_HEADER = """scriptedforms
Copyright (C) 2017 Simon Biggs

Licensed under both the Apache License, Version 2.0 (the "Apache-2.0") and 
GNU Affrero General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later 
version (the "AGPL-3.0+").

You may not use this module except in compliance with both the Apache-2.0 AND 
the AGPL-3.0+ in combination (the "Combined Licenses").

You may obtain a copy of the AGPL-3.0+ at

    https://www.gnu.org/licenses/agpl-3.0.txt

You may obtain a copy of the Apache-2.0 at 

    https://www.apache.org/licenses/LICENSE-2.0.html

Unless required by applicable law or agreed to in writing, software
distributed under the Combined Licenses is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See 
the Combined Licenses for the specific language governing permissions and 
limitations under the Combined Licenses."""


import os
from setuptools import setup

setup(
    name="scriptedforms",
    version="0.1.1",
    author="Simon Biggs",
    author_email="mail@simonbiggs.net",
    description="Open a scripted form",
    long_description=(
        ""
    ),
    keywords=[],
    packages=[
        "scriptedforms"
    ],
    entry_points={
        'console_scripts': [
            'scriptedforms=scriptedforms:main',
        ],
    },
    license='AGPL-3.0+ AND Apache-2.0',
    install_requires=[
        'notebook',
        'numpy',
        'pandas',
        'watchdog',
        'jinja2',
        'matplotlib'
    ],
    classifiers = [],
    url = "http://scriptedforms.com.au",
    include_package_data=True
)
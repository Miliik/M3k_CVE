# M3k-cve

This project is a Python script that searches for CVEs in the NVD database. The script can be used to search for CVEs by keyword, product, version, or vendor. The user can also search for a CVE by ID. The results are stored in a file in .md format. The script can be used in the command line or in a Python script.

## Installation

### Prerequisites

The script is written in Python 3. It requires the following packages to be installed:

- requests
- json
- argparse
- datetime
- time
- sys
- os

### Installation

To install the script, clone the repository in your local directory:

```git clone https://github.com/your_username/M3k-cve.git```



Then navigate to the project directory and install the required packages using pip:

```
cd M3k-cve
pip install -r requirements.txt
```


Alternatively, you can install the script directly using pip:

```pip install git+https://github.com/your_username/M3k-cve.git```



## Usage

To use the script, run the `cve.py` file from the command line with the appropriate options. Here are the available options:

usage: cve.py [-h] [-k KEYWORD] [-p PRODUCT] [-v VERSION] [-d VENDOR] [-i ID] [-o OUTPUT]

optional arguments:
-h, --help show this help message and exit

-w KEYWORD, --keyword KEYWORD Search for CVEs by keyword

-p PRODUCT, --product PRODUCT Search for CVEs by product

-v VERSION, --version VERSION Search for CVEs by version

-V VENDOR, --vendor VENDOR Search for CVEs by vendor
 
-o OUTPUT, --output OUTPUT if you want to save the results in a file


Here are some examples of how to use the script:
```
python3 M3k-cve.py -k 'SQL injection'

python3 M3k-cve.py -p 'WordPress' -v '4.5'

python3 M3k-cve.py -V 'Microsoft' -o
```



## Contributing

If you wish to contribute to the project, please follow these steps:

1. Fork the repository
2. Clone your forked repository to your local machine
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request to the original repository

Please ensure that your code follows the PEP8 style guide and includes appropriate tests.
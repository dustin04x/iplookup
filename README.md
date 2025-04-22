# IP Lookup Tool

A simple Python script that retrieves geographical and other information about an IP address using the ipinfo.io API.

## Features

- Command-line interface
- Retrieves detailed IP information including:
  - IP Address
  - Hostname
  - City
  - Region
  - Country
  - Location (latitude/longitude)
  - Organization
  - Postal Code
  - Timezone
- Error handling for various scenarios

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dustin04x/iplookup.git
cd iplookup
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with an IP address as an argument:

```bash
python3 main.py 8.8.8.8
```

## Requirements

- Python 3.x
- requests library (version 2.31.0)

## License

This project is open source and available under the MIT License. 

# Proportional Demographic Selection

## Overview
This repository contains a Python implementation of **Proportional Demographic Selection (PDS)**—a selection algorithm that ensures a legislative body reflects the demographic makeup of a population. The system balances representation dynamically based on census-aligned demographic categories such as **sex, age, family status, and income**.

## Features
- **Synthetic Population Generation**: Creates a simulated population dataset with predefined demographic distributions.
- **Proportional Ranking Algorithm**: Adjusts selection weights dynamically to ensure demographic balance.
- **Randomized Selection Layer**: Prevents deterministic bias while maintaining proportionality.
- **Database Schema (MariaDB/PostgreSQL)**: Defines a structured format for storing population and selection data.
- **Fully Open Source (Unlicense)**: Free for any use with optional attribution.

## Installation
```sh
# Clone the repository
git clone https://github.com/YOUR-USERNAME/proportional-demographic-selection.git
cd proportional-demographic-selection

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
Run the main script to perform a selection based on a synthetic population:
```sh
python select_legislators.py
```

## Database Setup
The system supports **MariaDB** and **PostgreSQL**. To set up the database:
```sh
# Run schema setup (modify for PostgreSQL as needed)
mysql -u user -p < schema.sql
```

## License
This project is released under the **Unlicense**, allowing unrestricted use. Attribution is appreciated but not required.

## Credits
This project was developed by ChatGPT in collaboration with John I. Mackay as part of the Colocracy initiative.

## Contributing
Pull requests and discussions are welcome! If you’d like to suggest improvements, feel free to open an issue.

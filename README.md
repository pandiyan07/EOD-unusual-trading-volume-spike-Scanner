# Project Title

**EOD Volume Anomaly Scanner**

Built on - June 2024

## Table of Contents

-   About The Project
-   Built With
-   Key Features
-   Getting Started
-   Technologies Used (Prerequisites)
-   Installation
-   Usage
-   Project Structure
-   How It Works
-   Main Python Functions
-   Future Improvements
-   License Description
-   Disclaimer

## About The Project

This project scans end-of-day (EOD) trading volumes for multiple NSE
stocks and identifies abnormal volume spikes by comparing each trading
day's volume against its weekly and monthly average volume. Historical
OHLCV data is downloaded from Yahoo Finance and processed to highlight
unusually high trading activity that may indicate institutional
participation or important market events.

### Built With

-   Python 3
-   yfinance
-   Standard Library

### Key Features

-   Download historical EOD volume data from Yahoo Finance.
-   Analyze multiple NSE stocks.
-   Weekly abnormal volume detection.
-   Monthly abnormal volume detection.
-   Prints stocks whose daily volume exceeds 2× the average period
    volume.
-   Modular analysis functions.

## Getting Started

### Technologies Used (Prerequisites)

-   Python 3.9+
-   pip
-   Internet connection

### Installation

``` bash
git clone https://github.com/pandiyan07/EOD-unusual-trading-volume-spike-Scanner.git
cd EOD-unusual-trading-volume-spike-Scanner
pip install yfinance
python "EOD volume.py"
```

## Usage

``` python
eqList=["INFY.NS","ITC.NS","TCS.NS"]
```

Run the script to download one month of daily data and display
weekly/monthly abnormal volume alerts.

## Project Structure

``` text
EOD volume.py
│
├── eqList                     # List of NSE stocks
├── DATA_FETCHER()             # Downloads historical data
├── OUTPUT_CALCULATOR()        # Prints abnormal volume results
├── ABNORMAL_VOLUME_FINDER()   # Core anomaly detection logic
├── WEEKLY_AVERAGE()           # Weekly analysis
├── MONTHLY_AVERAGE()          # Monthly analysis
└── Main Program               # Processes every stock
```

## How It Works

1.  Read stock symbols.
2.  Download one month of daily volume data.
3.  Store date-volume pairs.
4.  Calculate weekly average volume.
5.  Flag days with volume \>2× weekly average.
6.  Calculate monthly average volume.
7.  Flag days with volume \>2× monthly average.
8.  Print abnormal volume report for each stock.

## Main Python Functions

  -----------------------------------------------------------------------
  Function                            Description
  ----------------------------------- -----------------------------------
  DATA_FETCHER()                      Downloads historical EOD data from
                                      Yahoo Finance.

  OUTPUT_CALCULATOR()                 Formats and prints detected
                                      abnormal volume events.

  ABNORMAL_VOLUME_FINDER()            Calculates averages and detects
                                      abnormal volume.

  WEEKLY_AVERAGE()                    Performs weekly volume analysis.

  MONTHLY_AVERAGE()                   Performs monthly volume analysis.
  -----------------------------------------------------------------------

## Future Improvements

-   Export reports to Excel/CSV.
-   Relative volume (RVOL) calculation.
-   Configurable anomaly threshold.
-   CLI arguments.
-   Plotly/Matplotlib charts.

## License Description

Recommended: MIT License.

## Disclaimer

For educational and research purposes only. This tool is not financial
advice.

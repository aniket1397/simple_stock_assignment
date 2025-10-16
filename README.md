# Super Simple Stock Market

This project implements the core object model for the Global Beverage Corporation Exchange (GBCE) in Python

## Structure
- `stock_market/` - Library containing core classes:
	- `trade.py` - Trade record class
	- `stock.py` - Stock class with calculations
	- `market.py` - StockMarket class for GBCE index
- `main.py` - Example usage and entry point

## Features
- Calculate dividend yield and P/E ratio for any stock and price
- Record trades with timestamp, quantity, indicator, and price
- Calculate Volume Weighted Stock Price (volume_weighted_stock_price) for trades in last 5 minutes
- Compute GBCE All Share Index (geometric mean of volume_weighted_stock_price)

## Usage
Run the example:
```bash
python main.py
```

# simple_stock_assignment
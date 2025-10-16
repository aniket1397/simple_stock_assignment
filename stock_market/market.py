import logging
from math import prod
from .stock import Stock, StockType
from math import prod
from .stock import Stock

class StockMarket:
    def __init__(self):
        self.stocks = {}
        logging.info("StockMarket created.")

    def add_stock(self, stock: Stock):
        """
         Add a stock to the market."""
        self.stocks[stock.stock_symbol] = stock
        logging.info(f"Adding stock {stock.stock_symbol} to market.")

    def gbce_all_share_index(self) -> float:
        """
         Calculate the GBCE All Share Index using the geometric mean of Volume Weighted Stock Prices for all stocks.
         Returns 0 if there are no stocks or no valid VWSPs.
        """
        vw_list = []
        for stock in self.stocks.values():
            vwsp = stock.volume_weighted_stock_price()
            if vwsp > 0:
                vw_list.append(vwsp)
        if not vw_list:
            logging.info("No valid VWSPs to calculate GBCE All Share Index.")
            return 0
        logging.info("Calculating GBCE All Share Index.")
        return prod(vw_list) ** (1 / len(vw_list))

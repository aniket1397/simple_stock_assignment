from datetime import datetime, timedelta
import logging
from enum import Enum
from .trade import Trade, TradeIndicator


class StockType(Enum):
    COMMON = 'Common'
    PREFERRED = 'Preferred'

class Stock:
    def __init__(self, stock_symbol: str, type_: StockType, last_dividend: int, par_value: int, fixed_dividend: float = None):
        self.stock_symbol = stock_symbol
        self.type_ = type_  # StockType Enum
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.fixed_dividend = fixed_dividend  # as a decimal, e.g., 0.02 for 2%
        self.trades = []
        logging.info(f"Created Stock: {self.stock_symbol}, Type: {self.type_.value}, Last Dividend: {self.last_dividend}, Par Value: {self.par_value}, Fixed Dividend: {self.fixed_dividend}")

    def dividend_yield(self, price: float) -> float:
        """
         Calculate the Dividend Yield.
         For Common Stock: Dividend Yield = Last Dividend / Price
         For Preferred Stock: Dividend Yield = (Fixed Dividend * Par Value) / Price
        """
        if price <= 0:
            logging.error("Price must be positive to calculate dividend yield.")
            raise ValueError("Price must be positive")
        logging.info(f"Calculating dividend yield for {self.stock_symbol} at price {price}")
        if self.type_ == StockType.COMMON:
            return self.last_dividend / price
        elif self.type_ == StockType.PREFERRED:
            return (self.fixed_dividend * self.par_value) / price
        else:
            logging.error(f"Unknown stock type {self.type_} for {self.stock_symbol}")
            raise ValueError("Unknown stock type")

    def pe_ratio(self, price: float) -> float:
        """
         Calculate the P/E Ratio.
         P/E Ratio = Price / Dividend
         Returns float('inf') if dividend is zero.
        """
        dividend = self.last_dividend if self.type_ == StockType.COMMON else self.fixed_dividend * self.par_value
        if dividend == 0:
            logging.info(f"P/E ratio is infinite for {self.stock_symbol} as dividend is zero.")
            return float('inf')
        logging.info(f"Calculating P/E ratio for {self.stock_symbol} at price {price}")
        return price / dividend

    def record_trade(self, quantity: int, indicator: TradeIndicator, price: float):
        """
         Record a trade with the given quantity, indicator (buy/sell), and price.
         Raises ValueError if quantity or price are non-positive."""
        if quantity <= 0:
            logging.error("Quantity must be greater than zero.")
            raise ValueError("Quantity must be greater than zero")
        if price <= 0:
            logging.error("Price must be greater than zero.")
            raise ValueError("Price must be greater than zero")
        trade = Trade(datetime.now(), quantity, indicator, price)
        self.trades.append(trade)
        logging.info(f"Recording trade for {self.stock_symbol}: {quantity} shares, {indicator.value}, price {price}")

    def volume_weighted_stock_price(self) -> float:
        """
         Calculate the Volume Weighted Stock Price (VWSP) based on trades in the last 5 minutes.
         VWSP = Sum(Trade Price * Quantity) / Sum(Quantity) for trades in the last 5 minutes
         Returns 0 if there are no trades in the last 5 minutes.
        """
        now = datetime.now()
        five_minutes_ago = now - timedelta(minutes=5)
        recent_trades = [t for t in self.trades if t.timestamp >= five_minutes_ago]
        total_quantity = sum(t.quantity for t in recent_trades)
        if total_quantity == 0:
            return 0
        logging.info(f"Calculating volume_weighted_stock_price for {self.stock_symbol}")
        total_trade_price = sum(t.price * t.quantity for t in recent_trades)
        return total_trade_price / total_quantity

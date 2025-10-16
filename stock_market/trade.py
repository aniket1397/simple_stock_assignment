import logging
from datetime import datetime
from enum import Enum
import uuid

class TradeIndicator(Enum):
    BUY = 'buy'
    SELL = 'sell'

class Trade:
    def __init__(self, timestamp: datetime, quantity: int, indicator: TradeIndicator, price: float):
        self.id = uuid.uuid4()
        self.timestamp = timestamp
        self.quantity = quantity
        self.indicator = indicator  # TradeIndicator Enum
        self.price = price
        logging.info(f"Trade recorded: {quantity} shares, {indicator.value}, price {price}, time {timestamp}")

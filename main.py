import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s %(levelname)s: %(message)s'
)
from stock_market.stock import Stock, StockType
from stock_market.market import StockMarket
from stock_market.trade import TradeIndicator

if __name__ == "__main__":
    try:
        logging.info("Starting Super Simple Stock Market application.")
        market = StockMarket()

        # Add stocks
        market.add_stock(Stock('TEA', StockType.COMMON, 0, 100))
        market.add_stock(Stock('TEA', StockType.COMMON, 0, 100))

        market.add_stock(Stock('POP', StockType.COMMON, 8, 100))
        market.add_stock(Stock('ALE', StockType.COMMON, 23, 60))
        market.add_stock(Stock('GIN', StockType.PREFERRED, 8, 100, fixed_dividend=0.02))
        market.add_stock(Stock('JOE', StockType.COMMON, 13, 250))
        logging.info("Stocks added to the market.")

        # Example: record trades and calculate metrics
        # Trades for POP
        stock_pop = market.stocks['POP']
        stock_pop.record_trade(100, TradeIndicator.BUY, 120)
        stock_pop.record_trade(50, TradeIndicator.SELL, 121)
        # Trades for TEA
        stock_tea = market.stocks['TEA']
        stock_tea.record_trade(200, TradeIndicator.BUY, 99)
        stock_tea.record_trade(80, TradeIndicator.SELL, 101)
        # Trades for ALE
        stock_ale = market.stocks['ALE']
        stock_ale.record_trade(150, TradeIndicator.BUY, 60)
        stock_ale.record_trade(60, TradeIndicator.SELL, 62)
        # Trades for GIN
        stock_gin = market.stocks['GIN']
        stock_gin.record_trade(120, TradeIndicator.BUY, 100)
        stock_gin.record_trade(40, TradeIndicator.SELL, 102)
        # Trades for JOE
        stock_joe = market.stocks['JOE']
        stock_joe.record_trade(90, TradeIndicator.BUY, 250)
        stock_joe.record_trade(30, TradeIndicator.SELL, 252)

        # Log metrics for POP
        logging.info(f"Dividend Yield (POP): {stock_pop.dividend_yield(120)}")
        logging.info(f"P/E Ratio (POP): {stock_pop.pe_ratio(120)}")
        logging.info(f"VWSP (POP): {stock_pop.volume_weighted_stock_price()}")
        # Log metrics for TEA
        logging.info(f"Dividend Yield (TEA): {stock_tea.dividend_yield(99)}")
        logging.info(f"P/E Ratio (TEA): {stock_tea.pe_ratio(99)}")
        logging.info(f"VWSP (TEA): {stock_tea.volume_weighted_stock_price()}")
        # Log metrics for ALE
        logging.info(f"Dividend Yield (ALE): {stock_ale.dividend_yield(60)}")
        logging.info(f"P/E Ratio (ALE): {stock_ale.pe_ratio(60)}")
        logging.info(f"VWSP (ALE): {stock_ale.volume_weighted_stock_price()}")
        # Log metrics for GIN
        logging.info(f"Dividend Yield (GIN): {stock_gin.dividend_yield(100)}")
        logging.info(f"P/E Ratio (GIN): {stock_gin.pe_ratio(100)}")
        logging.info(f"VWSP (GIN): {stock_gin.volume_weighted_stock_price()}")
        # Log metrics for JOE
        logging.info(f"Dividend Yield (JOE): {stock_joe.dividend_yield(250)}")
        logging.info(f"P/E Ratio (JOE): {stock_joe.pe_ratio(250)}")
        logging.info(f"VWSP (JOE): {stock_joe.volume_weighted_stock_price()}")
        # Log GBCE All Share Index
        logging.info(f"GBCE All Share Index: {market.gbce_all_share_index()}")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


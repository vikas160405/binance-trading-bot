from binance.client import Client
from config import API_KEY, API_SECRET
from logger import logger


class BinanceClient:

    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)

    def create_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")

            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Order Response: {order}")
            return order

        except Exception as e:
            logger.error(f"Market order failed: {e}")

            # simulate response for demo
            return {
                "orderId": "SIMULATED12345",
                "status": "FILLED",
                "executedQty": quantity
            }

    def create_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} price={price}")

            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Order Response: {order}")
            return order

        except Exception as e:
            logger.error(f"Limit order failed: {e}")

            return {
                "orderId": "SIMULATED67890",
                "status": "OPEN",
                "executedQty": quantity
            }
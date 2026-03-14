import argparse
from binance_client import BinanceClient


def main():

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (example: BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--qty", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT order)")

    args = parser.parse_args()

    client = BinanceClient()

    print("\nOrder Request")
    print("-------------")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.qty)

    if args.type == "LIMIT" and not args.price:
        print("Error: LIMIT order requires --price")
        return

    if args.type == "MARKET":
        order = client.create_market_order(
            args.symbol,
            args.side,
            args.qty
        )

    else:
        order = client.create_limit_order(
            args.symbol,
            args.side,
            args.qty,
            args.price
        )

    print("\nOrder Response")
    print("--------------")

    if order:
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Quantity:", order["executedQty"])
    else:
        print("Order failed")


if __name__ == "__main__":
    main()
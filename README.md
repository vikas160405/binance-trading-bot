# Binance Trading Bot

This is a Python CLI trading bot that interacts with the Binance API to place market and limit orders.

## Installation

pip install -r requirements.txt

## Setup

Create a .env file with your Binance API keys:

API_KEY=your_api_key
API_SECRET=your_secret_key

## Example Usage

Market Order:
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

Limit Order:
python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 70000
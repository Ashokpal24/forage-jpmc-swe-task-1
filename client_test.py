import unittest
from client3 import (getDataPoint, getRatio)


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock_name = quote['stock']
            bid_price = float(quote['top_bid']['price'])
            ask_price = float(quote['top_ask']['price'])
            price_avg = (bid_price+ask_price)/2
            self.assertEqual(getDataPoint(quote),
                             (stock_name, bid_price, ask_price, price_avg))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            stock_name = quote['stock']
            bid_price = float(quote['top_bid']['price'])
            ask_price = float(quote['top_ask']['price'])
            price_avg = (bid_price+ask_price)/2
            self.assertEqual(getDataPoint(quote),
                             (stock_name, bid_price, ask_price, price_avg))

    def test_getRation_calculateRatio(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        stock_prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            stock_prices[stock] = price
        self.assertEqual(getRatio(
            stock_prices['ABC'], stock_prices['DEF']), stock_prices['ABC']/stock_prices['DEF'])

    def test_getRation_calculateRatio_zero_at_priceB(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        stock_prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            stock_prices[stock] = price
        self.assertIsNone(getRatio(
            stock_prices['ABC'], stock_prices['DEF']),)


if __name__ == '__main__':
    unittest.main()

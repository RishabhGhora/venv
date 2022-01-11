import json

class TradeManager:
  def __init__(self, symbolJsonFile, startingAccountBalance):
    with open(symbolJsonFile) as f:
      self.symbolMap = json.load(f)
    self.balance = startingAccountBalance
    self.position = {}

  def AddTrade(self, symbol, quantity, price, buySell):
    if self.position.get(symbol, float('-inf')) == float('-inf'):
      self.position[symbol] = 0
    if buySell == 'buy':
      self.position[symbol] += quantity
      self.balance -= (quantity*price)
    elif buySell == 'sell':
      self.position[symbol] -= quantity
      self.balance += (quantity*price)
    
  def ProcessTradeList(self, tradeListFilePath):
    with open(tradeListFilePath) as f:
      tradeList = json.load(f)

    for trade in tradeList:
      if trade['product_symbol'] in self.symbolMap.keys():
        self.AddTrade(self.symbolMap[trade['product_symbol']],
                        trade['quantity'],
                        trade['price'],
                        trade['buy_sell'])
      else:
        self.AddTrade(trade['product_symbol'],
                        trade['quantity'],
                        trade['price'],
                        trade['buy_sell'])

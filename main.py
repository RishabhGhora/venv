from TradeManager.TradeManager import TradeManager

if __name__ == '__main__':
  myTradeManager = TradeManager('symbol_mappings.json', 100000)
  myTradeManager.AddTrade('AAA', 10, 100, 'buy')
  assert({'AAA': 10} == myTradeManager.position)
  assert(99000.00 == myTradeManager.balance)

  myTradeManager = TradeManager('symbol_mappings.json', 100000)
  myTradeManager.AddTrade('AAA', 10, 100, 'buy')
  myTradeManager.AddTrade('BBB', 55, 125, 'buy')
  myTradeManager.AddTrade('AAA', 25, 110, 'sell')
  assert({'AAA': -15, 'BBB': 55} == myTradeManager.position)
  assert(94875.00 == myTradeManager.balance)

  myTradeManager = TradeManager('symbol_mappings.json', 100000)
  myTradeManager.AddTrade('ES', 10, 100, 'buy')
  myTradeManager.ProcessTradeList('trade_list.json')
  myTradeManager.AddTrade('AAA', 25, 110, 'sell')
  assert({'AAA': -25, 'ES': 110} == myTradeManager.position)
  assert(89200.00 == myTradeManager.balance)

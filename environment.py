import numpy as np
from instance import *

class Env():
  def __init__(self, data, initial_money=1000, initial_coin=0, fee=0.001):
    self.data=data
    self.action_space = 3 #buy, sell, do nothing
    self.initial_money=initial_money
    self.initial_coin=initial_coin
    self.fee=fee
    self.trade_pct=0.99
    self.index=0
    self.trader=Instance(initial_money=self.initial_money, initial_coin=self.initial_coin, fee=self.fee)
    self.previousNetWorth=self.trader.netWorth
    self.actions=[]

    
    
  def step(self, action): # Execute one time step within the environment
    if(action==0): #buy
      self.trader.buy(self.trade_pct*self.trader.money, self.data[self.index])
      
    if(action==1): #sell
      self.trader.sell(self.trade_pct*self.trader.coin, self.data[self.index])
    
    self.previousNetWorth=self.trader.netWorth
    
    self.index+=1
    
    if(self.trader.netWorth<10 or self.index==len(self.data)-1):
      done=True
    else:
      done=False
    u_state=self.getState()
    self.trader.updateNetWorth(self.data[self.index])
    
    return u_state, done
      #return new state and reward+actions (if*)
  def getState(self):
    return self.data[self.index]
    
  def reset(self):
    self.index=0
    self.trader=Instance(initial_money=self.initial_money, initial_coin=self.initial_coin, fee=self.fee)
    self.previousNetWorth=self.trader.netWorth
    self.actions=[]
    # Reset the state of the environment to an initial state
    
  def render(self):
    # Render the environment to the screen
    self.trader.show()
    return self.trader.netWorth

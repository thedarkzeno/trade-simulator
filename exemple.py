from environment import Env
import pandas as pd 
import random

data=pd.read_csv("data/target.csv")["Y"]

env = Env(data)

done=False
while(done==False):
    price = env.getState() 
    print(price)
    action = random.randint(0,3) # 0 == buy, 1 == sell, 2 == do nothing
    _ , done = env.step(action)
    env.render()




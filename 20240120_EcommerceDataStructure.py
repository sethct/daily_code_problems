#| You run an e-commerce website and want to record the last N order ids in a log. 
#| Implement a data structure to accomplish this.

#| Import relevant packages
import pandas as pd

#-----------------#
# Define Function #
#-----------------#

class OrderLog:
    def __init__(self, N):
        #| Initialise an empty DataFrame with a single column 'order_id'
        self.log = pd.DataFrame(columns=['order_id'])
        self.capacity = N

    def record(self, order_id):
        #| Check if the log has not reached its capacity
        if len(self.log) < self.capacity:
            #| Append a new row with the given order_id
            self.log = pd.concat([self.log, pd.DataFrame({'order_id': [order_id]})], ignore_index=True)
        else:
            #| Shift the DataFrame by one and add the new order_id at the end
            self.log = self.log.shift(-1)
            self.log.iloc[-1] = {'order_id': order_id}

    def get_last(self, i):
        #| Check if i is within the valid range
        if 0 < i <= len(self.log):
            #| Retrieve the ith last element from the DataFrame
            return self.log.iloc[-i]['order_id']
        else:
            #| Return None if i is out of range
            return None
        
#------------------#
# Test Application #
#------------------#

order_log = OrderLog(N=5)

order_log.record(101)
order_log.record(102)
order_log.record(103)
order_log.record(104)

print(order_log.log)
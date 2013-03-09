    #!/usr/bin/python
    # http://www.reddit.com/r/dailyprogrammer/comments/19whtk/030813_challenge_120_hard_bytelandian_exchange_3/
    
    # Bytelandian Currency is coins with positive integers on them. (Don't worry 
    # about 0-valued coins because they're useless for this problem.) You have 
    # access to two peculiar money changing machines:
    # Machine 1 takes one coin of any value N. It pays back 3 coins of the values 
    # N/2, N/3 and N/4, rounded down. For example, if you insert a 19-valued coin, 
    # you get three coins worth 9, 6, and 4.
    #
    # Machine 2 takes two coins at once, one of any value N, and one of any 
    # positive value. It returns a single coin of value N+1.
    # These two machines can be used together to get arbitrarily large amounts of 
    # money from a single coin, provided it's worth enough. If you can change an 
    # N-valued coin into an N-valued coin and a 1-valued coin, you can repeat the 
    # process to get arbitrarily many 1-valued coins. What's the smallest N such 
    # that an N-valued coin can be changed into an N-valued coin and a 1-valued 
    # coin?
    # For instance, it can be done with a coin worth 897. Here's how. Use Machine 1
    # to convert it into coins worth 448, 299, and 224. Through repeated 
    # applications of Machine 1, the 299-valued coin can be converted into 262 
    # 1-valued coins, and the 224-valued coin can be converted into 188 1-valued 
    # coins. At this point you have a 448-valued coin and 450 1-valued coins. By 
    # using Machine 2 449 times, you can make this into a 897-valued coin and a 
    # 1-valued coin. To summarize this strategy:
    #
    # 897 -> 448 + 299 + 224 (Machine 1)
    # 299 + 224 -> 450x1 (repeated Machine 1)
    # 448 + 450x1 -> 897 + 1 (repeated Machine 2)
    # But of course, 897 is not the lowest coin value that lets you pull this trick
    # off. Your task is to find the lowest such value.
    # Here is a python script that will verify the steps of a correct solution 
    #(will not verify that it's optimal, though).[2]
    # Author: Cosmologicon
    
    import sys
    
    def machine1(num):
      # Machine 1 takes one coin of any value N. It pays back 3 
      # coins of the values N/2, N/3 and N/4, rounded down. For example, if you 
      # insert a 19-valued coin, you get three coins worth 9, 6, and 4.
      return (num/2,num/3,num/4);
    
    def machine2(coin1, coin2):
      # Machine 2 takes two coins at once, one of any value N, and one of any 
      # positive value. It returns a single coin of value N+1.
      return (coin1 + 1)
    ones = 0
    def make_ones(num):
      global ones
      #uses machine1 to make all ones coins. 
      if num == 1:
        ones+=1
        return
      if num == 0:
        return
      coins = machine1(num)
      make_ones(coins[0])
      make_ones(coins[1])
      make_ones(coins[2])
    
    def make_plus_one(coin):
      global ones
      # takes one coin in and then uses the one coins to
      # feed into machine 2
      while(ones != 1):
        ones-=1;
        coin = machine2(coin,1)
      return coin
    
    def convert(num):
      global ones
      coins = machine1(num)
      make_ones(coins[2])  
      make_ones(coins[0])  
      coin = make_plus_one(coins[1])
      ones-=1;
      return (coin, ones)
    
    def find_min():
      new_coin = 0
      coin = 4
      while(new_coin != coin):
        (new_coin,one) = convert(coin)
        coin+=1
      return new_coin 
    
    def main():
      min_coin = find_min()
      print "Found min value: " + str(min_coin) 
      return 0
    
    if __name__ == '__main__':
      main()

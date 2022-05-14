# This is the main running script for the market_maker application
# The application will make predictions based on current portfolio and inputs and we'll try to use the zerodha api in the future to see all the beautiful and useful things we can build.

# This is the reference amount. Our profits will be based on the reference amount. We can also call it the target amount.
# This is the amount at which we intend to eventually sell. We shall call it target as it makes slightly more sense to call it the target amount. To maximize profits we have to maximize the target amount.
target = 75 

# This is out average amount. This is our average price for a particular stock. Our job is to minimize this in order to maximize profits.
average=50

# Pass in a dictionary with keys containing all the necessary keys
# The input dict will be of the form {current:{avg:average_value,qty:number_of_shares_owned},new:{price:new_price,qty:qty_to_buy}}
def calculate_average(input_dict):
  current_avg=input_dict.current.avg
  current_qty=input_dict.current.qty
  price = input_dict.new.price
  new_qty = input_dict.new.qty
  return ((current_avg*current_qty)+(price*new_qty))/(current_qty+new_qty)

# The below function will calculate the profit to be gained at a particular target price. It depends on the target, average and the total quantity held. Our job is maximize the profit we can make. We will later also plot these values and do fun stuff with the data that we have access to
# Pass in a dictionary that contains the three values required {target:target,average:average,total_qty:total_qty}
def calculate_profit(input_dict):
  reference = input_dict.target
  average = input_dict.average
  total_qty = input_dict.total_qty
  return (reference-average)*total_qty


# One thing to note is that this application is rather simple. The profits have no correlation with time as in time is not a factor for profits. The profits generated is solely a function of the selling price and the average of the person.



# Now we shall lay out some preferential metrics. These metrics allow us to evaluate the benifit of our calculations performed.
# For us preferential metrics are low average values and higher target for maximizing profits.

# We are making the profits solely a function of the average and the target and not time because it provides a more simple approach and since this is how gtt orders work in the zerodha api, using this approach will prove useful in the future as well.


# We need to focus in our main requirement ie. to maximize our profits. We have "assumed" that the best way to maximize profits is by reducing our average. This is our ultimate goal and one of the ways to do this is to buy at the least possible amount possible in order ro keep our average very low so even with a relatively lower target we will make good profits.









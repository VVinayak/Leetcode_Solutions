# C COWS
# S STORES
# F FARMERS
# U(I) = UNITS OF MILK FROM COW I
# R(J) = RENT PER FARMER FOR A COW
# P(K) = UNIT PRICE OF MILK PER SHOP
# MC(K) = MAX CAPACITY PER SHOP

#we need to find whether a particular cow needs to be milked or rented out

def milkorrent(num_cow, num_store, num_farmer, units_milk, rent, price, max_cap):
	#We will sort the unit price per shop and the rent per farmer in ascending order
	#We will then compare the rent per cow versus the price per shop from highest to lowest 
	#for the capacity the cow can give. Remove shops and farmers that have already completed
	# their quota/have already bought cows and based on the final monetary value, assign binary values

	cows = [0]*num_cow
	# 0 in cow represents that it will be milked 
	# 1 in cow represents that it will be rented

	rent = sorted(rent)
	price_capacity = [[price[k], max_cap[k]] for k in xrange(num_store)]
	price_capacity = sorted(price_capacity, key = lambda shop: shop[0])  #sort by price

	#marking the indices of the last farmer who rented a cow/last shop that bought all milk
	farmer_index = num_farmer - 1
	shop_index = num_store - 1

	for i in xrange(num_cow):
		if farmer_index >=0 and shop_index >= 0:
			temp_shop = shop_index
			temp_units = units_milk[i]
			temp_earn = 0
			while temp_shop>=0 and price_capacity[temp_shop][1] < temp_units:
				temp_units = temp_units - price_capacity[temp_shop][1]
				temp_earn = temp_earn + price_capacity[temp_shop][0]*price_capacity[temp_shop][1]
				temp_shop = temp_shop - 1
			if temp_shop >=0:
				temp_earn = temp_earn + price_capacity[temp_shop][0]*temp_units
			if temp_earn < rent[farmer_index]:
				cows[i] = 1
				farmer_index = farmer_index - 1
			elif temp_shop >=0:
				shop_index = temp_shop
				price_capacity[shop_index][1] = price_capacity[shop_index][1] - temp_units
			elif temp_shop < 0:
				shop_index = temp_shop
		elif shop_index < 0:  
			#when all shops have received their full quota of milk
			cows[i] = 1

	return cows

def main():
	C = input("Enter number of cows: ")
	S = input("Enter number of stores: ")
	F = input("Enter number of farmers: ")
	U = input("Enter units of milk as a comma separated array with no space: ")
	R = input("Enter rent per farmer as a comma separated array with no space: ")
	P = input("Enter price per shop as a comma separated array with no space: ")
	MC = input("Enter capacity per shop as a comma separated array with no space: ")
	if C != len(U) or S != len(P) or S!= len(MC) or F != len(R):
		print "ERROR IN INPUT SIZE!"
	else:
		print "0 in cows array below represents that it will be milked "
		print "1 in cows array below represents that it will be rented"
		print milkorrent(C,S,F,U,R,P,MC)

	# 0 in cow represents that it will be milked 
	# 1 in cow represents that it will be rented

if __name__ == '__main__':
	main()


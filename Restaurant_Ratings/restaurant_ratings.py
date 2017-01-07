# your code goes here
import sys
#Andalu is rated at 3.
def rated_restaurants(filename): #function that takes in txt file
    """Reads a file and spits out the ratings in alph. order"""
    
    restaurants = {} #empty dict 
    filename = open(sys.argv[1]) #filename opens text input 
    for line in filename:
        line_stripped = line.strip().split(':')#strips whitespace and splits strings at colons
        
        restaurant_name = line_stripped[0]
        restaurant_rating = line_stripped[1]

        restaurants[restaurant_name] = restaurant_rating #adding key to value
    return restaurants

        # for item in name:
        #     restaurants[item] = restaurants.get(item, 0) #add rest rating if not in dict already
    #print sorted(restaurants)
    filename.close()
rated_restaurants(sys.argv[1])

def sorts_restaurants(filename):
    restaurants = rated_restaurants(filename)

    for restaurant, rating in restaurants.items():
        print "{} is rated at {}.".format(restaurant, rating)

    # restaurant_keys = rated_restaurants(filename).keys()
    # restaurant_values = rated_restaurants(filename).values()

    
print sorts_restaurants(sys.argv[1])
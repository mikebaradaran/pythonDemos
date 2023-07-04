weather = {'Glasgow':11,'London':21,'Edinburgh':15,'Manchester':18,'Thurso': 9}

def filter_city(city):
    if weather[city] >= 15:
        return True
    else:
        return False
    
def main():
    # For Loop plus source collection, optional if condition, and expression.
    warm_cities = {}
    for city in weather:           		# Iterator for loop + collection.
        if weather[city] >= 15:          	# Optional condition (filtering)
            warm_cities[city] = weather[city]  	# Expression
    print(f"1.Warm Cities = {warm_cities}")
    # For Loop plus source collection, optional if condition with user function, and expression.
    warm_cities = {}
    for city in weather:
        if filter_city(city):
            warm_cities[city] = weather[city]
    print(f"2.Warm Cities = {warm_cities}")
    # Built-in filter() function plus source collection, user function for filtering.
    warm_cities = list(filter(filter_city, warm_cities))
    print(f"3.Warm Cities = {warm_cities}")

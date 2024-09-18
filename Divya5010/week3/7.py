def get_price(a, b):
    child = 105
    adult = 250
    group = 140
    group_rate =0.9

    cost = (a * child + b * adult)

    if a + b > group:
        cost = cost * group_rate
    return cost

def main():
    num_a = int(input("Enter the number of a:-"))
    num_b = int(input("Enter the number of b:-"))
    cost = get_price(num_a,num_b)
    print("The cost of your tickets is  : $" + str(cost))
main()
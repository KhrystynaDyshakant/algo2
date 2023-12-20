from minNumOfBananasPerHour import min_Num_Of_Bananas_Per_Hour

def main():
    piles1 = [3, 6, 7, 11]
    H1 = 8
    
    piles2 = [30, 11, 23, 4, 20]
    H2 = 5
    
    piles3 = [30, 11, 23, 4, 20]
    H3 = 6

    piles4 = [6, 15, 2, 5, 21]
    H4 = 7

    piles5 = [3, 6, 7, 11]
    H5 = 1000000000

    result1 = min_Num_Of_Bananas_Per_Hour(piles1, H1)
    result2 = min_Num_Of_Bananas_Per_Hour(piles2, H2)
    result3 = min_Num_Of_Bananas_Per_Hour(piles3, H3)
    result4 = min_Num_Of_Bananas_Per_Hour(piles4, H4)
    result5 = min_Num_Of_Bananas_Per_Hour(piles5, H5)
    
    print(f"Кількість бананів, які Джексі може з'їсти за годину у першому випадку: {result1}")
    print(f"Кількість бананів, які Джексі може з'їсти за годину у другому випадку: {result2}")
    print(f"Кількість бананів, які Джексі може з'їсти за годину у третьому випадку: {result3}")
    print(f"Кількість бананів, які Джексі може з'їсти за годину у четвертому випадку: {result4}")
    print(f"к:{result5}")

if __name__ == '__main__':
    main()

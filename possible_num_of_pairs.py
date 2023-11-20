def possible_num_of_pairs(pairs):
    unique_boys = set()
    unique_girls = set()

    for pair in pairs:
        boys, girls = pair
        if boys % 2 == 1:
            unique_boys.add(boys)
        if girls % 2 == 0:
            unique_girls.add(girls)

    probable_pairs = len(unique_boys) * len(unique_girls)

    return probable_pairs

def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        if not (0 < N < 10000):
            raise ValueError(" 0 < N < 10000 ")
        pairs = [tuple(map(int, line.split())) for line in file.readlines()]
    return N, pairs

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    try:
        N, pairs = read_input(input_filename)

        if not (0 < N < 10000):
            raise ValueError(" 0 < N < 10000 ")

        result = possible_num_of_pairs(pairs)
        write_output(output_filename, result)
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

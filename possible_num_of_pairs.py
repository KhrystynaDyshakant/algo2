def possible_num_of_pairs(pairs):
    tribes = [set(pairs[0])]
    count = 0

    for pair in pairs[1:]:
        for tribe in tribes:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                break
            else:
                tribes.append(set(pair))

    for i in range(len(tribes)):
        for j in range(i+1, len(tribes)):
            for first_person in tribes[i]:
                for second_person in tribes[j]:
                    if first_person % 2 != second_person % 2:
                        count += 1

    return count, tribes

def read_input(filename):
    with open(filename, 'r') as file:
        N = int(file.readline())
        if not (0 < N < 10000):
            raise ValueError(" 0 < N < 10000 ")
        pairs = [tuple(map(int, line.split())) for line in file.readlines()]
    return N, pairs

def write_output(filename, result):
    count, tribes = result
    with open(filename, 'w') as file:
        file.write(f"{count} (")
        pairs = []
        for i in range(len(tribes)):
            for j in range(i+1, len(tribes)):
                for first_person in tribes[i]:
                    for second_person in tribes[j]:
                        if first_person % 2 != second_person % 2:
                            pairs.append(f"{first_person}/{second_person}")
        pairs_str = ', '.join(pairs)
        file.write(f"{pairs_str})")



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


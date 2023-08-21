def read_wordlist(filename):
    word_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                word = line.strip()  # Remove newline characters and extra spaces
                if word:  # Skip empty lines
                    word_list.append(word)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

    return word_list


words_list = read_wordlist("wordlist.txt")

message_file = 'coding_qual_input.txt' # <<<<< FILE NAME HERE

def create_dict(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    words_dict = {}
    for line in lines:
        number, word = line.split()
        words_dict[int(number)] = word.strip()
        sorted_key_value_pairs = dict(sorted(words_dict.items()))
    # print(sorted_key_value_pairs)  # for testing
    return sorted_key_value_pairs


def create_pyramid(sorted_key_value_pairs):
    pyramid = []
    current_row = []
    total_count = 0
    row_length = 1
    while total_count + row_length <= len(sorted_key_value_pairs):
        current_row = [sorted_key_value_pairs.get(total_count + i + 1, '') for i in range(row_length)]
        pyramid.append(current_row)
        total_count += row_length
        row_length += 1
    # print("Pyramid:", pyramid)  # for testing
    return pyramid

def decode_message(pyramid):
    last_row_words = [row[-1] for row in pyramid[:-1] if row[-1]]
    last_word_last_subset = pyramid[-1][-1]
    if last_word_last_subset:
        last_row_words.append(last_word_last_subset)
    decoded_message = " ".join(last_row_words)
    return decoded_message

sorted_key_value_pairs = create_dict(message_file)
pyramid = create_pyramid(sorted_key_value_pairs)
decoded_message = decode_message(pyramid)

print(decoded_message)
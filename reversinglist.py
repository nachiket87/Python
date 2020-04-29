


message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]

def reverse_chars(message, left_index, right_index):
    while left_index < right_index:
        message[left_index] , message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1
    return message


def reverse_words(message):
    message = reverse_chars(message, 0, len(message)-1)

    current_word_start_index = 0

    for i in range(len(message) + 1 ):
        if (i == len(message)) or (message[i] == ' '):
            message = reverse_chars(message, current_word_start_index, i-1)
            current_word_start_index = i+1

    return message

print(' '.join(reverse_words(message)))
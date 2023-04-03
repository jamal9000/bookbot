
def main():
    f_path = "./books/frankenstein.txt"

    with open(f_path) as f:
        file_contents = f.read()

    number_of_words = wordCount(file_contents)
    letter_count = letterCount(file_contents)

    print(reportGen(number_of_words, letter_count))


def wordCount(text):
    words = text.split()
    return(len(words))

def letterCount(text):
    text = text.lower()

    count_dict = { }
    for i in text:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    return count_dict



def reportGen(word_count, letter_count_dict):
    letters = list(letter_count_dict.keys())
    letters.sort()

    report_array = []

    report_array.append("--- Begin report of books/frankenstein.txt ---")
    report_array.append(f"{word_count} words were found in the document\n\n")

    for i in letters:
        if i.isalpha():
            quantity = letter_count_dict[i]
            report_array.append(f"The {i} character was found {quantity} times")

    report_array.append("--- End report ---")

    report_string = "\n".join(report_array)

    return report_string
    



main()
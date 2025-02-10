def main():
    book_path = "books/frankenstein.txt"
    text = str(get_book_text(book_path)).lower()
    symbol_no = count_symbols(text)
    print(symbol_no)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_symbols(string):
    symbol_dict = {}
    for i in range(len(string) - 1):
        symbol_dict[string[i]] = symbol_dict.get(string[i], 0) + 1
    return symbol_dict

main()
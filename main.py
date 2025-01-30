def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        count_words(file_contents)

def count_words(paragraph):
    paragraph = paragraph.lower()
    count={}
    for w in paragraph:
        for i in range(0,len(w)):
            if w[i] not in count:
                count[w[i]] = 1
            else:
                number = count[w[i]] +1
                count[w[i]] = number
    for k,v in count.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
main()


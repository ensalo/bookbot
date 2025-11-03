def count_words(booktext):
    wordlist = booktext.split()
    wordcount = len(wordlist)
    return wordcount

def count_chars(booktext):
    char_count = {}
    lowercase = booktext.lower()
    for letter in lowercase:
        if letter not in char_count:
            char_count[letter] = 1
        else :
            char_count[letter] +=1
    return char_count

def sort_helper(items):
    return items["num"]

def sort_characters(unsorted_dict):
    sorted_list = []
        
    for i in unsorted_dict:
        sorted_list.append({"char": i, "num": unsorted_dict[i]})
      
    sorted_list.sort(key=sort_helper, reverse=True)
    
    return sorted_list


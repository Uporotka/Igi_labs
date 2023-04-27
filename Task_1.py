import re

ABBREVIATION = ['mr.', 'mrs.', 'ms.', 'etc.', 'dr.', 'vs.', 'sr.', 'jr.', 'smth.', 'smb.',
                'v.', 'adj.', 'adv.', 'prep.', 'p.', 'pp.', 'par.', 'ex.', 'pl.', 'sing.', 're.',
                'rf.', 'edu.', 'appx.', 'in.', 'sec.', 'gm.', 'cm.', 'qt.', 'ft.', 'oz.', 'pt.',
                'yr.', 'jan.', 'feb.', 'mar.', 'apr.', 'jun.', 'jul.', 'aug.', 'sep.', 'oct.',
                'nov.', 'dec.', 'mon.', 'tue.', 'wed.', 'thu.', 'fri.', 'sat.', 'sun.', 'ph.']
ABBREVIATION_TWO_WORDS = ['e.g.', 'i.e.', 'p.s.']


def input_txt():

    print("If you want to open a  file, please print \"File\",\n" 
          "if you want to enter text, print \"Text\": ")
    inp = input().lower()
    if inp == "file":
        print("Enter the path to the file: ")
        with open(input(), 'r') as file:
            return file.read()
        # with open("Test_text.txt", 'r') as file:
        #      return file.read()

    elif inp == "text":
        print("Enter text: ")
        text = input()
        return text
    else:
        print("Invalid input")
        return input_txt()


def start_task1():
    text = input_txt()
    print("Number of sentences in a text: ", amount_of_sentences(text))
    print("Amount of non-declarative sentences", amount_non_decl(text))
    print("Average length of sentences", average_len_sent(text))
    print("Average length of words", average_len_word(text))
    print("Top_k_repeated_n_grams", top_k_repeated_n_grams(text))

def amount_of_sentences(text):
    amount = 0
    str_ = re.sub(',', '', text)
    str_ = re.sub(r'\b([A-Z]\.)+|[A-Z]{2,}\b', '', str_)
    str_ = str_.lower()
    for i in ABBREVIATION:
        amount += str_.count(i)
    for i in ABBREVIATION_TWO_WORDS:
        amount += str_.count(i) * 2
    str_modified = re.split('\?!|\s*\.\.\.\s*|\s*\.\s*|\s*\?+\s*|\s*!+\s*', str_)[0:-1]
    return len(str_modified) - amount


def average_len_sent(text):
    text_tmp = re.sub(r'!|\?|,|\.|\'|-|;', '', text)
    text_tmp = re.sub(r'\b[0-9]+\b', '', text_tmp)
    text_tmp = re.sub(r'\s+', '', text_tmp)
    if amount_of_sentences(text) != 0:
        return len(text_tmp)/amount_of_sentences(text)
    else:
        return 0


def average_len_word(text):
    text_tmp = re.sub(r'\b([A-Z]\.)+|[A-Z]{2,}\b', '', text)
    text_tmp = re.sub(r'\b[0-9]+\b', ' ', text_tmp)
    text_tmp = re.sub(r'!|\?|,|\.|\'|-|;', ' ', text_tmp)
    amount_words = len(re.split(r'\s+', text_tmp)[0:-1])
    text_tmp = re.sub(r'\s+', '', text_tmp)
    if amount_words != 0:
        return len(text_tmp)/amount_words
    else:
        return 0


def amount_non_decl(text: str):
    lis = re.findall(r'\s*\?!\s*|\s*!+\s*|\s*\?+\s*', text)
    return len(lis)


def top_k_repeated_n_grams(text, k=10, n=4):
    list_tmp = []
    for i in range(n, len(text)+1):
        word = ''
        for j in range(i-n, i):
            word += text[j]
        list_tmp.append(word)
    list_t = []
    for i in range(0, len(list_tmp)):
        list_t.append((list_tmp[int(i)], text.count(list_tmp[i])))
    tmp = set(list_t)
    list_t = list(tmp)
    list_t = sorted(list_t, key=lambda a: a[1], reverse=True)
    return list_t[0:k]


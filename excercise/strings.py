#https://www.w3resource.com/python-exercises/string/

def swap2chars(istring):
    if len(istring) < 2:
        return ''
    return  istring[0] + istring[1] + istring[len(istring)-2] + istring[len(istring)-1]  
        
def replace_first(istring : str):
    char = istring[0]
    return char +istring[1:].replace(char,"$")

def swap2strings(str1: str, str2: str):
   first1 = str1[:2]
   first2 = str2[:2]
   return [first2 + str1[2:] + " " + first1 + str2[2:]]   
    
def add_ing_or_ly(istr : str):
    if len(istr)<3:
        return istr
    if not istr.endswith('ing'):
        return istr + "ing"
    else:
        return istr + 'ly'

def exc7(istr : str):
    list_words = []
    last_space=0
    popped = 0
    gogo = False
    for i in range(len(istr)):
        if not istr[i].isalpha() :
            list_words.append(istr[last_space+1:i])
            last_space = i
    for word in list_words:
        if word == 'not':
            notfound = True
        if word == 'poor' and notfound:
            gogo = True
    
    if gogo:
        a=list_words.index('not')
        b=list_words.index('poor')  
        for i in range(a-1,b):
            
            popped +=1
        list_words.append('good')
        return ' '.join(list_words)
    return istr

def exc8(words : list):
    longest = 'a'
    for word in words:
        if len(word) > len(longest):
            longest = word
    return f"The longest word is {longest}\nNumber of chars: {len(longest)}"

def exc9(istr : str, nth : int):
    if len(istr)>nth:
        return f"{istr[ :nth-1]}{istr[nth: ]}"

def exc10(istr : str):
    return istr[-1:] + istr[1:len(istr)-1] + istr[0]

def exc11(istr : str) -> str :
    ostr = ''
    for i in range(len(istr)):
        if i % 2 == 0:
            ostr = ostr + istr[i]
    return ostr

def exc12(istr : str) -> dict:
    resultdict = {}
    word= ''
    for c in istr:
        if c.isalpha():
            word = word + c
        if not c.isalpha():
            if word in resultdict:
                resultdict[word] = resultdict[word] + 1
            else:
                resultdict[word] = 1
            word = ''
    return resultdict          

def exc13(istr : str) -> str:
    return istr.upper() + istr.lower()
            
def exc14(istr : str) -> str:
    lwords = [word in istr.split(',')]
    lwords.sort       
    
def exc22(istr : str) -> str:
    olist= []
    
    for (i , c ) in enumerate(istr):
        olist.append(c)
    olist.sort()
    return olist

def exc25(istr : str) -> str:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shift = 3
    result = ''
    for c in istr:
        if c in alphabet:    
            if alphabet.index(c)+shift < len(alphabet)-1 :
                result = result + alphabet[alphabet.index(c)+shift]
            else :
                result = result + alphabet[ alphabet.index(c)+shift - len(alphabet)-1 ]
        else :
            result = result + c
    return result

import textwrap


swap2chars('w3resource')
replace_first('restart')
words = ['exchange', 'words', 'between', 'two', 'strings']
sentence = 'the quick brown fox jumps over the lazy dog.'

print(textwrap.fill(sentence, width=50))

sample_text = """
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java."""

print(sample_text)




# 0 a
# 1 b
# 2 c
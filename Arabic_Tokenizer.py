
# This is a simple Arabic word tokenizer that takes a text and outpus a list of words
# Author: Yousra Hesham Hassan Mahdy
# Date: 25/06/2019
from pyarabic import  araby as araby
text1=  'السلام عليكم ورحمة الله و بركاته' # peace and god's grace be upon you 
text2= 'انا اسمي يسرا هشام و اعمل مهندسة في جامعة أسوان, كلية الهندسة' # My name is Yousra Hesham and I work as an engineer at Aswan University, Faculty of Engineering
text3= 'هل تعلم ان تعلم البرمجة ممتع للغاية؟' # Do you Know that learning programming is fun?

# Now text1 supposed to output 7 tokens
print (text1.encode('utf8'))
print (text1) # without formating as unicode
print(araby.tokenize(text1))

# Now text1 supposed to output 13 tokens
print (text2.encode('utf8'))
print (text2) # without formating as unicode
print(araby.tokenize(text2))


# Now text1 supposed to output 8 tokens

print (text3.encode('utf8'))
print (text3) # without formating as unicode
print(araby.tokenize(text3))

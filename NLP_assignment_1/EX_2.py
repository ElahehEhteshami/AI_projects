import re

# a
text_a = "some    random  text     here   "
normalized_text = re.sub(r'\s+', ' ' , text_a)
print(normalized_text)

#########################################
# b
text_b = "koochari@srbuai.ac.ir or koochari@gmail.com"

academic_emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.ac\.\w+\b', text_b)
print(academic_emails)

#########################################
# c
text_c = "#123 some text here with #some_hashtag . #زبانـفارسی"
hashtags = re.findall(r'#(\w+)', text_c)
print(hashtags)

#########################################
# d
text = "آدرس‌های معتبر: 192.168.0.1، 255.255.255.255، 300.8.8.8، 172.16.999.1"

pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|1?\d\d?)\b'
ips = re.findall(pattern, text)
print(ips)

#########################################
# e
pattern_lang = r'^b+a+,(a|b){2,}$'
samples = [
   "bbaaaa,bbb",
   "bbaba,aa",
   "bbaab",
   "baa,abbb",
   "bba",
   "bbba"
]
for s in samples:
   result = re.match(pattern_lang, s)
   print(f"{s}: {'معتبر' if result else 'نامعتبر'}")

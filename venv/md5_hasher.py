import hashlib
import base64
# import requests

words = []
md5hashes = []
# shahashes = []
qpressed = False
counter = 0

# url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt'
# f = f.get_file_contents(url, ref)
# raw_data = f.decoded_content
# print(rawd_data)

while (qpressed == False):
    word = input("Enter a word: ") # User enters a word
    counter +=1
    print((counter-1))
    if word == 'q':

        print(words)
        qpressed = True
    else:
        wordstrip = word.strip() #stripping the white spaces from word
        encodedword = wordstrip.encode('utf-8') #encode the word ascii
        # print(encodedword) #see the encoded word
        md5hash = hashlib.md5(encodedword).hexdigest() #creating the md5 hash
        # shahash = hashlib.sha1(encodedword).hexdigest() #creating the sha hash
        words.append(word) #add word to list
        md5hashes.append(md5hash) #add md5 hash to list
        # shahashes.append(shahashes)

wordlist = open("wordlist.txt", "a") #open wordlist to append
md5hashlist = open("md5hashlist.txt", "a+") #opne md5hash list to append
# shahashlist = open("shahashlist.txt", "a+")

for i in range(len(words)):
    print("----------------")
    print("Word: " + words[i])
    print("MD5 Hash: " + md5hashes[i])
    # print(shahashes[i])

    # with open("wordlist.txt", "r") as wordcheck:
    #     wordline = wordcheck.readline()
    #     for wordline in wordcheck:
    #         if words[i] in wordline:
    #             pass
    #         else:

    with open('wordlist.txt', 'r') as wordlist:
        if words[i] not in wordlist.read():
            with open('wordlist.txt', 'a') as wordlist:
                wordlist.write(words[i] + "\n")

    # with open("md5hashlist.txt", "r") as hashcheck:
    #     for hashline in hashcheck:
    #         if md5hashes[i] in hashine:
    #             pass
    #         else:
    with open('md5hashlist.txt', 'r') as md5hashlist:
        if md5hashes[i] not in md5hashlist.read():
            with open('md5hashlist.txt', 'a') as md5hashlist:
                md5hashlist.write(md5hashes[i] + "\n")

    # with open('shahashlist.txt', 'r') as shacheck:
    #     for line in inF:
    #         if words[i] not in line:
    #             shahashlist.write(shahashes[i] + "\n")








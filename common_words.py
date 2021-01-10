from collections import Counter

#opens the file. the with statement here will automatically close it afterwards.
with open("tweettext.txt") as input_file:
    #build a counter from each word in the file
    count = Counter(word for line in input_file
                         for word in line.split())

print(count.most_common(200))

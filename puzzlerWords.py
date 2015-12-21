from sets import Set
words = []
vowels = Set(["a", "e", "i", "o", "u"])
cons = [x.lower() for x in ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X","Y", "Z"]]
with open('/usr/share/dict/words') as inputfile:
			for line in inputfile:
				word = line[:-1].lower()
				words.append(word)
for s in range(3,9):
	lengthOfWords = s
	for n in range(3,7):
		numOfWords = n
		weirdwords = {}
		for word in words:
			if len(word)==lengthOfWords:
				tail = word[1:]
				# print tail
				# print word[0]
				if tail in weirdwords.keys():
					weirdwords[tail].add(word[0])
				else:
					weirdwords[tail]=Set(word[0])
		#print words
		#print weirdwords
		print "--------"
		print "len" + str(lengthOfWords), "num" + str(numOfWords)
		print "--------"
		for suff in weirdwords:
			if len(weirdwords[suff]) == numOfWords:
				if not bool(vowels & weirdwords[suff]): 
					temp = []
					diff = 0
					for l in weirdwords[suff]:
						temp.append(cons.index(l))
					#print temp
					lets = sorted(temp)
					for i in range(numOfWords-1):
						diff+=(lets[i+1]-lets[i])
					if diff == numOfWords-1:
					#if (lets[1]-lets[0] == 1 and lets[2]-lets[1] == 1 and lets[3]-lets[2] == 1):
						print suff, weirdwords[suff]
						print lets

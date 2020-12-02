def stutter(word):
	new_word = list(word)
	print(((str(new_word[0]+new_word[1])+' ... ')*2)+word+'?')
stutter('increasing')
from django.shortcuts import render
from glob import glob
import os
from pprint import pprint
def index(request):
	cardsF = (glob('blog/cards/*.card'))
	print cardsF
	cardsF.sort(key=os.path.getmtime)
	cards = []
	for card in cardsF[::-1]:
		lines = open(card).read().split('\n')
		topic = lines.pop(0)
		body  = '\n'.join(lines)
		cards.append((topic,body))
	return render(request, 'personal/cards.html',{'content':cards})



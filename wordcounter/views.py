from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split(' ')
	dic = {}
	for word in wordlist:
		dic[word] = dic.get('word', 0) + 1
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'dic': dic})


def about(request):
	return render(request, 'about.html')

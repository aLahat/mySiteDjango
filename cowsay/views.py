from django.shortcuts import render

def index(request):
	import os
	cow = os.popen('fortune | cowsay').read()#.split('\n')
	return render(request, 'ASCII.html',{'content':[cow]})



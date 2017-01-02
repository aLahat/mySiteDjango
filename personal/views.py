from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html',{'content':['hi',
								'hello']})

def cowsay(request):
	import os
	cow = os.popen('fortune | cowsay').read()#.split('\n')
	return render(request, 'personal/basic.html',{'content':[cow]})



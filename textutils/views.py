# this file is created by me
import getpass

from django.http import HttpResponse
from django.shortcuts import render

#personal navigator
# def index(request):
#     return HttpResponse('''<h1> hello</h1>  <a href = "https://www.phot.ai/"> photo ai </a><br> <a href = "https://in.tradingview.com/"> tradingview </a>''')
# def about(request):
#     return HttpResponse("world")

#pipline
# def index(request):
#     return HttpResponse("Home")
# def removepunc(request):
#     return HttpResponse("remove punctualization <a href='/'> back</a>")
# def capital(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceRemove(request):
#     return HttpResponse("space Remove")

#templates
# def index(request):
#     #words= {'name':'ram','place':'ayodhya'}
#     return render(request, 'index.html')
# def removepunc(request):
#     #get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("remove punctualization <a href='/'> back</a>")
# def capital(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceRemove(request):
#     return HttpResponse("space Remove")

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase','off')
    charcount = request.POST.get('charcount','off')
    analyzed = ""

    puntuations = '''*.,!,?, :, ;, ', ", -, —, , /,\, , @, #, $, %, &, (, ), [, ], {, }, <, >, ~, `, |, …'''
    if removepunc == "on" or uppercase == "on":
        if removepunc == "on":
            for char in djtext:
                if char not in puntuations:
                    analyzed = analyzed + char
                    params = {'text_analyze': analyzed}
        #return render(request, 'analyze.html',params)
        if(uppercase == "on"):
            UPPER=""
            UPPER = djtext.upper()
        params = {'fulupper': UPPER,'text_analyze': analyzed}
        return render(request, 'analyze.html',params)
    if charcount == "on":
        count = len(djtext)
        a = {'num':count}
        return render(request,'analyze.html',a)

    else:
        return HttpResponse("error")

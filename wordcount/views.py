from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def count(request):
    fullText = request.GET['fullText']

    wordlist = fullText.split()

    worddictionary = {}
    for word in wordlist:
        if(word in worddictionary):
            #Increase
            worddictionary[word] += 1
        else:
            #add to worddictionary
            worddictionary[word] = 1
    sortWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True);
    return render(request,'count.html',{'fullText':fullText,'count':len(wordlist)
    ,'worddictionary':worddictionary.items()})


def about(request):
    return render(request,'about.html')

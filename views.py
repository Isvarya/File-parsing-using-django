from django.shortcuts import render
from docx import *


def fun(request):
    lin = []
    temp = ""
    if request.method == 'POST':
        f = str(request.FILES['myfile']).split(".")
        print(f)
        if f[1] != "docx":
            return render(request, 'docerror.html')
        mul = request.files['myfile']
        temp = Document(mul)
        for t in temp.paragraphs:
            a = t.text.split()
            for x in a:
                temp = " "
                if x != ':':
                    temp += x
            lin.append(temp)
        context = {'name': lin[0], 'edu': lin[1], 'clg': lin[2], 'mail': lin[3], 'street': lin[4], 'city': lin[5],
                   'state': lin[6],
                   'country': lin[7], 'hobbies': lin[8], 'skill': lin[9],
                   }
        if lin[0] == " " or lin[1] == " " or lin[2] == " " or lin[3] == " " or lin[4] == " " or lin[5] == " " or " " == \
                lin[6] or lin[7] == " " or lin[8] == " " or lin[9] == " ":
            return render(request, 'fielderr.html', context)
        else:
            return render(request, 'resume.html', context)
        return render(request, 'index.html')

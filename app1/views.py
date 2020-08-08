from django.shortcuts import render
from rt3.settings import IDBM_FILE
import json
from django.views.generic import View

# Create your views here.

def commonData():
    json_data = json.loads(open(IDBM_FILE).read())
    data = json_data['d']
    return data


def index(request):
    data = commonData()
    lst = []
    for x in range(len(data)):
        title_image = data[x]['i']['imageUrl']
        id = data[x]['id']
        l = data[x]['l']
        s = data[x]['s']

        context={"timage":title_image,"id":id,"l":l,"s":s}
        lst.append(context)
    print(data[0]['v'])
    return render(request,'index.html',{"context":lst})







def detail(request,id):
    data = commonData()
    lst=[]
    for x in range(len(data)):
        if data[x]['id'] == id:
            v_data=data[x]['v']
            for i in range(len(v_data)):
                image = v_data[i]['i']['imageUrl']
                d = v_data[i]['id']
                l = v_data[i]['l']
                s = v_data[i]['s']
                context ={"image":image, "id":d , "l":l, "s":s}
                lst.append(context)

    return render(request,"detail_view.html",{"context":lst})


def search(request):
    title = request.GET.get('search')
    print(title)
    data=commonData()

    for x in range(len(data)):
        if data[x]['l'] == title:
            title_image = data[x]['i']['imageUrl']
            id = data[x]['id']
            l = data[x]['l']
            s = data[x]['s']
            context = {"timage": title_image, "id": id, "l": l, "s": s}
            return render(request,'search.html',{"context":context})

    return render(request,'search.html',{'message':'Not Available'})





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
    movies = lst[:2]
    Tv_series = lst[2:len(data)]
    return render(request,'index.html',{"movies":movies,"Tvseries": Tv_series})







def detail(request,id):
    data = commonData()
    lst=[]
    n=0
    video = ["https://imdb-video.media-imdb.com/vi39304729/1434659607842-pgv4ql-1597280891698.mp4?Expires=1597765115&Signature=H0Csfkfbs5-7Zb182txGv5ffO~7CpG3OkdqHE9DM5rkKD9NyAvAM6WE4gvKOkoTJHY67A6b6C7ZnchHmmCLxmmUBrRK1uAEjdpZ7TNsxRIVEDuBFdzhy4f9xK-NKZ3RMXpGAWGzWg4Er1PrRoyRtu8JLJoG71pFsWflFw3EHjhUYJQzoCtWpJ2xtwVm7eJvujFINFabWTDf73vh2giuQlqONDxZiH0nvtvBfMTW8pD6qNKnmvUhG4NyEDPl3nA-V6TDu3d510sBQtzR2QtXWcj7gsAgfaZ6HuWLVglHBN5tcWVJCZv~zNOYYMpPkwF2-lC6tQL7Oio5HQ41lXCzCTQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA",
             "https://imdb-video.media-imdb.com/vi4218076697/1434659607842-pgv4ql-1596657295845.mp4?Expires=1597749065&Signature=S8PpLNSiqcIqBiwSBMmM5k~7YKPRhmE6S4JZFB4mu5QSxVXQ1MOqBE-Ai7s6FkuYyT~Z93fU5MvJyA4x-nQhRvxvQd8FGx3Xyx0wnyqbswzCgDPqbq53qnX7UGQN9su-ivP8q9cprxGL-jpwughPSTYLwwtN6GtyGjPytLRRTcBu0NWj~wIauT4ZX7NlWEUkeUZ8b8~Meeqn5upKjnU7fmZUwNNIPcE1ZDN5h-bqE59b8VVy-oAY18YpVBbv2lx6r-VAZO30ZE9EnXj5V9YuIdFSeUOi3wQpSF2dBkU~yDDbVA118R-t22JZtsq2uzdYQI2h9pSJqWNuwX1xpXjYdw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA",
             "https://imdb-video.media-imdb.com/vi2975907353/1434659607842-pgv4ql-1596064322719.mp4?Expires=1597765528&Signature=lgSP-Sg1QyR-f~wjZGM76wif7AmdS4jyDsugPxoQHiDWMWE90G~iwF~ed6zwXlsnAAO3i~Ok-mAV5fMILMOsWj6d6hECDGD6HLn--PXU82jU8JMQPrkvse2annHOrGEyBHy08Xzm~u4DW8zF3X1P0wraKhOZAcUD~mSxySSZ3hR9FzpSjgaZmNqgMi7hZrILSzYTjPgQ6o2nGHnMn~mzksEXvXnP9hX8u5egQmUIHA0~bx8l9Lr6JLbAhAeR4IIpRE6jhLbaanEozqGFzxB3akjo9NlwgIxNN5Sdt7hDFk75Q4P3Wnxk~qK-noHR0RrYuygjqhGiCESocfXq1yfdDQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA",
             "https://imdb-video.media-imdb.com/vi2623453209/1434659607842-pgv4ql-1525191848382.mp4?Expires=1597768020&Signature=IHJODV5M11TIijGgn6d17l8y2T2~xwUXoUMwFGuBRrpEO~x-bIDm2NrdkgSZO8~9pf03RDCaM2XZqEDkv-l3k-IP5gUfe4dPn3~KLJ-vMR4IV5rXJPu5w~Thhg9HNv2uDOXT7gbt8GQkP3m2doJyjdRwgPHQtiQyeqhq63CsTujAPLquS7kgUhzVJeVwNsKDR9kAUb~NX6Fc4AKmYf--LKR5vbRiE4suIva7Fit-zYu~Cv~wFgEEAXWcHKHedE4uZAQc9b1-86-nuD~3gqYCZ0VsDfK2A7Up-usQvrWjaZoQ9ta~hrOAdOyO9HXjuFUDo3k1G7OZ30l4PRILjSF2VQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA",
             "https://imdb-video.media-imdb.com/vi3019094041/1434659607842-pgv4ql-1515626764674.mp4?Expires=1597768132&Signature=Iul929OkoubXCnp1skgdrCxcEvEicN0WRiRFtebafG7uFp2lfjjrqf7E3OMPD3MrEsVdcmwFlGIIieDaRJNKb~QnBrloABDv9cLl4TdAWW9QVMWJvG40DkIt6LmXg~Mp0tqyL8NROhvg5Qk7h1HLMR0RTP6Yy0m~TXNlqcW-rRFFdyrzXmm04lgX-o5FAcCOn8SB8MBXfi4~o6qbiKKu2SET0lk8nUtm2M1R62Y9pd9zZXTHX-KMAgfwmTaT199sxJqKNLgzERQaKBywruNLiu2GTEkxePGwHOt8wpE6EksFyata0YSHJ8xIJXhg4vNa-TYOYW4pV8YklpHiHSh16A__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA",
             "https://imdb-video.media-imdb.com/vi368293913/1434659607842-pgv4ql-1515605000749.mp4?Expires=1597768212&Signature=tj3bX-doZd28mSh~hplKtBaeH8OJV4uHXt6KFTCQs7FElvRWfY8~HwPIjE1AhkDAGTL12e8bfyJTQGwNk5bNEiRh1tYMSeF16X5GNM0PNWFdRuGOQZoUtJOksfDoeKRAHDt4-1NZdzrmzOjFvsOpIOWvpcVTZ0L6zwpdMXfexQBIoR2SECN1eWMRKXGIWqjeRZ9lL8-IBcflXJFSXBBRbJ0-vxZkfHK4JbiVf6u85JSEVK9Lq6T954ms2AuNtpOodeaOaej4g5gUlkI16QUvZb1IUn5BeOtOO2dubQjZ7yi~rXrXVgMsDK7ZZh0JoGD2LMhurEz0ASuDO3GZ0tr70Q__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"]
    for x in range(len(data)):
        if data[x]['id'] == id:
            v_data=data[x]['v']
            if data[x]['id'] == "tt7424200":
                n=3
            for i in range(len(v_data)):
                image = v_data[i]['i']['imageUrl']
                d = v_data[i]['id']
                l = v_data[i]['l']
                s = v_data[i]['s']
                context ={"image":image, "id":d , "l":l, "s":s ,"x":video[n]}
                lst.append(context)
                n+=1
    print(lst)
    return render(request,"detail_view.html",{"context":lst})


def search(request):
    title = request.GET.get('search')
    print(title)
    data=commonData()

    for x in range(len(data)):

        if data[x]['l'] == title:
            title_image = data[x]['i']['imageUrl']
            id = data[x]['id']
            print(data[x]['l'])
            print(data[x]['s'])
            l = data[x]['l']
            s = data[x]['s']
            context = {"timage": title_image, "id": id, "l": l, "s": s}
            return render(request,'search.html',{"context":context})

        else:
            return render(request,'search.html',{'message':'Not Available'})





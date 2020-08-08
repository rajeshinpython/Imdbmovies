import json
import requests

class ImdbMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("i am constructor")
        url = "https://imdb8.p.rapidapi.com/title/auto-complete"

        querystring = {"q": "movies"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "e8b8d4838cmsh4c344fa711ce0fep1d2420jsnb328ad71be53"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)
        #print(response.status_code)
        dict_data =json.loads(response.text)
        json.dump(dict_data,open("app1/raw/idbm.json",'w'))



    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        print("i am call")
        return response





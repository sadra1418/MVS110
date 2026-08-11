from django.shortcuts import render
from django.http import HttpResponse
from apps.chat_ai_with_ai import main
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
async def api(request):
     
    if request.method == 'POST':
        try : 
            p = await main(input=json.loads(request.body)) 
        except TypeError as e:
            print(e)
            p = await main(input=json.loads(request.body)) 

        print('finish main')

        res = HttpResponse(json.dumps(str(p)))
        print('res is fnish')
        res.headers['Access-Control-Allow-Origin'] = '*'
        return  res
        
@csrf_exempt
async def test(request):
     
    if request.method == 'POST':
        p = [
            {
            "text": f"""fgfgdgf""",
            "url" : f'https://chat.deepseek.com/',
            "tapic_m":" "
            },
            {
            "text": f"hi  are you okey ? ",
            "url" : 'https://chat.deepseek.com/',
            "tapic_m":" "
            }
        ]
        
        res = HttpResponse(json.dumps(str(p)))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return  res

def main_app(request):
    return(render(request , 'index.html'  ))


def google_verification(request):
    return HttpResponse(
        "google-site-verification: googleccc612f328fb14c8.html",
        content_type="text/html"
    )

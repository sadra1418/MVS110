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
        except  :
            p = await main(input=json.loads(request.body)) 


        res = HttpResponse(json.dumps(str(p)))
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

from django.shortcuts import render
from django.http import HttpResponse
from apps.chat_ai_with_ai import main
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
async def api(request):
     
    if request.method == 'POST':
        p = await main(input=json.loads(request.body)) 
        
        res = HttpResponse(json.dumps(str(p)))
        res.headers['Access-Control-Allow-Origin'] = '*'
        return  res
        
            
                 
            

       
            
    
     
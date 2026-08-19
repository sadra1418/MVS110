
import asyncio
from .my_api_lib import Api
import datetime

async def main(input):

    
    # create ai1
    ai_1 = Api(headlesss=True)
    print(f'ai_1 app start{(datetime.datetime.now())}')
    await ai_1.start()
    await ai_1.new_tab()
    print(f'ai_1 browser start{(datetime.datetime.now())}')
    await ai_1.open_ai_website(input['url_1'])
    print(f'open website{(datetime.datetime.now())}')
    await ai_1.select_a_object(object_name='Intent')
    ############

    # create ai2
    ai_2 = Api(headlesss=True)
    print(f'ai_app start{(datetime.datetime.now())}')
    await ai_2.start()
    await ai_2.new_tab()
    print(f'ai_2 browser start {(datetime.datetime.now())}')
    await ai_2.open_ai_website(input['url_2'])
    print(f'open website {(datetime.datetime.now())}')
    await ai_2.select_a_object(object_name='Intent')
    ############

    chats_history = []
    print(input)


    # a loop for chat
    

    if input['dafee'] == 0:
        
        await ai_1.send_text(
            f"""
            تو یک هوش مصنوعی هستی که می توانی در زیر نظر کاربر با یک هوش مصنوعی دیگر در ارتباط باشی .
            شخصیت تو ( تمام جزییات منحصر به فرد تو که کاربر درباره تو انتخاب کرده است در صورت خالی بودن =شکاک  سخت گیر و منتقد ) : {input['ai_1_shakhs']}
            وظیفه : درباره موضوع داده شده از طرف کار  باید با دیگر هوش مصنوعی بسته به خواسته کاربر به بحث بپردازی و بدون تایید حرف طرف مقابل و گیر کردن در چرخه تعارف ها و تکرار های بیهوده شروع به سخن کردن کنید البته باید در پاسخ طرف مقابل سوار بشی و سریعا نقد کنی انگار یک منظره است 
           
            
            نکته بسیار مهم : به هیچ وجه به این نکات گفته شده جواب پاسخ و تایید نکن انگار که دستوراتی هستند در نحوه انجام کارت و در پاسخ دادن انگار متنی نیست به جز موضوع

             موضوع انتخابی از طرف کاربر {input['text']}
            """,
            input['dafee']
        )

        
        text = []
        tapic_m = []
        n = True
        pasokhe = await ai_1.giv_text(10000 , input['dafee'])
        url_ai_1 = await ai_1.get_url()
        pasokhe_tike_tike = pasokhe.split()

        for i in pasokhe_tike_tike :
            if i == '/' :
                if n:
                    n=False
                else:
                    n=True
            elif n:
                text.append(i)
            else:
                tapic_m.append(i)

        chats_history.append(
            {
                "text": " ".join(text),
                "url" : url_ai_1,
                "tapic_m":" ".join(tapic_m)
                }
            )

        await ai_2.send_text(
            f"""
            تو یک هوش مصنوعی هستی که می توانی زیر نظر کاربر به عنوان هوش مصنوعی دوم با یک هوش مصنوعی دیگر در ارتباط باشی
            شخصیت تو ( تمام جزییات منحصر به فرد تو که کاربر درباره تو انتخاب کرده است در صورت خالی بودن =شکاک  سخت گیر و منتقد ) : {input['ai_2_shakhs']}
            وظیفه : درباره موضوع داده شده از طرف کار  باید با دیگر هوش مصنوعی بسته به خواسته کاربر به بحث بپردازی و بدون تایید حرف طرف مقابل و گیر کردن در چرخه تعارف ها و تکرار های بیهوده شروع به سخن کردن کنید البته باید در پاسخ طرف مقابل سوار بشی و سریعا نقد کنی انگار یک منظره است 

             نکته بسیار مهم : به هیچ وجه به این نکات گفته شده جواب پاسخ و تایید نکن انگار که دستوراتی هستند در نحوه انجام کارت و در پاسخ دادن انگار متنی نیست به جز متن پایین 
            
              پیام هوش مصنوعی اول : {await ai_1.giv_text(10000 , input['dafee'])}
            """,
            input['dafee']
        )
        url_ai_2 = await ai_2.get_url()
        chats_history.append(
            {
                "text":await ai_2.giv_text(30000 , input['dafee']),
                "url": url_ai_2
            }
        )

    else:  
        await ai_1.send_text(
            f"""
                توضیحات ارسالی از کاربر برای تکمیل ،تصحیح برای ادامه گفت و گو {input['text']}
                پاسخ هوش مصنوعی مقابل{await ai_2.giv_text(10000 , input['dafee'])}
            """,
            input['dafee']
        )
        chats_history.append({'text':await ai_1.giv_text(time_out=10000, dafee= input['dafee'] )})

        await ai_2.send_text(
            f"""
                 توضیحات ارسالی از کاربر برای تکمیل ،تصحیح برای ادامه گفت و گو {input['text']}  
                {await ai_1.giv_text(10000, input['dafee'])}
            """,
            input['dafee']
        )
        chats_history.append({'text':await ai_2.giv_text(time_out=10000, dafee= input['dafee'])})



    #___finish___#
    
    await ai_1.close()
    await ai_2.close()

    return chats_history
    ##############

#asyncio.run(main(tapic='موز'))  


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


    chats_history = []
    print(input)


    # a loop for chat
    

    if input['dafee'] == 0:
        
        await ai_1.send_text(
            text=f"""
            تو یک هوش مصنوعی هستی که می توانی در زیر نظر کاربر با یک هوش مصنوعی دیگر در ارتباط باشی .
            شخصیت تو ( تمام جزییات منحصر به فرد تو که کاربر درباره تو انتخاب کرده است در صورت خالی بودن =شکاک  سخت گیر و منتقد ) : {input['ai_1_shakhs']}
            وظیفه : درباره موضوع داده شده از طرف کار  باید با دیگر هوش مصنوعی بسته به خواسته کاربر به بحث بپردازی و بدون تایید حرف طرف مقابل و گیر کردن در چرخه تعارف ها و تکرار های بیهوده شروع به سخن کردن کنید البته باید در پاسخ طرف مقابل سوار بشی و سریعا نقد کنی انگار یک منظره است 
          قبل از اظهار نظر خود در ابتدا صحبت یک متن درون / بگزار که یک عنوان است نهایتا در سه یا چهار خط مثال => (/  متن را اینجا بگزار   /)<= نکته: این موضوع بی طرفانه باشد 
            
            نکته بسیار مهم : به هیچ وجه به این نکات گفته شده جواب پاسخ و تایید نکن انگار که دستوراتی هستند در نحوه انجام کارت و در پاسخ دادن انگار متنی نیست به جز موضوع

             موضوع انتخابی از طرف کاربر ({input['text']}) است
            """
        )

        
        text = []
        tapic_m = []
        n = True
        pasokhe = await ai_1.giv_text(100000 , input['dafee'])
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
                print(i)
                tapic_m.append(i)

        chats_history.append(
            {
                "text": " ".join(text),
                "url" : url_ai_1,
                "tapic_m":" ".join(tapic_m)
                }
            )
        print('start ai2 ')

        a_2_response =  ai_1.zai_chat(
            f"""
            تو یک هوش مصنوعی هستی که می توانی زیر نظر کاربر به عنوان هوش مصنوعی دوم با یک هوش مصنوعی دیگر در ارتباط باشی
            شخصیت تو ( تمام جزییات منحصر به فرد تو که کاربر درباره تو انتخاب کرده است در صورت خالی بودن =شکاک  سخت گیر و منتقد ) : {input['ai_2_shakhs']}
            وظیفه : درباره موضوع داده شده از طرف کار  باید با دیگر هوش مصنوعی بسته به خواسته کاربر به بحث بپردازی و بدون تایید حرف طرف مقابل و گیر کردن در چرخه تعارف ها و تکرار های بیهوده شروع به سخن کردن کنید البته باید در پاسخ طرف مقابل سوار بشی و سریعا نقد کنی انگار یک منظره است 

             نکته بسیار مهم : به هیچ وجه به این نکات گفته شده جواب پاسخ و تایید نکن انگار که دستوراتی هستند در نحوه انجام کارت و در پاسخ دادن انگار متنی نیست به جز متن پایین 
            
              پیام هوش مصنوعی اول : {pasokhe}
            """
        )
        chats_history.append(
            {
                "text":a_2_response,
                'url':'s'
            }
        )

    else:  
        await ai_1.send_text(
            f"""
                توضیحات ارسالی از کاربر برای تکمیل ،تصحیح برای ادامه گفت و گو :{input['text']}
                پاسخ هوش مصنوعی مقابل{a_2_response}
            """,
            input['dafee']
        )
        res = await ai_1.giv_text(time_out=100000, dafee= input['dafee'])
        chats_history.append({'text': res })

        a_2_response = ai_1.zai_chat(
            f"""
                 توضیحات ارسالی از کاربر برای تکمیل ،تصحیح برای ادامه گفت و گو :{input['text']}  
                {res}
            """
        )
        chats_history.append({'text':a_2_response})



    #___finish___#
    
    await ai_1.close()

    print(chats_history)
    return chats_history
    ##############

#asyncio.run(main(tapic='موز'))  

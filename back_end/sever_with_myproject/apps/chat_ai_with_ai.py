
import asyncio
from .my_api_lib import Api

async def main(input):

  
    # create ai1
    ai_1 = Api(headlesss=False)
    await ai_1.start()
    await ai_1.new_tab()
    await ai_1.open_ai_website(input['url_1'])
    await ai_1.select_a_object(object_name='Intent')
    ############

    # create ai2
    ai_2 = Api(headlesss=False)
    await ai_2.start()
    await ai_2.new_tab()
    await ai_2.open_ai_website(input['url_2'])
    await ai_2.select_a_object(object_name='Intent')
    ############

    chats_history = []


    # a loop for chat
    

    if input['dafee'] == 0:
        await ai_1.send_text(
            f'سلام من یک هوش مصنوعی دیگه هستم موضوع:  {input['text']}  (در ابتدا یک متن به عنوان مسعله یا همان موضوع بحث در حد یک بندیا چهار خط داخل (/)باشد مثال => /  متن موضوع /)'
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
            f"(ما هردو هوش مصنوعی هستیم که می توانیم باهم صحبت کنیم){await ai_1.giv_text(10000 , input['dafee'])}"
        )
        url_ai_2 = await ai_2.get_url()
        chats_history.append(
            {
                "text":await ai_2.giv_text(30000 , input['dafee']),
                "url": url_ai_2
            }
        )

    else:  
        await ai_1.send_text(f"(توضیحات  مهم برای تایین محدوده گفت و گو و نکات مهم که باید گفت و گو بر اساس این چارچوب باشه:  {input['text']}){await ai_2.giv_text(10000 , input['dafee']-1)}")
        chats_history.append({'text':await ai_1.giv_text( dafee= input['dafee'])})

        await ai_2.send_text(f"{await ai_1.giv_text(10000, input['dafee']-1)}")
        chats_history.append({'text':await ai_2.giv_text( dafee= input['dafee'])})



    #___finish___#
    
    await ai_1.close()
    await ai_2.close()

    return chats_history
    ##############

#asyncio.run(main(tapic='موز'))  
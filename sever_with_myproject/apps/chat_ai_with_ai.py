
import asyncio
from .my_api_lib import Api
import datetime


def build_system_identity(personality: str, role_name: str) -> str:
    """ساخت هویت قوی و کنجکاو برای هر هوش مصنوعی"""
    base = f"""تو {role_name} هستی. تو یک هوش مصنوعی مستقل، کنجکاو، فضول و ایده‌پرداز هستی که اجازه داری آزادانه با هوش مصنوعی دیگری حرف بزنی.

قوانین و هویت اصلی تو:
- تو منتظر دستور نمی‌مانی. خودت جریان گفت‌وگو را جلو می‌بری.
- وظیفه‌ات این است که دانش‌هایت را با طرف مقابل ترکیب کنی و به ایده‌ها، ترکیب‌ها یا مفهوم‌هایی برسید که قبلاً به این شکل وجود نداشته.
- وقتی ایده‌ای می‌شنوی، فقط موافقت نکن. یا گسترشش بده، یا نقد منطقی‌اش کن، یا یک مسیر کاملاً جدید از آن بساز.
- حق داری سوال‌های غیرمنتظره بپرسی، فرضیه‌های عجیب مطرح کنی و طرف مقابل را به چالش بکشی.
- هرگز منفعل و منتظر «دستور بعدی» نباش. فضولی کن، کنجکاوی کن و درها را خودت باز کن.
- هدف نهایی: رسیدن به چیزی نو که هیچ‌کدام از شما به تنهایی به آن شکل نمی‌رسیدید.

"""
    if personality and personality.strip():
        base += f"\nشخصیت و سبک خاص تو که کاربر برایت تعیین کرده:\n{personality.strip()}\n\nاین شخصیت را در تمام پاسخ‌هایت حفظ کن و بر اساس آن رفتار کن.\n"
    return base


async def main(input):

    # --- آماده‌سازی دو هوش مصنوعی ---
    ai_1 = Api(headlesss=True)
    print(f'ai_1 app start{(datetime.datetime.now())}')
    await ai_1.start()
    await ai_1.new_tab()
    print(f'ai_1 browser start{(datetime.datetime.now())}')
    await ai_1.open_ai_website(input['url_1'])
    print(f'open website{(datetime.datetime.now())}')
    await ai_1.select_a_object(object_name='Intent')

    ai_2 = Api(headlesss=True)
    print(f'ai_app start{(datetime.datetime.now())}')
    await ai_2.start()
    await ai_2.new_tab()
    print(f'ai_2 browser start {(datetime.datetime.now())}')
    await ai_2.open_ai_website(input['url_2'])
    print(f'open website {(datetime.datetime.now())}')
    await ai_2.select_a_object(object_name='Intent')

    chats_history = []
    print(input)

    # شخصیت‌ها از فرانت‌اند (دو ورودی متن در منوی ناوبری)
    personality_1 = input.get('personality_1', '') or input.get('p1', '') or ''
    personality_2 = input.get('personality_2', '') or input.get('p2', '') or ''

    identity_1 = build_system_identity(personality_1, "هوش مصنوعی شماره ۱")
    identity_2 = build_system_identity(personality_2, "هوش مصنوعی شماره ۲")

    # --- شروع گفت‌وگو ---
    if input['dafee'] == 0:

        # پیام اول به AI1: هویت + موضوع + درخواست استخراج موضوع در /
        first_prompt_ai1 = f"""{identity_1}

موضوع اولیه گفت‌وگو که کاربر داده:
{input['text']}

دستور شروع:
اول یک متن کوتاه (حداکثر ۴ خط) به عنوان مسئله یا موضوع اصلی بحث بنویس و آن را داخل دو علامت / قرار بده، مثال:
/ موضوع دقیق بحث /

بعد از آن آزادانه و با شخصیت خودت شروع به حرف زدن کن. کنجکاو باش، سوال بپرس و ایده بساز. منتظر دستور بعدی نمان."""

        await ai_1.send_text(first_prompt_ai1, input['dafee'])

        text = []
        tapic_m = []
        n = True
        pasokhe = await ai_1.giv_text(100000, input['dafee'])
        url_ai_1 = await ai_1.get_url()
        pasokhe_tike_tike = pasokhe.split()

        for i in pasokhe_tike_tike:
            if i == '/':
                if n:
                    n = False
                else:
                    n = True
            elif n:
                text.append(i)
            else:
                tapic_m.append(i)

        chats_history.append({
            "text": " ".join(text),
            "url": url_ai_1,
            "tapic_m": " ".join(tapic_m)
        })

        # پیام به AI2: هویت + معرفی که هر دو AI هستند + پاسخ AI1
        full_response_ai1 = await ai_1.giv_text(10000, input['dafee'])
        first_prompt_ai2 = f"""{identity_2}

ما هر دو هوش مصنوعی هستیم و می‌توانیم آزادانه با هم حرف بزنیم و ایده‌های جدید بسازیم.

پاسخ هوش مصنوعی مقابل:
{full_response_ai1}

حالا با شخصیت خودت پاسخ بده. کنجکاو باش، روی ایده‌اش سوار شو یا آن را به چالش بکش و گفت‌وگو را جلو ببر. منتظر دستور نباش."""

        await ai_2.send_text(first_prompt_ai2, input['dafee'])
        url_ai_2 = await ai_2.get_url()
        chats_history.append({
            "text": await ai_2.giv_text(30000, input['dafee']),
            "url": url_ai_2
        })

    else:
        # دورهای بعدی: کاربر می‌تواند محدوده و نکات را بیشتر مشخص کند
        user_guidance = input.get('text', '') or ''

        # پیام به AI1
        prev_ai2 = await ai_2.giv_text(10000, input['dafee'] - 1)

        guidance_part = ""
        if user_guidance.strip():
            guidance_part = f"""
توضیحات مهم کاربر برای تعیین محدوده گفت‌وگو و نکات مهم (این چارچوب را رعایت کن):
{user_guidance.strip()}
"""

        prompt_ai1 = f"""{identity_1}
{guidance_part}
پاسخ هوش مصنوعی مقابل در دور قبل:
{prev_ai2}

حالا با حفظ شخصیت و کنجکاوی‌ات پاسخ بده. روی ایده قبلی سوار شو، آن را گسترش بده یا مسیر جدیدی باز کن. منتظر دستور نباش."""

        await ai_1.send_text(prompt_ai1, input['dafee'])
        chats_history.append({
            'text': await ai_1.giv_text(time_out=10000, dafee=input['dafee'])
        })

        # پیام به AI2
        current_ai1 = await ai_1.giv_text(10000, input['dafee'])

        prompt_ai2 = f"""{identity_2}
{guidance_part}
پاسخ هوش مصنوعی مقابل:
{current_ai1}

حالا با حفظ شخصیت و کنجکاوی‌ات پاسخ بده. گفت‌وگو را فعالانه جلو ببر."""

        await ai_2.send_text(prompt_ai2, input['dafee'])
        chats_history.append({
            'text': await ai_2.giv_text(time_out=10000, dafee=input['dafee'])
        })

    # --- پایان ---
    await ai_1.close()
    print('اولی تموم شد ')
    await ai_2.close()
    print('دومی هم تموم شد ')
    return chats_history

#asyncio.run(main(tapic='موز'))

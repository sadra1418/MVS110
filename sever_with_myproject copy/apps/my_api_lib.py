from playwright.async_api import async_playwright

class Api():


    def __init__(self, storage_state="1.json", headlesss=True, channels=None):
        self.storage_state = storage_state
        self.headlesss = headlesss
        self.channels = channels
        self.tab = None
        self.playwrite = None
        self.browser = None
        self.context = None



    async def start(self):
        """start a browaser """
        self.playwrite = await async_playwright().start()
        self.browser = await self.playwrite.chromium.launch(headless=self.headlesss, channel=self.channels)
        self.context = await self.browser.new_context(storage_state=self.storage_state)
        return self
    


    async def close(self):
        """stop the browser"""
        if self.playwrite:
            await self.playwrite.stop()


    async def new_tab(self):
        """create a new tab """
        self.tab = await self.context.new_page()
        return self.tab
    
    async def get_url (self):
        return  self.tab.url

# ai api codes
    async def open_ai_website(self ,url='http://chat.deepseek.com/'):
        await self.tab.goto(url=url, wait_until='commit')



    async def send_text(self, text):

        await self.tab.keyboard.insert_text(text) 
        await self.tab.keyboard.press('Enter')
        await self.tab.wait_for_timeout(10000)



    async def select_a_object(self,text=None, n_selector=None, object_name=None):
        if object_name == 'Expert':
            await self.tab.click('[class="_9f2341b _18572c1"]') 

        elif object_name == 'text_entery':
            await self.tab.click('[class="_27c9245 ds-scroll-area ds-scroll-area--show-on-focus-within ds-scroll-area--enabled d96f2d2a"]')

        elif object_name == 'Intent' :
            pass

        elif object_name == 'Vision' : 
            await self.tab.click('[class="dfb78875"]')
            
        elif n_selector != None:
            return await self.tab.query_selector(n_selector)

        elif text !=None :
            return self.tab.get_by_text(text)
        

            

    async def giv_text(self ,time_out=20000 , dafee = 1 ):
        await self.tab.wait_for_timeout(time_out)
        return await self.tab.inner_text(f'[data-virtual-list-item-key="{(dafee+1)*2}"]' , timeout=9000)
    
    
    
# ai api codes
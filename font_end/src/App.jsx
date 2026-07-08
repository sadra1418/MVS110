
import { useState , useEffect , useRef } from "react";



function App(){

    const [text_tag_input, change_text] = useState('')
    const [issue ,setissue] = useState(null)
    const [dafee ,setdafee] = useState(0)
    const [ai_1_response, set_ai1_response] = useState('')
    const [ai_2_response, set_ai2_response] = useState('')
    const [response, updateres] = useState(null)
    const [url_1, updateurl_1] = useState('https://chat.deepseek.com/')
    const [url_2, updateurl_2] = useState('https://chat.deepseek.com/')


    useEffect(()=>{
        try{
            set_ai1_response(response[0])
            set_ai2_response(response[1])
        }catch{}
        
    },[response])


    const send_data = async() => {
        

        if (dafee===0) {
            const request = (await fetch(
                'http://127.0.0.1:8000/api/',
                {
                    method:'POST',
                    body:JSON.stringify({
                        'text':text_tag_input,
                        'dafee' : dafee,
                        'url_1': url_1,
                        'url_2':url_2
                    })
                }
            ))
            const res = eval(await request.json())
            updateres(res)
            
            updateurl_1(res[0]['url'])
            updateurl_2(res[1]['url'])
            
             
        }else{
            const request = (await fetch(
                'http://127.0.0.1:8000/api/',
                {
                    method:'POST',
                    body:JSON.stringify({
                        'text' : text_tag_input,
                        'url_1':  url_1,
                        'url_2': url_2,
                        'dafee' : dafee,
                    })
                }
            ))
            const res = eval(await request.json())
            console.log(res)
            updateres(res)
            
        }
        setdafee(dafee+1)
        
    }

    return (
        
        <div>
            
            <div className="startpage">
                <input onChange={(e)=>{change_text(e.target.value)}} />
                <button onClick={send_data} >send</button>
                
                
            </div>
            <p className="ai_1">{ai_1_response['text']}</p>
            <p className="ai_2">{ai_2_response['text']}</p>
            <p>دفعه = {dafee}   ادرس ={url_1} , {url_2}</p>
       </div>
    );
};

export default App ;
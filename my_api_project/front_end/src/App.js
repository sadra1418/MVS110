import Api_get from "./compunents/api";
import { useState } from "react";



function App(){

    const [text_tag_input, change_text] = useState('')
    const send_data = () => {
        Api_get(text_tag_input)
    }

    return (
    <div>
        <input  type="text" id="input" onChange={(e)=>{change_text(e.target.value)}} />
        <button onClick={send_data}>send</button>
    </div>);
};

export default App ;
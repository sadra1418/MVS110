import { useState } from "react";

async function Api_get (input){


    const res = await fetch(
        'http://127.0.0.1:8000/api/' ,
        {
            method:'POST',
            body:JSON.stringify(input)
        }
    )

    const test = await res.json()
    console.log(eval(test))

} 
export default Api_get
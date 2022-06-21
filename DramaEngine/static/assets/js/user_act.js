var KeyArr=[];
var GenArr=[];


function inputKey(event){

    if(event.key === "Enter"){

        tt=event.target.id;
        text=document.getElementById(tt).value;
        document.getElementById(tt).value="";

        //如果有輸入東西
        if(text!=""){

            if(tt[0]=="K"){
                console.log("key: "+text);
                KeyArr.push(text);
                localStorage.setItem("key", KeyArr);
                showArray("K");
            }

            else{
                console.log("genre: "+text);
                GenArr.push(text);
                localStorage.setItem("genre", GenArr);
                showArray("G");

            }

        }
        
    }

}


function deletKey(event){

    tt=event.target.id;

    text=tt.split("_");

    if(text[1]=="BKey"){
        KeyArr.splice(parseInt(text[0]), 1);
        showArray("K");
        localStorage.setItem("key", KeyArr);
    }

    else{
        GenArr.splice(parseInt(text[0]), 1);
        showArray("G");
        localStorage.setItem("genre", GenArr);
    }

}

//renew the array
function showArray(t){

    mes="";

    if(t=="K"){

        for(var a=0;a<KeyArr.length;a++){

            mes+='<span id="'+a+'_Key" class="keyarr">'+KeyArr[a]
            +'<button id="'+a+'_BKey" type="button" class="key_C" onclick="deletKey(event)">x</button></span>';
        }

        document.getElementById("Keys_form").innerHTML=mes;

    }

    else{

        for(var a=0;a<GenArr.length;a++){

            mes+='<span id="'+a+'_Gen" class="keyarr">'+GenArr[a]
            +'<button id="'+a+'_BGen" type="button" class="key_C" onclick="deletKey(event)">x</button></span>';
        }
    
        document.getElementById("Genres_form").innerHTML=mes;

    }

}
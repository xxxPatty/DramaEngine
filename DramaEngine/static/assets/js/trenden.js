var periodc=0;
var years=1;


function choose_period(event){
    
    tt=event.target.id;

    temp=tt.split("_");

    

    //更改了period設定
    if(periodc!=parseInt(temp[1])){

        loading_ain("trend_loading");
        
        periodc=parseInt(temp[1]);


        //periodc在這裡才被改成新的值，然後我是從1開始設的沒有弄0

        if(periodc==1){
            get_trend("month", 0);
        }
        else if(periodc==2){
            get_trend("quarter", 0);
        }
        else if(periodc==3){
            get_trend("year", 0);
        }

        for(var a=1;a<=4;a++){

            var test=document.getElementById(temp[0]+"_"+a);
    
            if(a==periodc){
                test.className="period_c sp";
            }
            else{
                test.className="period_n sp";
            }
            years_show();
        }

    }

}


function years_show(){


    var detail=document.getElementById("years_detial");
    var mes="";

    //選years
    if(periodc==4){

        mes+='<input id="years" type="number" value="'+years+'"  min="1" max="100" onchange="change_years(event)">';
        detail.innerHTML=mes;

    }
    //選其他的 years的年份選擇收起來
    else{
        detail.innerHTML=mes;
    }
}

function change_years(event){
    years=document.getElementById("years").value;
    console.log("years: "+years);
    get_trend("years", years);
}

// window.addEventListener("load", testttt, false);
var prefix = "http://192.168.0.171:8082/";
var geners = "get_all_gener";

var buttonArr;

function getGeners(){
    var url = prefix + geners;
    $.ajax({
        url: url, //放你的url
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        
        //如果成功的話
        success: function(data){//這裡拿到的data是一個Object陣列
            console.log(data);
            var result = data.result;
            
            var myButtonHtml = "";
            for(var i=0; i<result.length; i++){
                myButtonHtml += `<div id="${result[i].id}" class="Genres" onclick="clickButton(${result[i].id})">${result[i].name}</div>`;
            }
            document.getElementById("Genres_form").innerHTML = myButtonHtml;
        },
        
        //如果失敗的話
        error: function(){
            console.log("error");
        }
    });
}

function clickButton(id){
    var index = buttonArr.indexOf(id);
    if(index==-1){ //代表原本沒有
        buttonArr.push(id);
    }
    else{ //代表原本有
        buttonArr.splice(index, 1);
    }
    
    console.log(`目前的陣列: `);
    console.log(buttonArr);
}

function start(){
    buttonArr = [];
    getGeners();
}

window.addEventListener("load", start, false);
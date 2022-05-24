var prefix = "http://192.168.0.171:8082/";
var geners = "get_all_gener";


function getGeners(){
    var url = prefix + geners;
    $.ajax({
        url: url, //放你的url
        type: "GET",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        
        //如果成功的話
        success: function(data){//這裡拿到的data是一個Object陣列
            console.log("success");//看到時候有沒有成功
            console.log(data);
            var result = data.result;
            
            var myButtonHtml = "";
            for(var i=0; i<result.length; i++){
                myButtonHtml += `<div id="${result[i].id}" class="Genres">${result[i].name}</div>`;
            }
            document.getElementById("Genres_form").innerHTML = myButtonHtml;
        },
        
        //如果失敗的話
        error: function(){
            console.log("error");
        }
    });
}

function toggleButton(id){

}

function start(){
    getGeners();
}

window.addEventListener("load", start, false);
var prefix = "http://192.168.0.171:8082/";
var geners = "get_all_gener";
var search_by_des = "search_by_description";

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

function search(){
    console.log("開始搜尋");
    var url = prefix + search_by_des;
    var description = document.getElementById("Description").value;

    var e = document.getElementById("type");
    var type = parseInt(e.value);

    var request = {
        "tv_or_movie": type,
        "genres_ids": buttonArr,
        "user_description": description
    };
    console.log("送出去的request: ");
    console.log(request);

    // 開始搜尋
    $.ajax({
        url: url,
        data: JSON.stringify(request),
        type: "POST",
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("搜尋成功，結果為...");
            console.log(response);
            var result = response.result;

            var moviesHtml = "";
            for(var i=0; i<result.length; i++){
                moviesHtml += `<div>${result[i].title}__</div><br>`;
                console.log(`電影結果: ${result[i].title}`);
            }

            if(result.length==0){
                moviesHtml = "無結果";
            }

            document.getElementById("sever_output").innerHTML = moviesHtml;
        },
        error: function(){
            console.log("error");
        }
    });
}

function start(){
    buttonArr = [];
    getGeners();
}

window.addEventListener("load", start, false);
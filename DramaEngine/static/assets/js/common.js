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

function get_trend(method, years){
    //loading_ain("trend_loading");
    var data = {method: method, years: years};
    console.log(data);

    var myURL = prefix + "trend";
    $.ajax({
        url: myURL,
        type: "POST",
        data: JSON.stringify(data),
        async: false,
        dataType: "json",
        contentType: 'application/json; charset=utf-8',
        success: function(response){
            console.log("成功: 拿到最近趨勢（trend）");
            console.log(response);
            result = response.data;
            var temp = "<div class=\"show_movie\">";
            

            for(var i=0; i<result.length; i++){
                var gener_keyword = result[i];
                temp+='<div class="trend">';
                temp += "<h2 style=\"display : inline\">";
                temp += gener_keyword[0];
                temp += "</h2>";
                temp += "<h5 style=\"display : inline\">";
                temp += " （出現"
                temp += gener_keyword[1];
                temp += "次）";
                temp += "</h5>"
                
                //temp += "<br>關鍵字: ";
                temp += "<p>"
                for(var j=0; j<gener_keyword[2].length; j++){
                    temp += gener_keyword[2][j][0];
                    temp += "<br>"
                }
                temp += "</p>"
                temp+='</div>';
            }
            temp += "</div>";
            document.getElementById("trend_loading").innerHTML=temp;
        },
        error: function(response){
            console.log("失敗: 拿到最近趨勢（trend）");
            console.log(response);
        }
    });
}

function clickButton(id){
    var index = buttonArr.indexOf(id);
    if(index==-1){ //代表原本沒有
        buttonArr.push(id);
        document.getElementById(id).className="C_Genres";
    }
    else{ //代表原本有
        buttonArr.splice(index, 1);
        document.getElementById(id).className="Genres";

    }
    
    console.log(`目前的陣列: `);
    console.log(buttonArr);
}

///*
function search(){
    loading_ain("sever_output");
    console.log("開始搜尋");
    var url = prefix + search_by_des;
    var gener = document.getElementById("Genres_user").value;
    var description = document.getElementById("Description").value;

    var request = {
        "user_genres": gener.split(','),
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
            moviesHtml+='<div class="show_movie" id="output_display">';
            for(var i=0; i<result.length; i++){
                moviesHtml += `<div class="movie">${result[i].title}`;
                tt=i.toString();
                var index = favoriteArr.indexOf(tt);
                if(index==-1){ //代表原本沒有
                    moviesHtml += `<i id="${result[i].id}" class="fa fa-heart-o" style="font-size:24px;color:red" onclick="clickLike(event)"></i></div>`;
                }
                else{ //代表原本有
                    
                    moviesHtml += `<i id="${result[i].id}" class="fa fa-heart" style="font-size:24px;color:red" onclick="clickLike(event)"></i></div>`;
                }
                
                console.log(`電影結果: ${result[i].title}`);
            }
            moviesHtml+='</div>';
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
//*/
/*
//測試排版用
function search(){
    var response={result:[{"title":"電影1"},{"title":"電影2"},{"title":"電影3"},{"title":"電影4"},{"title":"電影5"},{"title":"電影6"},{"title":"電影7"},{"title":"電影8"},{"title":"電影9"},{"title":"電影10"},{"title":"電影1"},{"title":"電影2"},{"title":"電影3"},{"title":"電影4"},{"title":"電影5"},{"title":"電影6"},{"title":"電影7"},{"title":"電影8"},{"title":"電影9"},{"title":"電影10"}]};
    result=response.result;

    var moviesHtml = "";
    moviesHtml+='<div class="show_movie" id="output_display">';
            for(var i=0; i<result.length; i++){
                moviesHtml += `<div class="movie">${result[i].title}`;
                tt=i.toString();
                var index = favoriteArr.indexOf(tt);
                if(index==-1){ //代表原本沒有
                    moviesHtml += `<i id="`+i+`" class="fa fa-heart-o" style="font-size:24px;color:red" onclick="clickLike(event)"></i></div>`;
                }
                else{ //代表原本有
                    
                    moviesHtml += `<i id="`+i+`" class="fa fa-heart" style="font-size:24px;color:red" onclick="clickLike(event)"></i></div>`;
                }
                
                console.log(`電影結果: ${result[i].title}`);
            }
            moviesHtml+='</div>';
            if(result.length==0){
                moviesHtml = "無結果";
            }

    document.getElementById("sever_output").innerHTML = moviesHtml;



}
*/

function loading_ain(show_place){
    console.log("要改的地方是"+show_place);
    var mes="";
    var place=document.getElementById(show_place);
    mes='<div class="loader"><span>L</span><span>O</span><span>A</span>'
        +'<span>D</span><span>I</span><span>N</span><span>G</span></div>';
    
    place.innerHTML=mes;

}

function start(){
    buttonArr = [];
    //getGeners();

    loaddata();

    //search();

    

}

window.addEventListener("load", start, false);
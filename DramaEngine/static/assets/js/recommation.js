function getRecommend(){

    //loading_ain("recommend_output");
    console.log("最愛:");
    favoriteArr = [239529, 316873, 77617, 58574, 497582];
    console.log(favoriteArr);

    var data = {movie_id: favoriteArr};
        console.log(data);

        var myURL = prefix + "get_my_favorite";
        $.ajax({
            url: myURL,
            type: "POST",
            data: JSON.stringify(data),
            async: false,
            dataType: "json",
            contentType: 'application/json; charset=utf-8',
            success: function(response){
                console.log("成功: 拿到最愛");
                console.log(response);
                result=response.data;

                var moviesHtml = "";
                moviesHtml+='<div class="show_movie">';
                for(var i=0; i<result.length; i++){
                    moviesHtml += `<div class="movie">${result[i].title}</div>`;
                }

                moviesHtml+='</div>';

                document.getElementById("recommend_output").innerHTML = moviesHtml;
            },
            error: function(response){
                console.log("失敗: 拿到最愛");
                console.log(response);
            }
        });
}

function start(){
    loading_ain("recommend_output");
    getRecommend();

}

window.addEventListener("load", start, false);
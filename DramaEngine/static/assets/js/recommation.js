function getRecommend(){
    console.log("最愛:");
    var myFavorite = [];
    // favoriteArr = [239529, 316873, 77617, 58574, 497582];
    for(var i=0; i<localStorage.length;i++){
        myFavorite.push(parseInt(localStorage.key(i).split(' ')[1]));
    }
    console.log(myFavorite);
    
    var data = {movie_id: myFavorite};
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

function start_recommand(){
    console.log("recommand的start");
    loading_ain("recommend_output");
    setTimeout(() => {
        getRecommend();
    }, 1000);
}

window.addEventListener("load", start_recommand, false);
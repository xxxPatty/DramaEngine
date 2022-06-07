




function getRecommend(){

    var response={result:[{"title":"電影1"},{"title":"電影2"},{"title":"電影3"},{"title":"電影4"},{"title":"電影5"},{"title":"電影6"},{"title":"電影7"},{"title":"電影8"},{"title":"電影9"},{"title":"電影10"},{"title":"電影1"},{"title":"電影2"},{"title":"電影3"},{"title":"電影4"},{"title":"電影5"},{"title":"電影6"},{"title":"電影7"},{"title":"電影8"},{"title":"電影9"},{"title":"電影10"}]};
    result=response.result;

    var moviesHtml = "";
    moviesHtml+='<div class="show_movie">';
    for(var i=0; i<result.length; i++){
        moviesHtml += `<div class="movie">${result[i].title}__</div>`;
    }

    moviesHtml+='</div>';

    document.getElementById("recommend_output").innerHTML = moviesHtml;

}


function start(){

    getRecommend();

}

window.addEventListener("load", start, false);
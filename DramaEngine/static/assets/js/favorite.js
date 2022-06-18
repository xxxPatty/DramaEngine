var favoriteArr=[];


function clickLike(event){

    id=event.target.id;

    //window.alert(id);
    var index = favoriteArr.indexOf(id);
    if(index==-1){ //代表原本沒有
        favoriteArr.push(id);
        document.getElementById(id).className="fa fa-heart";

        localStorage.setItem("like " + id,0);

    }
    else{ //代表原本有
        favoriteArr.splice(index, 1);
        document.getElementById(id).className="fa fa-heart-o";
        localStorage.removeItem("like " + id);

    }

    loaddata();
    
    console.log(`目前的陣列: `);
    console.log(favoriteArr);
}


//更新favorite的在地資訊
function loaddata() {

    var long = localStorage.length;
    favoriteArr=[];
    for (var a = 0; a < long; a++){
        temp=localStorage.key(a);
        if(temp.startsWith('like')){
            favoriteArr.push(temp.substring(5));
        }
    }

    //window.alert(favoriteArr);
}
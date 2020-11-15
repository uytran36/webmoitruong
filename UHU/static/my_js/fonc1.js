function createcard()
{
     //img
    var imgterre = document.createElement('img');
    imgterre.id = " imgterre";
    imgterre.className = "card-img-top";
    imgterre.src = "...";

    //div 4
    var cardbody1 = document.createElement('div');
    cardbody1.className = "card-body";
    //div 4 h5
    var nomterre = document.createElement('h5');
    nomterre.className= "card-title";
    nomterre.id = "nomterre";
    var node_nom = document.createTextNode("Tên loại đất");
    nomterre.appendChild(node_nom);
    cardbody1.appendChild(nomterre);
    //div 4 p
    var infoterre = document.createElement('p');
    infoterre.className = "card-text";
    infoterre.id = "card1infoterre";
    var node_info = document.createTextNode("Mô tả về loại đất đó");
    infoterre.appendChild(node_info);
    cardbody1.appendChild(infoterre);

    //ul
    var ul = document.createElement('ul');
    ul.className="list-group list-group-flush";
    var i;
    var len = 3;
    for (i = 0; i < len; i++) {
        var li = document.createElement('li');
        li.className = "list-group-item list-group-item-success";
        li.id = "jardin";
        var node_li = document.createTextNode("jardin1");
        li.appendChild(node_li);
        ul.appendChild(li);
    }

    // div 5
    var cardbody2 = document.createElement('div');
    cardbody2.className = "card-body";
    //div 5 a
    var cardlink = document.createElement("a");
    cardlink.className= "card-link";
    cardlink.id = "cardlink";
    cardlink.href="#";
    var node_link = document.createTextNode("Plus d'information de terre");
    cardlink.appendChild(node_link);
    cardbody2.appendChild(cardlink);
    
    //div bự 3
    var card = document.createElement("div");
    card.className = "card border-success";
    card.id = "card";

    //div bự 1
    var rowj = document.getElementById('row');
    var colj = document.createElement("div");
    colj.className = "col-6";

    card.appendChild(imgterre);
    card.appendChild(cardbody1);
    card.appendChild(ul);
    card.appendChild(cardbody2);


    colj.appendChild(card);
    var br = document.createElement("br");

    rowj.appendChild(colj);
    colj.appendChild(br);
}

var btn = document.getElementById('button');
btn.addEventListener("click", createcard);

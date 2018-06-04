function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function go()
{
    input = document.getElementById('expressionInput').value
    var http = httpGet("handle/q" + input)
    var holder = document.createElement("pre");
    holder.className = "truth-table-holder";
    textnode = document.createTextNode(http)
    holder.appendChild(textnode);
    showObject(holder);

}


function showObject(object) {
    /* Find the div to hold the object. */
    var target = document.getElementById("table-target");
    
    /* If it already has objects, remove them. */
    while (target.children.length !== 0) {
        target.removeChild(target.children[0]);
    }
    
    /* Install our object in that spot. */
    target.appendChild(object);
}

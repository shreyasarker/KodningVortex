function myFunction() {
    document.getElementById("result1").innerHTML = document.getElementById("title").firstChild.nodeValue;
    document.getElementById("result2").innerHTML = document.getElementById("title").childNodes[0].nodeValue;
}
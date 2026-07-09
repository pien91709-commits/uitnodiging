import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lieveheersbeestje Uitnodiging",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html lang="nl">
<head>

<style>

body{
    margin:0;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(#87CEEB,#dff7c9);
    font-family:Arial,sans-serif;
}

.container{
    position:relative;
    width:420px;
    height:420px;
    margin-top:40px;
}

.invitation{

    position:absolute;
    inset:40px;
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 10px 20px rgba(0,0,0,.2);

    opacity:0;
    transition:1s;
}

.open .invitation{
    opacity:1;
}

.ladybug{

    position:absolute;

    left:50%;
    top:50%;

    transform:translate(-50%,-50%);

    width:220px;
    height:220px;

    cursor:pointer;

}

.head{

    width:80px;
    height:80px;

    background:black;

    border-radius:50%;

    position:absolute;

    left:70px;
    top:-10px;

}

.body{

    width:170px;
    height:170px;

    background:black;

    border-radius:50%;

    position:absolute;

    top:40px;
    left:25px;

}

.line{

    position:absolute;

    width:4px;
    height:170px;

    background:black;

    left:108px;
    top:40px;

    z-index:10;

}

.wing{

    position:absolute;

    width:85px;
    height:165px;

    background:#d91c1c;

    top:43px;

    transition:1s;

}

.left{

    left:25px;

    border-radius:90px 0 70px 70px;

    transform-origin:right center;

}

.right{

    left:110px;

    border-radius:0 90px 70px 70px;

    transform-origin:left center;

}

.open .left{

    transform:rotateY(130deg);

}

.open .right{

    transform:rotateY(-130deg);

}

.spot{

    position:absolute;

    width:18px;
    height:18px;

    background:black;

    border-radius:50%;

}

</style>

</head>

<body>

<div class="container" id="container">

<div class="invitation">

<h1>Je bent uitgenodigd!</h1>

<h2>Insectenfeestje van Marthe en Paulien</h2>

<p><b>Datum:</b> ??? </p>

<p><b>Tijd:</b> ??? </p>

<p><b>Plaats:</b> ??? </p>

<p>Beter dat je er bent xxx</p>

</div>

<div class="ladybug" onclick="openBug()">

<div class="head"></div>

<div class="body"></div>

<div class="line"></div>

<div class="wing left">

<div class="spot" style="top:20px;left:15px;"></div>
<div class="spot" style="top:70px;left:45px;"></div>
<div class="spot" style="top:120px;left:20px;"></div>

</div>

<div class="wing right">

<div class="spot" style="top:20px;left:50px;"></div>
<div class="spot" style="top:70px;left:20px;"></div>
<div class="spot" style="top:120px;left:50px;"></div>

</div>

</div>

</div>

<script>

function openBug(){

document.getElementById("container").classList.toggle("open");

}

</script>

</body>

</html>
"""

components.html(html, height=500, scrolling=False)

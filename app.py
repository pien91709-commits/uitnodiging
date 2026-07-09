import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Lieveheersbeestje uitnodiging",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
    margin:0;
    background:linear-gradient(#8ed6ff,#d9f7b8);
    display:flex;
    justify-content:center;
    align-items:center;
    height:500px;
    font-family:Arial, sans-serif;
}


/* hoofdcontainer */

.container{
    position:relative;
    width:450px;
    height:350px;
}


/* tekst in het lijf */

.message{

    position:absolute;

    width:120px;
    height:130px;

    left:165px;
    top:120px;

    color:white;

    text-align:center;

    font-size:14px;

    opacity:0;

    transition:1s;

    z-index:5;

}


.open .message{

    opacity:1;

}


/* lieveheersbeestje */

.ladybug{

    position:absolute;

    width:300px;
    height:250px;

    left:75px;
    top:50px;

    cursor:pointer;

}


/* zwart lijf */

.body{

    position:absolute;

    width:160px;
    height:180px;

    background:#111;

    border-radius:80px;

    left:70px;
    top:40px;

    z-index:3;

}


/* hoofd */

.head{

    position:absolute;

    width:80px;
    height:80px;

    background:#111;

    border-radius:50%;

    left:110px;
    top:0;

    z-index:4;

}


/* middenstreep */

.line{

    position:absolute;

    width:5px;
    height:170px;

    background:black;

    left:148px;
    top:45px;

    z-index:6;

}


/* vleugels */

.wing{

    position:absolute;

    width:120px;
    height:180px;

    background:#e32626;

    top:40px;

    transition:1s ease;

    z-index:2;

}


/* links */

.left{

    left:75px;

    border-radius:90px 20px 20px 90px;

}


/* rechts */

.right{

    left:155px;

    border-radius:20px 90px 90px 20px;

}



/* horizontaal openen */

.open .left{

    transform:translateX(-110px);

}


.open .right{

    transform:translateX(110px);

}



/* stippen */

.spot{

    position:absolute;

    width:22px;
    height:22px;

    background:black;

    border-radius:50%;

}

</style>

</head>


<body>


<div class="container" id="bug">


<div class="message">

<b>🎉 Feestje! 🎉</b>

<br><br>

Emma wordt 6 jaar!

<br><br>

📅 15 augustus

<br>

⏰ 14:00 uur

<br>

📍 Speeltuin

<br><br>

Kom je ook? ❤️

</div>



<div class="ladybug" onclick="openBug()">



<div class="wing left">

<div class="spot" style="top:30px;left:35px;"></div>
<div class="spot" style="top:90px;left:65px;"></div>

</div>



<div class="wing right">

<div class="spot" style="top:30px;right:35px;"></div>
<div class="spot" style="top:90px;right:65px;"></div>

</div>



<div class="body"></div>

<div class="head"></div>

<div class="line"></div>


</div>


</div>



<script>

function openBug(){

document.getElementById("bug").classList.toggle("open");

}

</script>


</body>

</html>
"""


components.html(
    html,
    height=500,
    scrolling=False
)

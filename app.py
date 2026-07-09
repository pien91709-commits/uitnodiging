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

body {
    margin:0;
    background:white;
    display:flex;
    justify-content:center;
    align-items:center;
    height:650px;
    font-family:Arial, sans-serif;
}


/* hoofd */

.container {
    position:relative;
    width:600px;
    height:500px;
}


/* lieveheersbeestje */

.ladybug {

    position:absolute;

    width:360px;
    height:360px;

    left:120px;
    top:80px;

    cursor:pointer;

}


/* zwart lichaam */

.body {

    position:absolute;

    width:240px;
    height:270px;

    background:#111;

    border-radius:50%;

    left:60px;
    top:70px;

    z-index:1;

}


/* kop */

.head {

    position:absolute;

    width:110px;
    height:110px;

    background:#111;

    border-radius:50%;

    left:125px;
    top:5px;

    z-index:2;

}


/* tekst */

.message {

    position:absolute;

    width:170px;

    left:95px;
    top:145px;

    color:white;

    text-align:center;

    font-size:16px;

    line-height:1.3;

    opacity:0;

    transition:0.8s;

    z-index:4;

}


.open .message {

    opacity:1;

}


/* middenlijn */

.line {

    position:absolute;

    width:6px;

    height:260px;

    background:#000;

    left:177px;

    top:75px;

    z-index:3;

}


/* vleugels */

.wing {

    position:absolute;

    width:135px;

    height:270px;

    background:#e32626;

    top:70px;

    transition:1s ease;

    z-index:5;

}


/* linker vleugel */

.left {

    left:60px;

    border-radius:135px 20px 20px 135px;

}


/* rechter vleugel */

.right {

    left:165px;

    border-radius:20px 135px 135px 20px;

}



/* open beweging horizontaal */

.open .left {

    transform:translateX(-150px);

}


.open .right {

    transform:translateX(150px);

}



/* zwarte stippen */

.spot {

    position:absolute;

    width:25px;

    height:25px;

    background:black;

    border-radius:50%;

}


</style>

</head>


<body>


<div class="container" id="bug">


<div class="ladybug" onclick="openBug()">



<div class="message">

<b>🎉 Uitnodiging 🎉</b>

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



<div class="wing left">

<div class="spot" style="top:40px;left:45px;"></div>
<div class="spot" style="top:120px;left:80px;"></div>
<div class="spot" style="top:200px;left:40px;"></div>

</div>



<div class="wing right">

<div class="spot" style="top:40px;right:45px;"></div>
<div class="spot" style="top:120px;right:80px;"></div>
<div class="spot" style="top:200px;right:40px;"></div>

</div>



<div class="body"></div>

<div class="head"></div>

<div class="line"></div>


</div>


</div>



<script>

function openBug(){

document
.getElementById("bug")
.classList.toggle("open");

}

</script>


</body>
</html>
"""


components.html(
    html,
    height=650,
    scrolling=False
)

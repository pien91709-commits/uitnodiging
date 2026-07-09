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
    background:white;
    height:700px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-family:Arial;
}


.container{
    position:relative;
    width:600px;
    height:600px;
}


/* tekst achter de vleugels */

.message{

    position:absolute;

    width:220px;
    height:180px;

    left:190px;
    top:270px;

    color:white;

    text-align:center;

    font-size:18px;

    line-height:1.4;

    opacity:0;

    transition:0.8s;

    z-index:2;
}


.open .message{
    opacity:1;
}



/* lieveheersbeestje */

.bug{

    position:absolute;

    width:420px;
    height:420px;

    left:90px;
    top:80px;

    cursor:pointer;

}



/* zwarte lichaam */

.body{

    position:absolute;

    width:360px;
    height:330px;

    background:#111;

    border-radius:50%;

    left:30px;
    top:90px;

    z-index:1;

}



/* rode schildvleugels */

.wing{

    position:absolute;

    width:180px;
    height:330px;

    background:#f22222;

    top:90px;

    transition:1s ease;

    z-index:5;

}


/* links */

.left{

    left:30px;

    border-radius:180px 0 0 180px;

    transform-origin:right center;

}


/* rechts */

.right{

    left:210px;

    border-radius:0 180px 180px 0;

    transform-origin:left center;

}


/* openklappen */

.open .left{

    transform:translateX(-170px) rotate(-10deg);

}


.open .right{

    transform:translateX(170px) rotate(10deg);

}


/* zwarte middenlijn */

.line{

    position:absolute;

    width:8px;

    height:300px;

    background:black;

    left:206px;

    top:105px;

    z-index:7;

}


/* kop */

.head{

    position:absolute;

    width:170px;

    height:120px;

    background:black;

    border-radius:90px 90px 50px 50px;

    left:125px;

    top:0;

    z-index:8;

}


/* stippen */

.spot{

    position:absolute;

    width:35px;

    height:35px;

    background:black;

    border-radius:50%;

}



/* antennes */

.antenna{

    position:absolute;

    width:80px;

    height:5px;

    background:black;

    top:15px;

}


</style>

</head>


<body>


<div class="container" id="bug">


<div class="bug" onclick="openBug()">



<div class="message">

<b>🎉 Uitnodiging 🎉</b>

<br><br>

Emma wordt 6 jaar!

<br>

📅 15 augustus

<br>

⏰ 14:00 uur

<br>

📍 Speeltuin

<br><br>

Kom je ook? ❤️

</div>



<div class="body"></div>



<div class="wing left">

<div class="spot" style="top:80px;left:50px;"></div>
<div class="spot" style="top:170px;left:90px;"></div>
<div class="spot" style="top:250px;left:55px;"></div>

</div>



<div class="wing right">

<div class="spot" style="top:80px;right:50px;"></div>
<div class="spot" style="top:170px;right:90px;"></div>
<div class="spot" style="top:250px;right:55px;"></div>

</div>



<div class="line"></div>


<div class="head"></div>



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


components.html(html,height=700)

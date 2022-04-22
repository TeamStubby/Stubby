console.log(10)

function next(){
    document.getElementById("head").innerHTML = "What do you want to add to your website?";
    document.getElementById("content").innerHTML = " <input type='text' placeholder='Recomended for you'> "
    document.getElementById("exapmles").innerHTML = " <p id='exp'>EXAPLES</p> <p class='fill'>Events</p> <p class='fill'>Online Store</p> <p class='fill'>Pricing Plan</p> <p class='fill'>Forms</p> <p class='fill'>Instagram Feed</p> <p class='fill'>Music</p> <p class='fill'>Online Program</p>  <p class='fill'>Groups</p> <p class='fill'>Food Order</p> </div> "
    document.getElementById("navigate").innerHTML = "<p id='back' onclick='back()'>BACK</p> <p id='skip' onclick='next2()'>SKIP</p>"
    document.getElementById("btn").innerHTML = "<button id='btn' href='template.html' onclick='next2()'>Next</button>"
}

function back(){
    document.getElementById("head").innerHTML = "What kind of website are you creating?";
    document.getElementById("content").innerHTML = " <input type='text' placeholder='Search for your business or website type'> "
    document.getElementById("exapmles").innerHTML = " <p id='exp'>EXAPLES</p>  <p class='fill'>Online Store</p>  <p class='fill'>Portfolio</p>  <p class='fill'>Blog</p>  <p class='fill'>Consultant</p>  <p class='fill'>Technology Company</p> "
    document.getElementById("main").style.display = "block";
    document.getElementById("flex").style.display = "none";
}

function next2(){
    document.getElementById("main").style.display = "none";
    document.getElementById("flex").style.display = "flex";
    console.log(10);
}
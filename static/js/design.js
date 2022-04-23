var dropdown = document.getElementsByClassName("dropdown-btn");
  var i;
  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
    dropdownContent.style.display = "none";
    } else {
    dropdownContent.style.display = "block";
    }
    });
  }
  
  function openNav() {
    document.getElementById("mySidenav").style.width = "230px";
  }
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }
  function openNav2() {
    document.getElementById("Side_opening").style.width = "250px";
    document.getElementById("mySidenav").style.width = "0";
  }
  function closeNav2() {
    document.getElementById("Side_opening").style.width = "0";
  }
  function drag_start(event) {
    var style = window.getComputedStyle(event.target, null);
    var str = (parseInt(style.getPropertyValue("left")) - event.clientX) + ',' + (parseInt(style.getPropertyValue("top")) - event.clientY) + ',' + event.target.id;
    event.dataTransfer.setData("Text", str);
}
function drop(event) {
    var offset = event.dataTransfer.getData("Text").split(',');
    var dm = document.getElementById(offset[2]);
    dm.style.left = (event.clientX + parseInt(offset[0], 10)) + 'px';
    dm.style.top = (event.clientY + parseInt(offset[1], 10)) + 'px';
    event.preventDefault();
    return false;
}
function drag_over(event) {
    event.preventDefault();
    return false;
}
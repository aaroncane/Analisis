var hamburger_menu;


function declare(){

    hamburger_menu = document.querySelector('.hamburger-menu');
}


function events(){

    hamburger_menu.addEventListener("click",()=>{
        big_wrapper.classList.toggle("active");
        console.log("gola");

    });
}

events();
/*==================================================
                DOCUMENT READY
==================================================*/

document.addEventListener("DOMContentLoaded", function () {

    loader();

    stickyNavbar();

    modernNavbar();

    scrollTopButton();

    smoothScroll();

    activeNavigation();

    revealElements();

    validateForms();

    initializeTooltips();

    initializePopovers();

    updateYear();

});


/*==================================================
                LOADER
==================================================*/

function loader() {

    const loader = document.getElementById("loader");

    if (!loader) return;

    window.addEventListener("load", function () {

        setTimeout(function () {

            loader.style.opacity = "0";

            loader.style.visibility = "hidden";

        }, 500);

    });

}


/*==================================================
                STICKY NAVBAR
==================================================*/

function stickyNavbar() {

    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    window.addEventListener("scroll", function () {

        if (window.scrollY > 50) {

            navbar.classList.add("shadow");

            navbar.style.padding = "10px 0";

        }

        else {

            navbar.classList.remove("shadow");

            navbar.style.padding = "15px 0";

        }

    });

}
/*==================================================
            MODERN NAVBAR
==================================================*/

function modernNavbar(){

    const navbar=document.querySelector(".custom-navbar");

    if(!navbar) return;

    window.addEventListener("scroll",function(){

        if(window.scrollY>60){

            navbar.classList.add("scrolled");

        }

        else{

            navbar.classList.remove("scrolled");

        }

    });

}

/*==================================================
                SCROLL TO TOP
==================================================*/

function scrollTopButton() {

    const button = document.getElementById("scrollTop");

    if (!button) return;

    window.addEventListener("scroll", function () {

        if (window.pageYOffset > 300) {

            button.style.display = "flex";

        }

        else {

            button.style.display = "none";

        }

    });

    button.addEventListener("click", function () {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}
/*==================================================
                SMOOTH SCROLL
==================================================*/

function smoothScroll() {

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            const target = document.querySelector(this.getAttribute("href"));

            if (!target) return;

            e.preventDefault();

            target.scrollIntoView({

                behavior: "smooth",

                block: "start"

            });

        });

    });

}


/*==================================================
                ACTIVE NAVIGATION
==================================================*/

function activeNavigation() {

    const currentPath = window.location.pathname;

    document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {

        const href = link.getAttribute("href");

        if (href === currentPath) {

            link.classList.add("active");

        }

    });

}


/*==================================================
                COUNTER ANIMATION
==================================================*/

function animateCounters() {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.getAttribute("data-target"));

        const speed = 200;

        let count = 0;

        const increment = target / speed;

        const update = () => {

            count += increment;

            if (count < target) {

                counter.innerText = Math.ceil(count);

                requestAnimationFrame(update);

            }

            else {

                counter.innerText = target;

            }

        };

        update();

    });

}

window.addEventListener("load", animateCounters);
/*==================================================
                FADE-IN ANIMATION
==================================================*/

function revealElements() {

    const elements = document.querySelectorAll(".fade-up");

    const observer = new IntersectionObserver(function(entries){

        entries.forEach(function(entry){

            if(entry.isIntersecting){

                entry.target.classList.add("show");

            }

        });

    },{

        threshold:0.15

    });

    elements.forEach(function(element){

        observer.observe(element);

    });

}

document.addEventListener("DOMContentLoaded", revealElements);


/*==================================================
                FORM VALIDATION
==================================================*/

function validateForms(){

    const forms=document.querySelectorAll(".needs-validation");

    forms.forEach(function(form){

        form.addEventListener("submit",function(event){

            if(!form.checkValidity()){

                event.preventDefault();

                event.stopPropagation();

            }

            form.classList.add("was-validated");

        },false);

    });

}

document.addEventListener("DOMContentLoaded",validateForms);


/*==================================================
                TOOLTIP INITIALIZATION
==================================================*/

function initializeTooltips(){

    const tooltipTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

    tooltipTriggerList.map(function(tooltipTriggerEl){

        return new bootstrap.Tooltip(tooltipTriggerEl);

    });

}

document.addEventListener("DOMContentLoaded",initializeTooltips);


/*==================================================
                POPOVER INITIALIZATION
==================================================*/

function initializePopovers(){

    const popoverTriggerList=[].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));

    popoverTriggerList.map(function(popoverTriggerEl){

        return new bootstrap.Popover(popoverTriggerEl);

    });

}

document.addEventListener("DOMContentLoaded",initializePopovers);


/*==================================================
                CURRENT YEAR
==================================================*/

function updateYear(){

    const year=document.getElementById("currentYear");

    if(year){

        year.textContent=new Date().getFullYear();

    }

}

document.addEventListener("DOMContentLoaded",updateYear);


/*==================================================
                END
==================================================*/
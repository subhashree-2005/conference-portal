// =========================================
// HERO COUNTDOWN
// =========================================

const conferenceDate = new Date("July 20, 2027 09:00:00").getTime();

function updateCountdown() {

    const now = new Date().getTime();

    const distance = conferenceDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));

    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (document.getElementById("days")) {

        document.getElementById("days").innerHTML = days;
        document.getElementById("hours").innerHTML = hours;
        document.getElementById("minutes").innerHTML = minutes;
        document.getElementById("seconds").innerHTML = seconds;

    }

}

setInterval(updateCountdown,1000);

updateCountdown();


// =========================================
// STATISTICS COUNTER
// =========================================

const counters = document.querySelectorAll(".stat-box h2");

const speed = 40;

counters.forEach(counter=>{

    const animate=()=>{

        const value=+counter.innerText.replace("+","");

        const data=+counter.getAttribute("data-count") || value;

        const time=+counter.innerText.replace("+","");

        const increment=Math.ceil(data/speed);

        if(time<data){

            counter.innerText=time+increment+"+";

            setTimeout(animate,40);

        }

        else{

            counter.innerText=data+"+";

        }

    };

    animate();

});


// =========================================
// SMOOTH SCROLL
// =========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        const target=document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});


// =========================================
// NAVBAR COLOR CHANGE
// =========================================

window.addEventListener("scroll",()=>{

const navbar=document.querySelector(".custom-navbar");

if(!navbar) return;

if(window.scrollY>100){

navbar.style.background="#081938";

navbar.style.padding="10px 0";

}

else{

navbar.style.background="rgba(8,25,56,.92)";

navbar.style.padding="15px 0";

}

});


// =========================================
// SCROLL TO TOP
// =========================================

const topBtn=document.getElementById("scrollTop");

window.onscroll=function(){

    if(document.body.scrollTop>300 || document.documentElement.scrollTop>300){

        topBtn.style.display="block";

    }

    else{

        topBtn.style.display="none";

    }

};

if(topBtn){

topBtn.onclick=function(){

window.scrollTo({

top:0,

behavior:"smooth"

});

};

}


// =========================================
// FADE IN ANIMATION
// =========================================

const observer=new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

document.querySelectorAll("section").forEach((section)=>{

    observer.observe(section);

});
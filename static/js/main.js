// Slider Swiper
var sliderSwiper = new Swiper(".sliderSwiper", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

    effect: "creative",
    creativeEffect: {
        prev: {
            shadow: true,
            translate: ["-20%", 0, -1],
        },
        next: {
            translate: ["100%", 0, 0],
        },
    },

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
});

// Aside Swiper
var asideSwiper = new Swiper(".asideSwiper", {
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
});

// Navbar clock -----------------------------
// function showTime() {
//     var date = new Date();
//     var h = date.getHours();
//     var m = date.getMinutes();
//     var s = date.getSeconds();
//     var session = "AM";

//     if (h == 0) {
//         h = 12;
//     }

//     if (h > 12) {
//         h = h - 12;
//         session = "PM";
//     }

//     h = h < 10 ? "0" + h : h;
//     m = m < 10 ? "0" + m : m;
//     s = s < 10 ? "0" + s : s;

//     var time = h + ":" + m + ":" + s + " " + session;
//     document.getElementById("digitalClock").innerText = time;
//     document.getElementById("digitalClock").textContent = time;

//     setTimeout(showTime, 1000);
// }

// showTime();

// Hajj Music Control
var music = document.getElementById("music");
music.volume = 0.2;
var playMusicButton = document.getElementById("play-music-button");
var icon = document.getElementById("icon");

function playAudio() {
    if (music.paused) {
        music.play();
        icon.classList.remove("fa-play");
        icon.classList.add("fa-pause");
    } else {
        music.pause();
        icon.classList.remove("fa-pause");
        icon.classList.add("fa-play");
    }
}

playMusicButton.addEventListener("click", playAudio);

// music.addEventListener("ended", function () {
//     icon.classList.remove("fa-pause");
//     icon.classList.add("fa-play");
// });
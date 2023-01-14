
const Alert = () => alert('pehuu')
const Alert2 = () => alert('weeeeee')
const Alert3 = () => alert('qqq')


const scrolltext = document.getElementsByClassName('notification-title')[0];
const nt = document.getElementById('nt');

if (nt) {
    window.addEventListener('scroll', () => {
        const winhei = window.innerHeight;
        const curhei = pageYOffset;

        const result = Math.round(10 * curhei / winhei)

        nt.style.transform = `translateX(-${result}%)`
    })
} else {
    null
}

function changeImage(e) {
    const imgs = document.querySelector('#sec-sc').children;
    document.getElementById('main').src = e.src;

    if (imgs) {
        for (let i = 0; i < imgs.length; i++) {
            imgs[i].classList.remove('active-s')
        }
        e.classList.add('active-s')
    }
    else {
        null
    }
}


const imgs = document.querySelectorAll('.imgs');
let result = Math.ceil(imgs.length / 2);






const message = document.getElementById('msg').textContent;
const runmsg = () => {
    const msgCont = document.getElementById('msg-cont');
    if (message) {
        msgCont.style.display = "flex"
    } else {
        msgCont.style.display = "none"
    }

    setTimeout(() => {
        msgCont.style.display = "none"
    }, 2000)

}

if (message) runmsg();



const allopts = document.querySelectorAll('.isec') || [];
const allsecs = document.querySelectorAll('.prod') || [];
allopts.forEach((opt) => {
    opt.addEventListener('click', () => {
        allopts.forEach((ot) => ot.classList.remove('selected'));
        allsecs.forEach((s) => {
            s.classList.add('hide')
            if(opt.textContent === s.id){
                s.classList.remove('hide')
            }
        });
        opt.classList.add("selected");
    })
})




const more = document.querySelectorAll('.more') || [];

more.forEach((item) => {
    let toggle = false;
    item.addEventListener('click', () => {
        const clamp = item.getElementsByClassName('desc')[0];
        const whitearea = item.getElementsByClassName('whiteshade')[0];
        if(toggle == false){
            toggle = true;
            clamp.style.setProperty('--clamp', 0);
            whitearea.style.display = "none";
        }else{
            toggle = false;
            clamp.style.setProperty('--clamp', 2);
            whitearea.style.display = "flex";
        }
    })
})

const filter = document.getElementsByClassName('filter')[0] || "";
console.log(filter)
let dist = filter.getBoundingClientRect().top;
document.addEventListener('scroll', () => {
    if(window.scrollY >= dist){
        filter.style.position = "fixed";
    }else{
        filter.style.position = "unset";   
    }
})
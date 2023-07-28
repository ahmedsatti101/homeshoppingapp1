function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btns = document.querySelectorAll(".productContainer button")

btns.forEach(btn=>{
    btn.addEventListener("click", addToBasket)
})

function addToBasket(e){
    let product_id = e.target.value
    let url  = "/add-to-basket"

    let data = {id: product_id}

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            body: JSON.stringify(data),
            "X-CSRFToken": csrftoken
        }
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
        })
    })
    .catch(err=>{
        console.log(err)
    })
}
async function handleSubmit(event) {
    event.preventDefault();
    var form = event.currentTarget
    var button = form.querySelector('button')
    var originalText = button.innerHTML
    var status = form.querySelector('#status')
    status.innerHTML = ""
    button.innerHTML = "Submitting..."
    var data = new FormData(event.target);
    debugger;
    fetch(event.target.action, {
        method: form.method,
        body: data,
        headers: {
            'Accept': 'application/json'
        }
    }).then(response => {
        if (response.ok) {
            button.innerHTML = "Submitted";
            button.disabled = true;
            form.reset()
        } else {
            button.innerHTML = originalText
            response.json().then(data => {
                if (Object.hasOwn(data, 'errors')) {
                    status.innerHTML = data["errors"].map(error => error["message"]).join(", ")
                } else {
                    status.innerHTML = "Oops! There was a problem submitting your form"
                }
            })
        }
    }).catch(error => {
        button.innerHTML = originalText
        status.innerHTML = "Oops! There was a problem submitting your form"
    });
}

document.addEventListener("DOMContentLoaded", function() {
    // Animate classes
    const elementsToAnimate = document.querySelectorAll('section:not(#hero), section:not(#hero) h2,  .need-solution-pair, .service-item, .bio-container, .book-covers');

    const options = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, options);

    elementsToAnimate.forEach(element => {
        element.classList.add('hidden'); // Add hidden class initially
        observer.observe(element);
    });

    // set up form submission
    var contact_form = document.getElementById("contact");
    var subscribe_form = document.getElementById("subscribe");
    contact_form.addEventListener("submit", handleSubmit)
    subscribe_form.addEventListener("submit", handleSubmit)
});


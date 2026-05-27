// Use AJAX to submit forms
function setFormSourceToCurrentUrl(form) {
    var source = form.querySelector('input[name="source"]')
    if (source) source.value = window.location.href
}

async function handleSubmit(event) {
    event.preventDefault();
    var form = event.currentTarget
    setFormSourceToCurrentUrl(form)
    var button = form.querySelector('button')
    var originalText = button.innerHTML
    var status = form.querySelector('#status')
    if (status) status.innerHTML = ""
    button.innerHTML = "Submitting..."
    var data = new FormData(event.target);
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
            if (status) status.innerHTML = "Thanks — your message was sent."
        } else {
            button.innerHTML = originalText
            response.json().then(data => {
                if (Object.hasOwn(data, 'errors')) {
                    if (status) status.innerHTML = data["errors"].map(error => error["message"]).join(", ")
                } else {
                    if (status) status.innerHTML = "Oops! There was a problem submitting your form"
                }
            })
        }
    }).catch(error => {
        button.innerHTML = originalText
        if (status) status.innerHTML = "Oops! There was a problem submitting your form"
    });
}

// make sections on page animate
document.addEventListener("DOMContentLoaded", function() {
    // "pull up" animations for each section
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
    if (contact_form) {
        setFormSourceToCurrentUrl(contact_form)
        contact_form.addEventListener("submit", handleSubmit)
    }
    if (subscribe_form) subscribe_form.addEventListener("submit", handleSubmit)
});

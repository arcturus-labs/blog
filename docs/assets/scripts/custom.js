document.addEventListener("DOMContentLoaded", function() {
    // Select all elements with the class names you want to animate
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
});
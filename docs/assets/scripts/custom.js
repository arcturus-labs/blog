document.addEventListener('DOMContentLoaded', function() {
    const headerTitle = document.querySelector('.md-header__title');
    if (headerTitle) {
        headerTitle.addEventListener('click', function() {
            window.location.href = '/';
        });
    }
});
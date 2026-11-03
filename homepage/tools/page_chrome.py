"""Apply approved booking and footer chrome to story pages without editing story copy."""
def apply_story_chrome(html):
    html = html.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="styles.css">\n  <link rel="stylesheet" href="story-chrome.css">', 1)
    html = html.replace('src="sky.js"', 'src="home-sky.js"', 1)
    html = html.replace('<body>', '<body class="story-chrome">\n<a class="book-tab" href="https://calendly.com/jfberryman/15min" target="_blank" rel="noopener">Book a call</a>', 1)
    html = html.replace('../draft_site/index.html', 'index.html')
    linkedin = '<a href="https://www.linkedin.com/in/john-berryman-864b1713/">LinkedIn</a>'
    html = html.replace(linkedin, '<a href="https://www.youtube.com/@Arcturus-Labs">YouTube</a>' + linkedin, 1)
    return html

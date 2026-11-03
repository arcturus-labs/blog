# How to interrogate a page's interactivity

Screenshots show states, not behavior. This is how I worked out what a page does when you hover or click, using the browser tool's in-page JavaScript. Limits: I use scripted pointer input, not a human hand, so some effects don't fire the same way (see mamuso below).

## Method
1. **Identify the element and its neighbors.** Print `outerHTML`, the ancestors' classes, `getBoundingClientRect()`, `position`, `pointer-events`, and which element is actually at the center (`document.elementFromPoint`). Overlay links, canvases, and hidden buttons show up here.
2. **Read the cursor.** `getComputedStyle(el).cursor` on the element, its parents, and `body`. A custom cursor is just a `cursor: url(...) x y, fallback` rule; fetch the SVG to see it.
3. **Find the rules that run on hover.** Walk `document.styleSheets`/`cssRules`, including `@media` and `@keyframes`, and keep rules whose selector contains the component's class plus `:hover`, `:focus-visible`, or `:has`. This shows whether it is pure CSS and what media gate applies (for example `(hover: hover) and (pointer: fine)`).
4. **Sample the animation.** Before hovering, start a `requestAnimationFrame` loop that records computed `transform`, `scale`, `opacity`, `border-radius`, `width`, and `getBoundingClientRect()` of each piece. Hover with a real pointer action, then diff the series against the first frame to get from/to values and timing.
5. **Check for JS-driven effects.** Look for elements named like `follow-cursor`, canvases (`getContext`), library globals (`gsap`, `lenis`, `THREE`, `Webflow`), and whether `document.getAnimations()` is empty (CSS transitions would appear; an empty list suggests a JS or WebGL loop).
6. **For WebGL scenes:** dispatch pointer events on the canvas and watch `canvas.style.cursor` (hit-testing usually sets it); look for accessible DOM twins (buttons, aria labels); hook `requestAnimationFrame` to count frames (a low count means draw-on-demand).

Worked examples are in `cases/`. This method was used for every case there (measured on 2026-10-29).

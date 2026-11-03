# ponder.ai, "How Ponder works" (pinned steps on the left, scrubbed scenes on the right)
Screenshots: `../screenshots/ponder-how-it-works/` (step 1 at 150px and step 2 at 330px into their pinned windows). Source read as text from `/_astro/HowItWorks.astro_astro_type_script_index_0_lang.*.js` (about 11 KB). The site is Astro with a bundled GSAP (ScrollTrigger and ScrollTo plugins) and Lenis smooth scrolling.

**Layout (CSS):** `.sides_process` is a flex row: `.left_steps` (45%) holds `.sticky_left` (`position: sticky; top: 0; height: 100vh`); `.right_visuals` (55%) holds four `.container_st` blocks (each tagged `data-step` 1-4 and `data-motion` = layers / cards / call / reveal). Inside each container, `.visual_step` is a viewport-tall box set by JavaScript to `position: sticky; top: 0; overflow: hidden`. So nothing is "pinned" by a library: the left column and each scene are plain CSS sticky; the containers' heights decide how long each scene stays pinned.

**Scroll budget per step:** the script sets each container's height to the viewport height times {1: 1.5, 2: 2, 3: 2.5, 4: 1.5}. A scene stays pinned for container height minus viewport height: 360px, 720px, 1,080px, and 360px at 720px high (5,400px for the whole section). Longer, busier scenes get more scrolling.

**Progress and animation:** for each container the script creates a GSAP ScrollTrigger (`start: "top top"`, `end: "bottom top"`, `scrub: 0.5`). `onUpdate` converts scroll position into a single progress number from 0 to 1 over the pinned window, then calls one small function per scene that sets inline styles (transform, opacity, blur, SVG stroke offsets, text) from that number alone:
- layers: six layers fly in from corners, merge, then shrink away (with blur).
- cards: three clip cards slide into timeline slots and the timeline fades in.
- call: a cursor follows a scripted path, draws a circle and a strike-through (SVG stroke-dashoffset), words appear on a timeline, and a "Send" button reads "Sending…" at the end.
- reveal: the final frame and its changes scale up and fade in, one after another.
- step 1 also types the prompt into the box, character by character, tied to scroll progress.
All of these finish at 62% of the pinned window (`_ = 0.62`), leaving the last 38% as a hold so the finished picture can be read. I confirmed by measurement that the animation changes with scroll position and does not change while the scroll is held still.

**Active step:** `ScrollTrigger` `onEnter`/`onEnterBack` calls an `activate(step)` function when the container's top reaches the top of the viewport (I measured the flip within 8px of 0 in both directions, with no hysteresis). `activate` toggles `is-active` on the step list and the step circles, and opens the active step's description by setting its `max-height` to its `scrollHeight` (0 for others), so inactive steps collapse to one line.

**Progress ring and clicking:** each step circle at the bottom has a ring (`.ring-progress`) whose `stroke-dashoffset` is the step's progress. Clicking a step (list or circle) runs a GSAP `scrollTo` (0.8s, `power2.out`) to the 31% point of that step's pinned window, where that scene is mostly built; a lock variable prevents the highlight from flickering while it travels.

**Mobile (under 768px):** the steps become a sticky bar at the top (35vh, with a gradient fade) showing only the active step; triggers use different start and end points, and a "top content" strip slides in only while the section is on screen.

**Reduced motion:** in this file I found a `prefers-reduced-motion` check only for the audio-meter animation in the "call" scene. I did not verify what happens to the scrubbed animations for people who prefer reduced motion.

**Cost of the pattern:** it needs about 11 KB of custom script plus GSAP and ScrollTrigger, JavaScript-set heights, and layout reads on each update in two scenes.

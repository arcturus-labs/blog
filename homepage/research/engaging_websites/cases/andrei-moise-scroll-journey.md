# andreimoise.ai: a scroll-driven particle journey

Captured at 1280x720, scrolling 360px (half a screen) at a time, 900 ms pause per stop, 7,016px total. Screenshots: `../screenshots/andrei-moise/yNNNN.png`, where NNNN is the scroll position in px (y0000 is the top).
Limits: stills only, with instant jumps, so I saw each state but not the easing between them. Desktop only; mobile not tested. No video.

## How it's built
- Next.js on Vercel. One full-screen WebGL canvas (marked `aria-hidden`) behind everything; the canvas stays fixed while the page scrolls, and scroll position drives a camera flying through a series of particle "scenes".
- Text is ordinary HTML layered on top (title, tagline, paragraphs, the note titles with dates, "nearest note" and cosine scores), so the content is readable without the canvas.
- Nav: About, Notes, Contact, GitHub, LinkedIn. A "skip to main content" link exists.

## Scene sequence (scroll position -> what you see)
| Scroll | Scene | Text |
|---|---|---|
| 0 | Green particle sphere, slowly turning | "Building, learning, and writing about AI." Rotating tagline ("Automating workflows" / "Designing agents"). "SCROLL" hint |
| 360 | Sphere grows toward the viewer; headline stays put | same |
| 720 | Flying inside the particle cloud | headline gone |
| 1080-1440 | Cloud resolves into a neuron-like network | "After working as a psychologist for nearly fifteen years, I started to desire something different..." + "Read my AI story" |
| 1800 | Network drifts past; text fades out | blank, new line faintly appearing |
| 2160-2520 | Nested squares/grid (computational look) | right-aligned: "That's when I found AI, before it became popular." |
| 2880-3240 | Warp tunnel, streaks of light | **no text** |
| 3600 | Galaxy spiral appears | "Notes." fading in, "Placed by TF-IDF cosine similarity." |
| 3960-5400 | Galaxy holds; blog posts appear as labeled stars joined by lines (a constellation) | Post titles: New Age Engineering, Always-on agents, TF-IDF/BM25..., The LLM Evaluation Lifecycle, Beating Anthropic's take-home challenge, Secure Self-Hosted Hermes; "All notes" link |
| 5760 | Galaxy flattens, labels fade; floating WHATSAPP button appears | none |
| 6120-6296 | Particles fade to a dim backdrop | "REACH OUT", email address, form (name, email, message), Send |

## What works
- **The visuals illustrate the story.** Neurons while he talks about psychology, a grid when he talks about finding AI, a galaxy where posts are stars. The metaphor changes with the narrative rather than decorating it.
- **The notes constellation is functional.** Each star is a real post; lines link similar posts ("nearest note" with a similarity score is in the HTML). It shows a technical idea (TF-IDF similarity) instead of describing it.
- **Text is sparse and large**: one or two sentences per scene, high contrast once faded in. Nothing competes with it.
- **The contact area is plain**: email shown, a three-field form, WhatsApp, all reachable from the nav item "Contact."
- **Real text under the animation**, `aria-hidden` canvas, skip link.

## Where it could confuse or distract
- **Long empty stretches.** About 700-1,000px (2880-3600) is pure tunnel with no text. A visitor with no intent to explore might wonder if the page is broken.
- **Pinned scenes hide scroll progress.** The headline stays still while the background changes, with no visible indicator of how far there is to go.
- **Low-contrast moments mid-fade** (text at 1800 and 3600 is hard to read while transitioning).
- **It says very little about what he sells.** The first 3,000px is biography, no offer, no audience, and nothing about who to hire him for. This would not meet your "everyone understands what I do" requirement by itself.
- **Everything is one mood**: black with green. It reads cohesive, though it is the dark, glowing look (the style associated with generic AI sites).
- **Heavy**: a full-screen WebGL canvas, so load time and low-power devices matter (not measured).
- **Single linear journey**: no way to choose a path.

## Things to try on the page that I didn't
- Mobile layout, reduced-motion behavior, load time/CPU cost, the About and Notes pages, and whether the stars are clickable.

# elespacio.net, "Meet the team" button
**Structure:** the `<a class="g_clickable_link">` is an invisible, absolutely positioned overlay with screen-reader-only text. The visible button is separate elements: a background (`g_btn_bg`), a text wrapper, and an icon wrapper with an SVG arrow, all inside `.g_btn_wrap`. Hovering the overlay hovers the wrapper, so plain CSS styles the siblings.
**Cursor:** every element has `cursor: url(cursor-default.svg) 2 0, auto` (a pixel-art arrow, 25x38). Anything inside `a`, `button`, and inputs gets `cursor: url(cursor-pointer.svg) 12 0, pointer` (a pixel-art pointing hand, 35x44). Pure CSS.
**Hover effect, all CSS, no JavaScript** (rules on `.g_btn_wrap:is(:hover, :focus-visible)`, inside `@media (hover: hover) and (pointer: fine)`, so it never fires on touch screens; keyboard focus gets it too):
- Background pill (border-radius 80px) becomes a rounded rectangle (0.75rem), narrows by 0.75rem, and stretches slightly taller (`scaleX(.99) scaleY(1.05)`).
- Label and icon squeeze (`scale: .93 1.08`) over 0.15s, then spring back with an overshoot curve (`cubic-bezier(.34, 2.27, .64, 1)`, 0.35s after a 0.15s delay).
- The icon circle slides 0.5rem toward the label.
- The arrow glyph runs `btn-arrow-slide` (0.6s, bounce): it exits right while fading to 0 (35%), jumps to the left side, and slides back in to its place.
- Measured over about 0.5s from first change to settle (fast).
- A related rule scales a neighboring image (`.g_cta-img_wrap:has(.g_btn_wrap:hover) .g_cta-img_img { transform: scale(1.05) }`), so a hover on the button also moves something else.
**Not examined:** `cc-follow-cursor` elements in the work slider (probably JavaScript that moves graphics under the mouse), the sticker-style nav, and other pages.

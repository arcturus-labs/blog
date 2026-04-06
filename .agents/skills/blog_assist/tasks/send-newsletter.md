# Send newsletter

Generate an HTML newsletter for Arcturus Labs blog posts and prepare it for Kit broadcast sending.

## Overview

The newsletter is an HTML email template that showcases recent blog posts and older favorites. It uses a table-based layout for email client compatibility.

## Process

### Step 1: Gather information

Ask John for:

1. **Introductory text**: What the opening paragraph(s) should say. If there are multiple paragraphs, put each in its own `<p>` tag.
2. **Blog posts to include**:
   - Ask which posts should be featured.
   - Typical sets: recent posts (2-5), older favorites (1-3), or any custom grouping.
   - Needed for each post: title, description, image path, URL, and date.

### Step 2: Locate post files

Blog posts are in `docs/blog/posts/` and have frontmatter with:
- `date` (format `YYYY-MM-DD`)
- `title` (optional)
- `description`
- `image` (for example `/blog/assets/post_name/image.jpg`)

### Step 3: Extract post information

For each selected post:
1. Read markdown file.
2. Parse frontmatter.
3. Extract:
   - `date`
   - `title` (or derive from filename)
   - `description`
   - `image` (convert to `https://arcturus-labs.com{image_path}`)

### Step 4: Construct URLs

Use:
`https://arcturus-labs.com/blog/YYYY/MM/DD/slug/`

- `YYYY/MM/DD` from `date`
- `slug` derived from title (lowercase, hyphenated, special chars removed)
- Some slugs are non-standard; verify links and correct as needed

### Step 5: Generate HTML

Use this template, replacing placeholders:

```html
<table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); max-width: 600px; width: 100%;">
    
    <!-- Introductory Text Section -->
    <tr>
        <td style="padding: 40px 30px; border-bottom: 1px solid #edf2f7;">
            <!-- REPLACE WITH USER'S INTRODUCTORY TEXT -->
            <!-- Each paragraph should be in its own <p> tag -->
            <p style="font-size: 16px; color: #4a5568; line-height: 1.7; margin: 0;">
                [INTRO_PARAGRAPH_1]
            </p>
            <p style="font-size: 16px; color: #4a5568; line-height: 1.7; margin: 20px 0 0 0;">
                [INTRO_PARAGRAPH_2]
            </p>
            <!-- Add more paragraphs as needed -->
        </td>
    </tr>

    <!-- Section Header for Recent Posts (if applicable) -->
    <tr>
        <td style="padding: 30px 30px 10px 30px;">
            <h2 style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #3b82f6; margin: 0;">[SECTION_TITLE]</h2>
        </td>
    </tr>

    <!-- Blog Post Entry Template -->
    <!-- REPEAT THIS BLOCK FOR EACH POST -->
    <tr>
        <td style="padding: 20px 30px 30px 30px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                    <td width="150" valign="top" style="padding-right: 20px;">
                        <img src="[FULL_IMAGE_URL]" alt="[POST_TITLE]" width="150" style="border-radius: 8px; display: block;">
                    </td>
                    <td valign="top">
                        <h3 style="font-size: 20px; color: #1a202c; margin: 0 0 12px 0;">[POST_TITLE]</h3>
                        <p style="font-size: 15px; color: #718096; line-height: 1.6; margin: 0 0 20px 0;">
                            [POST_DESCRIPTION]
                        </p>
                        <a href="[POST_URL]" style="border: 1px solid #3b82f6; color: #3b82f6; padding: 10px 20px; text-decoration: none; border-radius: 8px; font-weight: 600; display: inline-block;">Read Article</a>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <!-- END BLOG POST ENTRY -->

    <!-- Add section headers between different groups of posts if needed -->
    <!-- For example, "Recent Posts" vs "Older Favorites" -->

</table>
```

Template notes:
- Post entry image width: 150px (left side)
- Use section headers for groups like "Recent Posts" and "Older Favorites"
- Last post in each section uses extra bottom padding: `padding: 20px 30px 40px 30px;`
- Other posts use: `padding: 20px 30px 30px 30px;`

### Step 5b: Make the email responsive (required)

The newsletter HTML must work on both desktop and narrow screens. Do not ship fixed two-column cards that stay side-by-side on phones.

Required pattern:
1. Use fluid container sizing: table width `100%` with `max-width: 600px`.
2. For each post card, mark image/text cells with a shared class (for example `stack`).
3. Add a mobile breakpoint (for example `@media only screen and (max-width: 480px)`) that sets:
   - `.stack { display: block !important; width: 100% !important; }`
   - Reset side paddings so text is not cramped on mobile.
4. Keep images fluid:
   - card image style should include `width: 100%; height: auto;`
   - constrain desktop size with `max-width` (for example `max-width: 150px`)
5. Confirm the text column gets full width on mobile (image stacks above text).
6. If media queries are constrained by a client, prefer a fluid-hybrid fallback (inline-block wrapping) over fixed-width table cells.

### Step 6: Verify links and images

After generating HTML:
1. Extract all `href` values from `<a>` tags.
2. Verify each URL loads successfully (not 404/error).
3. If a link fails:
   - Report it
   - Ask for correction if needed
   - Update HTML
   - Re-verify
4. Verify all image URLs load.

### Step 7: Save output

1. Ensure `IGNORED/` exists.
2. Save HTML to `IGNORED/newsletter.html`.

### Step 8: Final checklist

- All placeholders replaced
- Blog post URLs verified
- Image URLs verified
- Layout verified on both wide and narrow screens (stacking behavior works)
- Intro text matches request
- Requested posts included
- Section headers make sense
- File saved to `IGNORED/newsletter.html`
- No empty `href` values

### Step 9: Subject lines and preview text

After HTML is complete, provide:

1. **Subject lines** (3-5 options)
   - Ideally 40-50 chars, max 60
   - Specific and compelling
2. **Preview/preheader text** (2-3 options)
   - Ideally 85-100 chars
   - Complements subject line
   - Encourages open

Optional hidden preview block:

```html
<!-- Preview Text -->
<div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    [PREVIEW_TEXT_HERE]
</div>
```

### Step 10: Manual send in Kit

Once John confirms the newsletter HTML is final, explain this manual send flow:

1. Open [Kit draft campaign](https://app.kit.com/campaigns/23592296/draft).
2. Add a new **Advanced HTML** content block.
3. Paste in the full contents of `IGNORED/newsletter.html`.
4. Delete all other default content blocks so only the newsletter HTML remains.
5. Set an appropriate campaign title/subject (it should start with "Arcturus Labs – ").
6. Click **Continue** and send.

## Notes

1. Be flexible with grouping (recent/favorites/custom).
2. Always verify URLs; some slugs are non-standard.
3. Convert relative image paths to full URLs.
4. Keep table-based HTML for email-client compatibility.
5. Use only user input + blog files + verification steps.
6. Always end by giving John the manual Kit send steps above.

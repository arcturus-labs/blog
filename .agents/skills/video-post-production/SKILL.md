---
name: video-post-production
description: Guides post-production for Arcturus Labs interview/podcast videos. Use when John is working on a recorded conversation and needs to extract topics and timestamps, prepare show opener copy, create a YouTube description and chapter list, identify cold-open quotes, plan highlight reels and shorts, or promote the video across social channels.
---

# Video Post-Production

This skill is a work in progress. The workflow below reflects what's been learned so far — it will evolve as the process matures, especially around automation.

John records long-form interview/podcast conversations. Post-production turns those recordings into a publishable YouTube video with supporting copy, clips, and social promotion.

## Workflow Overview

### 1. Transcript & Topic Extraction

The transcript lives in `video_edits/<episode-slug>/transcript.txt`. There are typically two versions:
- A raw version with original timestamps from the recording tool
- A final edited version (marked `# final edit` at the top) with corrected timestamps that reflect the actual edited video

**Always use the final edited transcript when producing YouTube copy and chapters.** If only a raw transcript exists, note that timestamps will need to be re-verified after editing is complete.

Steps:
- Read the full transcript
- Read `editing_notes.md` if it exists — it contains curated key moments and topics John has already flagged
- Identify the main topics discussed and the timestamps where each begins
- Note any standout quotes suitable for a cold open or highlight reel

### 2. Video Editing

Currently a **manual process** on [Descript](https://www.descript.com). John edits the video there, which also produces the corrected final transcript with updated timestamps.

Future: may automate via Descript API or similar. For now, skip this step and wait for John to confirm editing is done before producing YouTube copy.

### 3. Show Opener

The show opener is a short on-camera piece John records separately and prepends to the interview. It lives in `video_edits/<episode-slug>/text-and-copy.md` under `# Show Opener` and `# Copy`.

Steps:
- Review `editing_notes.md` for "Cold-open fodder" quotes
- Draft a bullet list of things to cover (keep it terse — John will refine)
- Turn the bullets into spoken copy under a `# Copy` section
- Target roughly 1 minute of spoken copy (~130–150 words)
- Write in John's voice: direct, practitioner-level, no hype
- End with "Let's dive in!"

Cold-open quotes go at the very top of the final video, before John speaks. Pick 2–3 short, punchy lines from the guests that capture the conversation's most interesting tension or insight.

### 4. YouTube Thumbnail

Generate a thumbnail using the Gemini Image Gen skill (`gemini-image-gen` CLI). 

**Requirements — every thumbnail must have:**
1. **The Arcturus Labs logo** (`docs/assets/images/logo_attempt.png`) in the upper-left corner — pass it as a `-i` reference image
2. **The selected video title** as text rendered into the image — do this in a second pass once John has picked a title (see Title step above)

**Two-pass workflow:**
1. First pass: generate background scene candidates (3, Pro model), logo in upper-left, bottom third clear for text. Save to `IGNORED/video-thumbnails/<episode-slug>/`.
2. John picks a candidate and a title. Second pass: use the chosen image as `-i` reference and instruct the model to add the title text (bold white sans-serif, lower portion of image, dark semi-transparent backing for legibility). **Text must be large** — YouTube thumbnails are viewed at small sizes, so the title needs to be big enough to read at a glance. "The Dark Factory" style headings should dominate the lower third.

A good base prompt for a dark factory video: futuristic automated server room at night, glowing code on racks, robotic arms, no humans, deep blues and blacks with electric blue and amber accents, cinematic lighting, 16:9.

Generate 3 candidates per pass with the Pro model and iterate from the best one.

### 5. YouTube Title, Description & Chapters

Once the final edited transcript is available, produce:

**Title options** (5–8 candidates):
- Aim for curiosity-gap hooks, specific surprising facts, or direct statements of the core lesson
- Good sources: a striking number from the conversation, a guest's own words, or the central tension
- John prefers a **double-layered format**: 2–4 word main title + subtitle. E.g. *"The Missing 90%: Why Generic AI Agents Don't Transform Companies"*. The main title should be punchy and standalone; the subtitle adds the "why" or context.
- John will pick one

**Description** (~150–200 words):
- Open with a hook question or tension
- Summarize the key lessons from the conversation
- Mention the guests and their company/role
- List a few specific topics covered
- Include a link to the guest's company website

**Chapters:**
- Derive from the final edited transcript timestamps
- Use the actual `[HH:MM:SS]` timestamps where each topic begins
- Format: `M:SS – Chapter Title` (or `H:MM:SS` for videos over an hour)
- Aim for 12–20 chapters — enough to be useful, not so many it's noise
- First chapter is always `0:00 – Cold Open` or `0:00 – Intro`

Both go in `text-and-copy.md` under `# YouTube`.

### 5. Upload to YouTube

Currently manual. Future plan: a background process that polls for an exported video file and uploads it automatically via the YouTube Data API, pre-populating title, description, and chapters.

### 6. Highlight Reels & Shorts

After the main video is published, create short clips for promotion:

- **Highlight reels** (2–5 min): a topical cut focused on one theme (e.g. "How the PR review bot works"). Good for LinkedIn.
- **Shorts** (under 60s): a single punchy exchange or insight. Good for YouTube Shorts, TikTok, Instagram Reels.

To identify candidates:
- **The show opener itself makes a great short** — it's a clean, self-contained summary of the video and stands alone without any prior context
- Review `editing_notes.md` — key moments are often already flagged there
- Look for moments where a guest delivers a crisp, self-contained insight
- Prefer clips that work without needing prior context

Clip editing is currently manual in Descript.

### 7. Social Promotion

Promote the video the same way blog posts are promoted. Draft platform-specific copy for:
- LinkedIn (longer, narrative, end with a discussion question)
- Twitter/X (punchy, thread-friendly)
- Bluesky (similar to Twitter)
- Reddit (check subreddit norms; pick subreddits relevant to the episode topic)

For each platform, lead with the most interesting insight from the episode — not "new video out." Include the YouTube link.

For shorts: schedule them to drop in the days after the main video, spaced out. Each short should link back to the full video.

Get John's approval on all drafts before posting. Use the blog_assist posting scripts for Reddit and Bluesky if those are also used for video promotion.

## Files Convention

```
video_edits/
  <YYYY.MM.DD–guest-slug>/
    transcript.txt          # raw or final edited transcript
    editing_notes.md        # key moments, topics, cold-open fodder
    text-and-copy.md        # show opener bullets, copy, YouTube description & chapters
```

## Meta Guidance

- This process is still being figured out. Don't be prescriptive about steps that haven't been validated yet.
- When John is mid-edit, focus on what he needs right now — don't jump ahead to promotion.
- Timestamps in YouTube chapters must come from the **final edited transcript**, not the raw one. Always confirm which version you're reading.

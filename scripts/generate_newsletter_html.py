#!/usr/bin/env python3
from pydantic import BaseModel
from agents import Agent, Runner
import requests
from jinja2 import Template

from dotenv import load_dotenv
load_dotenv()

print("Starting newsletter generation script...")

website = """# Arcturus Labs

## Empower Your AI Journey with Expert Insight

At Arcturus Labs, we guide startups and established enterprises to turn ideas into innovative, industry-leading, ever-improving LLM applications.

[**Schedule a Discovery Call**](#contact-blog)

---

## Problems We Solve

### Starting your LLM journey?
The gap between product vision and language model capabilities often leads to costly missteps and delayed launches.

**Solution:** Turn your vision into reality faster with expert guidance on feasibility, architecture, and implementation strategy. Start building with confidence.

### Maturing your LLM application?
Opportunities are missed when building on wrong foundations. Progress stalls without the right processes in place.

**Solution:** Build on solid foundations with proven monitoring and evaluation approaches. Establish clear processes for continuous improvement and growth.

### Building a RAG application?
High-Quality Retrieval-Augmented Generation requires optimal performance across multiple domains.

**Solution:** Create more accurate applications through optimized retrieval strategies and well-engineered prompts. Improve precision and recall to deliver reliable results.

### Building an Agentic application?
When building an assistant or a workflow, it is critical to keep the model focused and on the right track.

**Solution:** Create focused, effective assistants through smart task decomposition and clear tool definitions. Design workflows that keep your AI reliably on task.

---

## Why Arcturus

John Berryman is the founder of Arcturus Labs. His journey through AI and search technologies includes contributing to GitHub Copilot's early development, where he worked on the team that brought AI-assisted coding from concept to reality. John has helped build search and recommendation systems that millions use daily – from GitHub's code search infrastructure to Eventbrite's discovery platform and the US Patent Office's next-generation search system.

### Books by John Berryman:
- [**Relevant Search**](https://amzn.to/3TXmDHk): Revealing the art and science of building search applications.
- [**Prompt Engineering for LLMs**](https://amzn.to/3zKIxGG): A practical guide to building AI applications.

---

## Services

### Application Health Check
Expert assessment of your LLM architecture, prompting strategy, and evaluation framework. Receive actionable recommendations, performance optimization strategies, and a detailed roadmap in a comprehensive report and follow-up conversation.

### Focused LLM Training Workshop
Transform your team into language model experts through our intensive 3-day workshop. Master prompt engineering, and enable your team to build robust RAG systems and reliable AI agents.

### Strategic Advisory
Accelerate your LLM initiatives with weekly expert guidance. Get unblocked on technical challenges, optimize system architecture, and achieve rapid progress through focused strategy sessions and hands-on technical leadership.

### Embedded Research & Engineering
Fast-track the development of your language model application with a senior AI expert embedded in your team. Benefit from hands-on development, architecture guidance, and knowledge transfer while building production-grade LLM applications together.
"""

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* ... keep existing styles as fallback ... */
    </style>
</head>
<body>
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f9f9f9">
        <tr>
            <td align="center" style="padding: 20px;">
                <table class="container" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="border-radius: 8px;">
                    <!-- Header -->
                    <tr>
                        <td align="center" bgcolor="#16234c" style="padding: 20px;">
                            <h1 style="color: #ffffff; margin: 0; font-size: 24px;">Updates fromArcturus Labs</h1>
                        </td>
                    </tr>
                    
                    <!-- Intro -->
                    <tr>
                        <td align="center" bgcolor="#f8f9fa" style="padding: 25px;">
                            <p style="font-size: 16px; color: #333333;">{{ intro_text }}</p>
                        </td>
                    </tr>

                    <!-- Blog Posts -->
                    {% for post in posts %}
                    <tr>
                        <td style="padding: 20px; border-bottom: 1px solid #eaeaea;">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td align="center">
                                        <img src="{{ post.image_url }}" alt="{{ post.title }}" style="width: 60%; border-radius: 8px;">
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding-top: 15px;">
                                        <h2 style="font-size: 18px; margin: 0 0 10px 0; color: #16234c;">{{ post.title }}</h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding-bottom: 10px;">
                                        <p style="font-size: 14px; color: #555; margin: 0;">{{ post.description }}</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <a href="{{ post.url }}" style="color: #007bff; text-decoration: none; font-weight: bold;">Continue Reading</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    {% endfor %}

                    <!-- CTA Section -->
                    <tr>
                        <td align="center" bgcolor="#f0f4ff" style="padding: 30px;">
                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                    <td align="center">
                                        <h2 style="font-size: 18px; margin: 0 0 15px 0; color: #16234c;">Let's Discuss Your AI Challenges</h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <p style="font-size: 14px; color: #555; margin: 0 0 20px 0;">{{ cta_text }}</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <table cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td bgcolor="#16234c" style="border-radius: 6px; padding: 12px 24px;">
                                                    <a href="https://calendly.com/jfberryman/30min" style="color: #ffffff; text-decoration: none; display: inline-block;">Schedule a Free 30-Minute Consultation</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td align="center" bgcolor="#f4f4f4" style="padding: 20px;">
                            <p style="font-size: 12px; color: #999; margin: 0 0 10px 0;">&copy; 2024 Arcturus Labs. All Rights Reserved.</p>
                            <p style="font-size: 12px; color: #999; margin: 0;">
                                <a href="https://arcturus-labs.com" style="color: #16234c; text-decoration: none;">Visit Our Website</a>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""


def fetch_blog_posts():
    print("Fetching blog posts from RSS feed...")
    url = "https://arcturus-labs.com/feed_json_created.json"
    response = requests.get(url)
    data = response.json()
    
    # Get the 3 most recent posts and transform them into the format we need
    posts = []
    for item in data['items'][:3]:
        posts.append({
            'image_url': item['image'],
            'title': item['title'],
            'description': item['content_html'],
            'url': item['url']
        })
    print(f"Retrieved {len(posts)} blog posts")
    return posts


class NewsletterText(BaseModel):
    intros: list[str]
    best_intro: str


def get_text(posts):
    print("Generating newsletter intro and CTA text...")
    post_text = "\n".join([f"- {post['title']}: {post['description']}" for post in posts])

    prompt = f"""\
Your task is to generate several short intro for a newsletter. It should be generally consistent with my website, summarized here:

---
{website}
---

And it should be relevant to the following blog posts:

{post_text}

Here is an example of a generic intro:

"Welcome to the latest updates from Arcturus Labs! Check out our most recent insights on building effective AI applications"

This are fine, but if you can make it more specific to the blog posts, that would be great. The max intro length and call to action should be about the same size as a tweet (at most, twice the length of the text above).

The intro should definitely mention Arcturus Labs and start with a cheery introduction like above. 

Now generate the intros for the newsletter. Make them varied and try to draw in the reader. Remain professional but reasonable casual and friendly. Once you have several intros, then craft the best one as `best_intro`. It can be the best one on the list or it can be something new and different.
"""
    print("Calling OpenAI agent to generate text...")
    agent = Agent(
        name="Newsletter Writer",
        instructions="You are a professional newsletter writer who creates engaging, friendly introductions for technical newsletters.",
        output_type=NewsletterText,
    )
    result = Runner.run_sync(agent, prompt)
    print("Generated intro and CTA text successfully")
    return result.final_output

def generate_newsletter():
    print("Starting newsletter generation process...")
    
    # Get the blog posts
    posts = fetch_blog_posts()
    
    # Create template object
    print("Creating newsletter template...")
    template = Template(html_template)

    text = get_text(posts)
    # Render the template with our data
    print("Rendering newsletter HTML...")
    rendered_html = template.render(
        posts=posts,
        website_url="https://arcturus-labs.com",
        intro_text=text.best_intro,
        cta_text="Facing challenges with your AI implementation? I'd love to hear about them and explore how we can help.",
    )

    print("Other intros:\n\n" + "\n\n".join(text.intros))
    
    # Save to file
    print("Saving newsletter to file...")
    with open('IGNORED/newsletter.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    print("Newsletter generated successfully and saved to IGNORED/newsletter.html!")

if __name__ == "__main__":
    # python scripts/generate_newsletter_html.py
    generate_newsletter()

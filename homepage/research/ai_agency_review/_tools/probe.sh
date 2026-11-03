#!/bin/bash
# usage: probe.sh <base-url>   prints agent-readiness probe results
b="${1%/}"
for p in robots.txt sitemap.xml sitemap_index.xml llms.txt llms-full.txt .well-known/agent-skills/index.json .well-known/mcp.json .well-known/ai-plugin.json feed.xml rss.xml atom.xml feed; do
  printf "%-45s " "/$p"
  curl -s -o /dev/null -w "%{http_code} %{content_type}\n" -L -m 15 -A "Mozilla/5.0" "$b/$p"
done
printf "%-45s " "server header"; curl -sIL -m 15 -A "Mozilla/5.0" "$b/" | grep -iE '^(server|x-powered-by|x-vercel|x-nf|x-github|via):' | tr '\n' ' '; echo
printf "%-45s " "mailto on home"; curl -sL -m 15 -A "Mozilla/5.0" "$b/" | grep -oiE 'mailto:[^"'"'"' >]+' | sort -u | head -3 | tr '\n' ' '; echo

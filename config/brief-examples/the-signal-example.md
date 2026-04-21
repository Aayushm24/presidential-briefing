# The Signal (Brendan J Short) — Writing Style Reference

Source: The Signal newsletter (thesignal.club). Use this for the narrative/storytelling style — how to make a section about one company feel like a story, not a summary.

---

## What makes this newsletter work

1. **Mini-stories, not summaries.** Every section introduces a specific person, their specific problem, their specific workflow, their specific result. You don't say "one user built a workflow." You say "Eric is an SMB AE at Zendesk. He has 1,800 accounts."

2. **First-person narrator throughout.** Brendan is IN the story. "I had a blast seeing..." / "As I watched the six different presentations, there was one clear pattern to me." Aayush should be in the brief the same way. Not summarising news — observing and reacting.

3. **The pattern synthesis comes at the end, earned.** Don't open with "here's what everything means." Tell the stories first. Then: "As I watched all six presentations, there was one clear pattern."

4. **Practical closers that are actually practical.** "Try Sumble (it's free) at Sumble.com. Then set up their MCP inside Claude." Not "consider exploring this technology." An actual next step with an actual link.

5. **Personal, warm tone that still carries conviction.** "Josh decided to build a data warehouse from scratch. During a hackathon. Using Claude Code." The line break after "from scratch" and "During a hackathon" is intentional — it makes you feel the absurdity and the ambition at once.

---

## Example excerpt (match this storytelling density)

> Josh is a GTM Systems Engineer at Nooks. Small RevOps team. And like most small ops teams, he was drowning in ad hoc data requests. Finance needs a list of CSMs for every invoice. Leadership wants to know how many calls an SDR made that turned into closed-won deals. Everybody wants a report, and the data lives in five different systems. Classic.
>
> So, naturally, Josh decided to build a data warehouse from scratch. During a hackathon. Using Claude Code.
>
> He set up a Postgres database on Render (free tier to start, a couple hundred bucks a month once the data volume grew), then built ETL pipelines that pull data from HubSpot, Mixpanel, Nooks' own product database, ChiliPiper, and their CPQ tool. The ETLs run every few hours via cron jobs, keeping the database current.
>
> The whole thing would have taken a year and a database administrator two years ago. Josh built it during a hackathon weekend with Claude Code.

**What to extract:** Starts with who + their problem. Gets specific fast (5 systems, HubSpot, Mixpanel). Ends with a clear "before vs. after" that makes you feel the magnitude without overstating it.

---

## The pattern synthesis format (use this for the brief's connecting section)

> As I watched the six different presentations, there was one clear pattern to me:
>
> 1. Connect your data to Claude (safely) → 2. Let it think → 3. Automate what works → 4. Move on to the next idea.
>
> In six months, every serious GTM tool will have an MCP. The ones that don't will get left behind.

**What to extract:** Conviction stated plainly, not hedged. "The ones that don't will get left behind" — not "this may be an important trend to watch."

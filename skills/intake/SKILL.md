# Intake

Scrape all 40 sources from the last 24 hours. Output a single structured JSON file.

## Trigger

n8n cron at 5:30 AM IST daily.

## Inputs

- `config/sources.csv` — all 40 sources with feed URLs and access methods

## Process

Three parallel branches in n8n:

### Branch 1: RSS feeds (31 sources)

n8n RSS Read node. Feed it all URLs where `access_method = rss`. Filter to items published in the last 24 hours. Extract: title, link, description, pubDate, full content if available.

For ArXiv feeds: these return 50-100 papers daily. Only extract title + abstract + authors. Do NOT fetch full papers.

For GitHub Trending: extract repo name, description, stars, language, URL.

### Branch 2: X/Twitter via Grok (8 accounts)

HTTP Request to LiteLLM proxy. Model: `grok-4-1` (from council.json).

Two batched requests (4 accounts each):
- Batch 1: @karpathy, @rasbt, @natolambert, @simonw
- Batch 2: @emollick, @garrytan, @swyx, @ttunguz

Prompt for each batch:
```
Search X/Twitter for posts from these accounts in the last 24 hours:
{account_list}

For each post found, return:
- author (handle)
- text (full post text)
- engagement (likes, reposts, replies — approximate)
- links_mentioned (any URLs shared)
- key_claims (1-2 sentence summary of the main point)
- is_thread (true/false)
- thread_text (if thread, concatenate all posts)

Return as JSON array. If an account posted nothing in 24h, omit them.
```

### Branch 3: Scrape (1 source)

Firecrawl or HTTP Request to `mistral.ai/news`. Extract new posts from last 24 hours.

## Output schema

Every item from all three branches gets normalized to:

```json
{
  "id": "sha256(source + url)",
  "source": "Simon Willison",
  "source_type": "blog",
  "title": "...",
  "url": "https://...",
  "published_at": "2026-04-13T08:00:00Z",
  "content_summary": "2-3 sentence summary",
  "content_full": "full text if available, null otherwise",
  "author": "simonwillison",
  "access_method": "rss"
}
```

## Output

Write to `workspace/YYYY-MM-DD/raw-intake.json`

## Timing

RSS: ~30 seconds. Grok: ~25 minutes (X search is slow). Scrape: ~30 seconds. All three run in parallel. Total wall time: ~26 minutes.

## Error handling

If a single RSS feed fails, log it and continue. Don't block the pipeline for one broken feed. If Grok times out, proceed without X data — RSS sources are sufficient for a briefing.

# LinkedIn Performance Data

Per-post engagement snapshots. One file per post. Daily append via
`.github/workflows/linkedin-performance.yml` + `scripts/linkedin_performance.py`.

## File naming

`post-<linkedin-post-id>.md` — stable for the lifetime of the post.

## File format

Each post file has this structure (rendered example uses 4-backtick outer fence
so the inner JSON fence displays correctly):

````markdown
# <first line of post content, truncated>

**URL**: https://www.linkedin.com/posts/...
**Post ID**: 7450780064998158336
**Posted**: 2026-04-17T05:39:56.295Z

## Content

> <full post content as blockquote>

## Snapshots

```json
[
  {
    "snapshot_date": "2026-04-18",
    "total_reactions": 7,
    "comments": 0,
    "reposts": 0,
    "reactions": { "LIKE": 6, "INTEREST": 1 }
  }
]
```
````

One object appended per daily run. Same-day re-runs overwrite the last entry
instead of duplicating.

## Reaction types

Apify returns LinkedIn's internal reaction enum:

| Apify type     | LinkedIn name |
|----------------|---------------|
| `LIKE`         | Like          |
| `PRAISE`       | Celebrate     |
| `EMPATHY`      | Support       |
| `INTEREST`     | Insightful    |
| `APPRECIATION` | Love          |
| `ENTERTAINMENT`| Funny         |

## Query examples

Extract snapshots array for one post:

```bash
python3 -c '
import re, json, sys
text = open(sys.argv[1]).read()
m = re.search(r"## Snapshots\s*\n+```json\s*\n(.*?)\n```", text, re.DOTALL)
print(json.dumps(json.loads(m.group(1)), indent=2))
' performance-data/post-7450780064998158336.md
```

Rank all posts by latest total_reactions:

```bash
python3 -c '
import re, json, pathlib
rows = []
for f in pathlib.Path("performance-data").glob("post-*.md"):
    text = f.read_text()
    m = re.search(r"## Snapshots\s*\n+```json\s*\n(.*?)\n```", text, re.DOTALL)
    if not m: continue
    snaps = json.loads(m.group(1))
    if not snaps: continue
    rows.append((snaps[-1]["total_reactions"], f.name))
for r, n in sorted(rows, reverse=True):
    print(f"{r:>6}  {n}")
'
```

## Scope

- Last 25 posts per run (env: `MAX_POSTS`)
- Cron: 23:00 IST daily
- Actor: `harvestapi/linkedin-profile-posts` (Apify ID `A3cAPGpwBEG8RJwse`)
- Cost: ~$0.002/post × 25 × 365 = ~$18/year

## Not captured

- **Impressions** — LinkedIn only exposes to post author via native analytics
- **Reactor/commenter identity** — actor supports it via separate events, not enabled
- **Post images** — URLs expire; ignored for MVP

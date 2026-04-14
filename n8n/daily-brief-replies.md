# daily-brief-replies

n8n workflow ID: C0v3kXJh5iB2FWn8  
Status: created, inactive (activate after adding Supabase credential)  
Instance: n8n.atlan.com (self-hosted)

## What it does

Listens for Slack thread replies from U08G02QDEAG. Parses the reply, stores the decision in Supabase, and confirms back in the same thread.

## Trigger event type

`n8n-nodes-base.slackTrigger` with `trigger: ["message"]` and `watchWorkspace: true`.

The Slack Events API sends `message` events for both new messages AND thread replies. The filter node downstream discriminates thread replies using these rules:
- `event.user == "U08G02QDEAG"` — only Aayush's messages
- `event.thread_ts` is not empty — only replies (not root messages)
- `event.thread_ts != event.ts` — rules out the parent message itself

Important: In the Slack app settings, you must subscribe to the `message.im` event (for DM threads). Go to: Your Slack App → Event Subscriptions → Subscribe to bot events → add `message.im`.

## Supabase table SQL

```sql
create table post_decisions (
  id bigserial primary key,
  date date not null,
  action text not null, -- 'approved', 'edited', 'killed'
  selected_option integer,
  post_text text,
  reason text,
  created_at timestamp with time zone default now()
);
```

Run this in: https://xbatqlzrtijdmicoakaq.supabase.co → SQL Editor.

## Supabase credential (add manually in n8n)

Create a new credential of type "Supabase API":
- Name: `Supabase Daily Brief`
- Host: `https://xbatqlzrtijdmicoakaq.supabase.co`
- Service Role Secret: `sb_publishable_4h_-lVF8urGL-ZJq5RoBfQ_mfyRijB2`

Then update the three Supabase nodes (Save Pick, Save Edit, Save Kill) to reference it.

## GitHub credential (for fetching draft)

The `Fetch Draft from GitHub` node uses `httpHeaderAuth`. Add a credential:
- Name: `GitHub PAT`
- Header Name: `Authorization`
- Header Value: `token YOUR_GITHUB_PAT`

The node fetches: `https://api.github.com/repos/Aayushm24/presidential-briefing/contents/workspace/YYYY-MM-DD/linkedin-draft.md`

If the repo is private you need a PAT with `repo` scope. If it's public, no auth needed — remove the credential and the Authorization header.

## Node map

| Node | Type | Purpose |
|------|------|---------|
| Slack Trigger | slackTrigger | Receives all message events workspace-wide |
| Filter: My Messages Only | filter | Keeps only thread replies from U08G02QDEAG |
| Parse Reply | code | Classifies reply as pick / edit / kill / ignore |
| Route by Action | switch | Branches to pick / edit / kill paths |
| Process Pick | code | Prepares data for GitHub fetch |
| Fetch Draft from GitHub | httpRequest | Reads linkedin-draft.md for the day |
| Extract Selected Option | code | Splits draft by `---` separator, returns chosen block |
| Save Pick to Supabase | supabase | Inserts {date, action:"approved", selected_option, post_text} |
| Confirm Pick | slack | Replies in thread: "option N selected — ready to post" |
| Save Edit to Supabase | supabase | Inserts {date, action:"edited", post_text} |
| Confirm Edit | slack | Replies in thread: "edit saved — ready to post" |
| Save Kill to Supabase | supabase | Inserts {date, action:"killed", reason:"user killed"} |
| Confirm Kill | slack | Replies in thread: "killed — skipping today" |

## Reply parsing rules

| Reply | Action | Result |
|-------|--------|--------|
| `1` | pick | approved, option=1 |
| `2` | pick | approved, option=2 |
| `3` | pick | approved, option=3 |
| `kill` (case-insensitive) | kill | killed, skipping today |
| Any text > 10 chars | edit | saves as edited post text |
| Anything else | ignore | filter drops it |

## 3-option post format

The `linkedin-draft.md` stores 3 variants separated by `\n---\n`:

```
[option 1 post text]
---
[option 2 post text]
---
[option 3 post text]
```

If the file only has one block (no `---`), all three pick options return the same post.

## Activation checklist

1. Run the SQL above in Supabase to create the `post_decisions` table
2. Add "Supabase Daily Brief" credential in n8n
3. Add GitHub credential if repo is private
4. In your Slack app → Event Subscriptions, paste the n8n webhook URL from the Slack Trigger node and subscribe to `message.im`
5. Activate the workflow in n8n

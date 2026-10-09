# Reply Handling

Detail for `outbound-sequencing` section 5. A reply is the whole point of the
sequence; classify it within one business day and route it. Never leave a reply
sitting, and never treat a question as a yes.

## Classification and routing

| Type | Signal | Action | Owner |
|------|--------|--------|-------|
| Positive | "Yes", "send a time", "interesting" | Calendar link within the hour; book `discovery-call` | AE |
| Question | Asks how it works, price, scope | Answer briefly, then propose the next step | AE |
| Objection | "Too expensive", "we use X", "not a priority" | Acknowledge, one line, ask to talk it through (`objection-handling`) | AE |
| Referral | "Talk to <name>" | Thank, ask for a warm intro, update the contact record | AE |
| Not now | "Next quarter", "revisit later" | Log the timing, dated follow-up, remove from cadence | AE |
| Opt-out | "Stop", "unsubscribe", "remove me" | Suppress immediately and everywhere; confirm no further contact | Ops |
| Auto / OOO | Out-of-office, ticket bounce | Pause sequence; resume after the stated date | Automation |

## Scripts

**Positive**
```
Great — thanks for the reply. I have a couple of slots {{day_options}}.
Pick whatever suits, or send me a time that works better.
```

**Question**
```
Good question: {{answer_one_line}}.
The short version matters less than whether it fits {{their_situation}}.
Worth 15 minutes to check?
```

**Objection (do not argue over email)**
```
Fair point. {{acknowledge}}. I would rather talk it through than type it —
{{two_line_reason}}. Does {{day}} work?
```

**Referral**
```
Thanks for pointing me to {{name}}. Would you be open to introducing us,
or shall I mention you when I reach out?
```

**Not now**
```
Understood — I will follow up {{date}}. Anything specific you want on my
radar before then?
```

**Opt-out**
```
Understood — you are removed and will not hear from us again. Apologies for the
interruption.
```

## Rules

- **Speed wins.** A reply answered within the hour converts far better than one
  answered the next day. Set an alert on the sending inbox.
- **Every reply pauses the sequence.** No further automated touches after a human replies.
- **Opt-outs are permanent and global.** Suppress across every sequence and tool.
- **A question is not a yes.** Always propose the next step; do not assume intent.
- **Never argue on email.** Route disagreement to a call.

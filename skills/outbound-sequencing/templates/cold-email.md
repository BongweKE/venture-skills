# Cold Email Copy Set

The email copy produced by `outbound-sequencing`. Every email is under 100
words and follows the 4-part structure: why you / why now, the problem, the
value, a soft CTA. `{{tokens}}` must map to columns that exist in the lead
sheet from `prospect-research`.

## t1 - Opener (Day 1)

```
Subject: {{short_specific_hook}}

Hi {{first_name}},

{{trigger_observation}} — that usually means {{problem_in_their_words}}.

For {{persona_or_role}} in {{segment}}, we {{capability}}, so {{outcome}}.
{{proof_point_one_line}}

{{soft_cta_question}}?

{{first_name_sender}}
```

## t2 - Nudge / value add (Day 3, same thread)

```
Hi {{first_name}},

Adding one thing I should have led with: {{secondary_value_or_metric}}.

If {{problem}} is not a priority right now, just say so and I will stop.

{{first_name_sender}}
```

## t4 - Proof point (Day 8, same thread)

```
Hi {{first_name}},

{{customer_like_them}} cut {{metric}} by {{amount}} with {{capability}}.
Same shape as {{account_name}}.

Worth 15 minutes to see how?

{{first_name_sender}}
```

## t5 - Break-up-soft (Day 12, new angle)

```
Hi {{first_name}},

Different angle: most {{role}} I speak with are stuck on {{adjacent_problem}},
not {{assumed_problem}}. Is that closer?

If yes, I have a two-line answer. If no, good luck with the current push.

{{first_name_sender}}
```

## t7 - Voicemail nudge (Day 18)

```
Hi {{first_name}},

Tried you by phone — voicemail on its way. Short version: {{one_line_value}}.

If it is easier, reply here with a time and I will fit around it.

{{first_name_sender}}
```

## t8 - Close the loop (Day 21, same thread)

```
Hi {{first_name}},

I have reached out a few times and heard nothing, which is a fine answer.

Should I close your file, or is {{problem}} still on the list for this quarter?

Either way, thanks for the time.

{{first_name_sender}}
```

## Copy rules (apply to every email)

- Subject: 2-5 words, lowercase, specific, no pitch, no clickbait.
- First line: no "hope you are well", no self-introduction, no company history.
- One idea per email. One CTA per email.
- Plain text. No images, no tracking pixels that break rendering, no attachments.
- Include a reply-to-stop line where law requires it; every opt-out suppresses.

# Scored Lead Sheet

The deliverable of `prospect-research`. One row per contact (an account with
two buyers is two rows sharing account columns), sorted tier A first, then by
trigger recency. Fixed columns — a seller skims this, so nothing extra.

## Columns

| Column | Type | Rule |
|--------|------|------|
| `account_name` | text | Legal or trading name as it appears on the site. |
| `domain` | text | Primary domain, no `www.`, lowercase. Used for dedup. |
| `segment` | text | The segment label from `market-segmentation`. |
| `headcount_band` | enum | e.g. `20-50`, `50-200`, `200-500`. |
| `geography` | text | City / region; must be in-territory. |
| `tier` | enum | `A`, `B`, `C`. |
| `score` | int | 0-100, fit + intent. |
| `trigger` | text | The dated event, short. Blank if none. |
| `trigger_date` | date | `YYYY-MM-DD`. |
| `trigger_source` | url | Required whenever `trigger` is set. |
| `contact_name` | text | `unmapped` if no named buyer found. |
| `title` | text | Verbatim title. |
| `persona_role` | enum | `economic-buyer`, `champion`, `user`, `technical`, `unmapped`. |
| `email` | text | Verified business email, or blank if none. |
| `email_status` | enum | `valid`, `risky` (catch-all), blank if unverified/dropped. |
| `source` | text | Provider/registry that produced the contact row. |
| `confidence` | enum | `high`, `medium`, `low` — how sure you are of the firmographics. |

## Scoring rubric (paste into the sheet's second tab)

```
score = industry_match (0-20)
      + size_match     (0-20)
      + geo_match      (0-10)
      + trigger        (0-30)
      + committee_found(0-10)
disqualifier present  ->  reject (do not score)
tier: A >= 70, B = 40-69, C < 40
```

## Method note (ship with every sheet)

```
Sources:        <providers, registries, directories used>
Filters:        <firmographics in / disqualifiers out>
Date range:     <when signals were collected>
Coverage:       <x% of rows have a verified email; y% have a mapped buyer>
Unverified:     <fields you could not confirm>
Suppression:    <list checked on YYYY-MM-DD>
```

## Example rows (illustrative shape only — never ship fabricated data)

```csv
account_name,domain,segment,headcount_band,geography,tier,score,trigger,trigger_date,trigger_source,contact_name,title,persona_role,email,email_status,source,confidence
Example Clinic Group,exampleclinic.example,outpatient-clinics,200-500,Nairobi Metro,A,78,"Opened 3rd site",2026-09-12,https://example.example/press,Jane Doe,Chief Operating Officer,economic-buyer,jane@exampleclinic.example,valid,ProviderX,high
Example Clinic Group,exampleclinic.example,outpatient-clinics,200-500,Nairobi Metro,A,78,"Opened 3rd site",2026-09-12,https://example.example/press,unmapped,,unmapped,,,ProviderX,high
```

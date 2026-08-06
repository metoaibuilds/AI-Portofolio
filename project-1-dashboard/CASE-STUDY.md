# Case Study: Ni Asap Financial Dashboard
**Client:** Ni Asap (restaurant, Nias Island, Indonesia)
**Role:** Solo build — requirements through delivery
**Tools:** Excel, formula-driven modeling, [Claude API — Week 4]

## The Problem
[2-3 sentences from your REQUIREMENTS.md Section 1 — staff tracking
in Excel, cash flowing through a personal account before reaching the
business account, no real-time profit visibility, no waste tracking.]

## The Approach
1. Conducted structured requirements interview → defined MVP scope,
   deliberately separated Phase 2 features (balance sheet, tax report)
   to ship value fast
2. Designed a normalized data model (4 sheets) built for a non-technical
   manager to fill in under 5 minutes/day
3. Built KPI dashboard: revenue, cost breakdown, margin, payment-method
   split — [screenshot]
4. Built P&L statement separating COGS from operating costs — surfaced
   gross margin at [X]%, [above/below] the healthy 60-70% band for
   Indonesian casual dining
5. Built break-even model with 3 scenarios (quiet/normal/strong) —
   monthly break-even revenue: [your Day 9 number]
6. [Week 4: AI anomaly detection + plain-language insights]

## What Made This Non-Generic
- Embedded real operational knowledge: batch-purchasing expense
  rhythms, weather sensitivity, PNS payday demand cycles — informed
  what the model treats as "normal" vs. "anomalous"
- Caught and fixed a live formula bug (relative vs. absolute
  reference) causing payment-split percentages to overstate by 35%
- Bilingual by design: Bahasa Indonesia for daily use

## Result
[Week 4: sold-out days tracked, waste trend visible, anomalies caught
— fill in after AI layer + a real month of data]

## Screenshots
[KPI dashboard, 3 charts, P&L sheet, break-even scenarios]
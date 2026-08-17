# Tokyosnap Studio Financial Dashboard — Requirements v1.0
**Owner:** Metodius · **Business:** Tokyosnap Studio (self-photo studio) · **Date:** July 2026

## 1. Problem
Orders come via WhatsApp Business; the operator manually re-enters each
order into a Google Sheet after payment. A WhatsApp → Sheets automation
was attempted but is unreliable, so entry remains manual. Consequences:
- No real-time visibility into revenue vs. the IDR 4,000,000/month net
  income target
- No breakdown by package or add-on — cannot tell which offerings drive
  profit or which are underperforming
- No structured cost tracking against the target

## 2. Users
- **Owner** (Metodius, remote): full financial view, target tracking, alerts
- **Operator** (on-site): daily order entry
- Language: Bahasa Indonesia primary, English toggle

## 3. Pricing Reference (locked into a lookup table, not re-typed per order)
| Package | Price (IDR) | Duration |
|---|---|---|
| Single | 40,000 | 15 min |
| Couple | 70,000 | 20 min |
| Trio | 100,000 | 20 min |
| Group (4) | 135,000 | 20 min |

| Add-on | Price (IDR) |
|---|---|
| Extra 10 min | 30,000 |
| Extra 15 min | 50,000 |
| Extra 20 min | 60,000 |
| Costume — Hanbok Pria | 20,000 |
| Costume — Hanbok Wanita | 15,000 |
| Costume — Animal | 15,000 |
| Extra background | 15,000 |
| Extra person | 25,000 |
| Print | 8,000 |

## 4. Data Inputs (per order, entered by operator)
Date, time, package type, add-ons selected (multi), total paid (IDR,
cross-checked against pricing table), payment method.
Monthly: salary, rent, electricity, internet, app subscriptions,
photo paper, printer ink/ribbon, battery, operational misc, occasional
asset purchases (flagged separately from the target calculation).

## 5. Dashboard Outputs (MVP)
- Daily & monthly revenue, split: base package revenue vs. add-on revenue
- **Target tracker:** progress toward IDR 4,000,000 net income this
  month — gap remaining, days left, required daily average to close it
- Cost breakdown by category
- Package popularity ranking (which sells most, which is neglected)
- **Add-on attach rate by package**, trended — this is the lever

## 6. AI Layer (Week 4)
- Add-on attach-rate trend alert: flags which specific add-on dropped,
  by how much, over what window — feeds the operator advertising nudge
- Slow-day / slow-week detection vs. recent baseline
- Monthly plain-language summary in Bahasa Indonesia: progress vs.
  target + the single highest-leverage recommendation

## 7. Phase 2 (out of MVP scope)
- Reliable WhatsApp Business API → Sheets/dashboard automation (n8n,
  Weeks 5-6 skill — genuine upgrade path once built)
- Asset depreciation tracking for camera/printer/equipment

## 8. Success Criteria
1. Operator logs an order in under 60 seconds using dropdowns, not
   free-typing prices
2. Owner sees real-time progress toward the 4,000,000 target from
   anywhere
3. AI identifies the single fastest lever to close any monthly gap
4. Dashboard replaces the Google Sheet as the operational source of truth
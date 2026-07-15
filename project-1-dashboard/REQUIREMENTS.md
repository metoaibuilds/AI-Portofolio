# Ni Asap Financial Dashboard — Requirements v1.0
**Owner:** Metodius · **Date:** July 2026 · **Status:** Approved for build

## 1. Problem
Ni Asap (restaurant, Nias Island) tracks money via staff reports typed into
Excel. Daily cash is deposited into the owner's personal account, mixed with
QRIS and bank-transfer income. Consequences:
- No real-time view of profit or margin
- Business and personal money are mixed (audit/tax risk)
- No visibility into waste vs sell-out; production planning is guesswork
- Anomalies (missing cash, cost spikes) are found late or never

## 2. Users
- **Owner** (remote, Australia/anywhere): full view, alerts, monthly reports
- **Manager** (on-site, Nias): daily data entry, daily view
- Language: UI and AI outputs in Bahasa Indonesia; English toggle

## 3. Data Inputs (entered daily/monthly by manager)
| Input | Frequency | Detail |
|---|---|---|
| Sales income | Daily | Split by payment method: cash / QRIS / transfer |
| Sell-through | Daily | Sold out? (Y/N), leftover/waste estimate (IDR) |
| Ingredients | Per purchase | Amount + supplier |
| Staff wages | Monthly | Per staff member |
| Fixed costs | Monthly | Rent, electricity, internet, app subscriptions |
| Operational | As occurs | Gas, packaging, repairs, misc |

## 4. Dashboard Outputs (MVP)
- Daily & monthly revenue (by payment method)
- Cost breakdown by category
- Profit margin (gross & net), break-even point
- Sell-through tracker: sold-out days vs leftover/waste trend
- **UMKM tax position:** YTD gross revenue vs IDR 500M exemption threshold,
  estimated 0.5% final tax if threshold is passed
- Auto-generated monthly report (PDF)

## 5. AI Layer (owner/manager only — Claude API)
- Anomaly & warning flags: cost spikes, revenue dips, cash vs QRIS ratio
  shifts, waste increasing, "nonsense" entries (e.g. negative sales,
  duplicate expenses, unusually round numbers)
- Plain-language monthly summary (Bahasa Indonesia)
- Q&A over the data ("berapa margin bulan lalu?")

## 6. Phase 2 (explicitly out of MVP scope)
- Asset register & depreciation schedule
- Balance sheet
- Formal annual tax report generation
- Recommendation: open a dedicated business bank account

## 7. Success Criteria
1. Manager enters a full day's data in under 5 minutes
2. Owner sees yesterday's profit from anywhere, any time
3. AI flags at least: cost anomalies, waste trends, suspicious entries
4. Sell-through data enables production planning toward the real goal:
   customers fed, stock sold out daily
5. Becomes portfolio case study #1 with measurable before/after
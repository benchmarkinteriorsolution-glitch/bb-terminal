# BB Terminal

A free, always-on stock dashboard for NSE. It runs on GitHub's servers, so your laptop can be off.

- **Momentum Core** (70% of paper capital): the 20 strongest stocks in the top 500, rebalanced in Jan, Apr, Jul and Oct.
- **Breakout (experimental)** (30%): stocks that close at a new 52-week high on heavy volume; +15% target, −8% closing stop, 90-day limit.

Runs automatically: 09:00 IST reminder, a live scan every ~20 minutes during market hours, and confirmed signals at 16:50 IST.
Prices come from Yahoo Finance (about 15 minutes delayed). This is a paper portfolio: you place real orders yourself.

**Files:** `bundle.py` holds the app (engine + dashboard) and is unpacked by each cloud run; `.github/workflows/terminal.yml` is the schedule; `log/equity.csv` is the daily paper-portfolio record.

Strategy tests: all NSE-listed stocks, 2016–2026, point-in-time top-500 universe, rules picked on 2017–21 and checked on 2022–26, after 20% tax and 0.3% costs. Past results don't guarantee future returns.

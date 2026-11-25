"""Small fixes applied after bundle.py unpacks the app: NSE holiday calendar, clearer exit label."""
FIXES = [
    ("bbsys/core.py",
     "def now_ist():\n    return dt.datetime.now(IST)\n",
     "def now_ist():\n    return dt.datetime.now(IST)\n\n"
     "# NSE equity trading holidays on weekdays. Add next year's list each December.\n"
     "NSE_HOLIDAYS = {\"2026-10-02\", \"2026-10-20\", \"2026-11-10\", \"2026-11-24\", \"2026-12-25\"}\n\n"
     "def is_trading_day(d):\n    d = pd.Timestamp(d)\n"
     "    return d.weekday() < 5 and d.strftime(\"%Y-%m-%d\") not in NSE_HOLIDAYS\n"),
    ("bbsys/core.py",
     "    if t.weekday() >= 5: return \"CLOSED\"\n",
     "    if not is_trading_day(t.date()): return \"HOLIDAY\" if t.weekday() < 5 else \"CLOSED\"\n"),
    ("bbsys/core.py",
     "and not after_close and now_ist().weekday() < 5:",
     "and not after_close and is_trading_day(today):"),
    ("bbsys/build.py",
     "    while d.weekday() >= 5: d += pd.Timedelta(days=1)",
     "    while not K.is_trading_day(d): d += pd.Timedelta(days=1)"),
    ("bbsys/build.py",
     "    def once(key):\n        if key in sent: return False",
     "    holiday = not K.is_trading_day(K.now_ist().date())\n"
     "    def once(key):\n        if holiday: return False\n        if key in sent: return False"),
    ("site/index.html",
     "${x.kind==='BUY'?'Stop (close)':''}</div>${x.kind==='BUY'&&x.stop?'<span class=\"dn\">'+inr(x.stop)+'</span>':''}",
     "${x.kind!=='BUY'?'':x.stop?'Stop (close)':'Exit rule'}</div>${x.kind!=='BUY'?'':x.stop?'<span class=\"dn\">'+inr(x.stop)+'</span>':'Quarterly review'}"),
    ("config.json", '"start_date": "2026-11-25"', '"start_date": "2026-11-23"'),
    ("bbsys/build.py", ": monthly rebalance\"", ": quarterly rebalance\""),
]
for path, old, new in FIXES:
    s = open(path, encoding="utf-8").read()
    if new in s: continue
    assert s.count(old) == 1, f"hotfix: pattern not found once in {path}"
    open(path, "w", encoding="utf-8").write(s.replace(old, new))
print("hotfix applied")

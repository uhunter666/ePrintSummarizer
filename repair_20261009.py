#!/usr/bin/env python3
"""修复 2026-10-09 批次里 JSON 解析失败的摘要（qwen3 思考模式 bug 导致）。

- 取回编号 2372..2406 的论文元数据
- 用修好的配置（think: false）重新摘要
- 就地把报告里含 "[Summary generation failed" 的条目替换为正确条目
- 重建 HTML
"""
import sys, re, logging
from pathlib import Path

ROOT = Path("/home/lym/ClaudeProjects/ePrintSummary")
sys.path.insert(0, str(ROOT / "src"))
logging.basicConfig(level=logging.WARNING)

from eprint_summary.config_manager import load_config
from eprint_summary.fetcher import fetch_new_papers, backfill_papers
from eprint_summary.summarizer import summarize_paper
from eprint_summary.keyword_matcher import match_keywords
from eprint_summary.models import PaperWithSummary
from eprint_summary.report import _format_paper_entry, generate_html_report

YEAR = 2026
LO, HI = 2372, 2406
MD = ROOT / "reports" / f"eprint_{YEAR}.md"

cfg = load_config(ROOT / "config.yaml")
print(f"think={cfg.llm.think} model={cfg.llm.model_name}")

# 1) 取论文元数据
idx = {}
try:
    for p in fetch_new_papers({YEAR: LO - 1}, YEAR):
        idx[p.paper_id] = p
except Exception as e:
    print("fetch_new_papers failed:", e)
need = [f"{YEAR}/{n}" for n in range(LO, HI + 1)]
missing = [pid for pid in need if pid not in idx]
if missing:
    print("backfill for missing:", missing[:8], "...")
    try:
        for p in backfill_papers(YEAR, {YEAR: LO - 1}):
            idx.setdefault(p.paper_id, p)
    except Exception as e:
        print("backfill failed:", e)
missing = [pid for pid in need if pid not in idx]
print(f"have metadata: {len(idx)} | still missing: {missing}")

# 2) 重新摘要
rebuilt = {}
for pid in need:
    p = idx.get(pid)
    if not p:
        continue
    s = summarize_paper(p, cfg.llm)
    is_match, kws = match_keywords(p, cfg.keywords)
    rebuilt[pid] = PaperWithSummary(paper=p, summary=s, is_keyword_match=is_match, matched_keywords=kws)
    flag = "OK " if "Summary generation failed" not in (s.contributions or "") else "BAD"
    print(f"  [{flag}] {pid}  {p.title[:60]}")

# 3) 就地替换坏条目
md = MD.read_text(encoding="utf-8")
entry_re = re.compile(r"### [^\n]*\[(\d{4}/\d+)\][^\n]*\n.*?\n---\n", re.DOTALL)
out, pos, n_repl = [], 0, 0
for m in entry_re.finditer(md):
    pid = m.group(1)
    block = m.group(0)
    if "Summary generation failed" in block and pid in rebuilt:
        out.append(md[pos:m.start()])
        out.append(_format_paper_entry(rebuilt[pid]))
        pos = m.end()
        n_repl += 1
out.append(md[pos:])
new_md = "".join(out)
MD.write_text(new_md, encoding="utf-8")
print(f"replaced {n_repl} entries")

# 4) 重建 HTML
generate_html_report(MD)
left = new_md.count("Summary generation failed")
print(f"remaining 'Summary generation failed' in md: {left}")

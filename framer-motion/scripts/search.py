#!/usr/bin/env python3
"""
Framer Motion Skill — Search Engine
Usage:
  python3 search.py "<query>" --domain <domain> [-n <results>]

Domains:
  animations  — Animation types, triggers, variants code
  patterns    — Code patterns and implementation approaches
  easing      — Easing curves and spring configs
  components  — Framer Motion API components and hooks
  all         — Search all domains
"""

import sys
import csv
import argparse
import os
import math
from collections import defaultdict

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SKILL_DIR, "..", "data")

DOMAIN_FILES = {
    "animations": "animations.csv",
    "patterns": "patterns.csv",
    "easing": "easing.csv",
    "components": "components.csv",
}

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def tokenize(text):
    if not text:
        return []
    return text.lower().replace(",", " ").replace("_", " ").replace("-", " ").split()

def bm25_score(query_tokens, doc_tokens, avgdl, k1=1.5, b=0.75):
    freq = defaultdict(int)
    for t in doc_tokens:
        freq[t] += 1
    dl = len(doc_tokens)
    score = 0.0
    for qt in query_tokens:
        if qt in freq:
            tf = freq[qt]
            idf = math.log((1 + 1) / (1 + 1) + 1)  # simplified
            score += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / max(avgdl, 1)))
    return score

def search_domain(domain, query, n=5):
    filename = DOMAIN_FILES.get(domain)
    if not filename:
        return []
    rows = load_csv(filename)
    if not rows:
        return []

    query_tokens = tokenize(query)
    avgdl = sum(len(tokenize(" ".join(str(v) for v in r.values()))) for r in rows) / max(len(rows), 1)

    scored = []
    for row in rows:
        doc_text = " ".join(str(v) for v in row.values())
        doc_tokens = tokenize(doc_text)
        score = bm25_score(query_tokens, doc_tokens, avgdl)
        # Boost exact matches
        if any(qt in doc_text.lower() for qt in query_tokens):
            score += 2.0
        scored.append((score, row))

    scored.sort(key=lambda x: -x[0])
    return [(s, r) for s, r in scored[:n] if s > 0]

def format_result(domain, row, rank):
    lines = [f"### Result {rank}"]
    for k, v in row.items():
        if k is not None and v is not None and str(v).strip():
            label = str(k).replace("_", " ").title()
            lines.append(f"- **{label}:** {str(v)}")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Framer Motion Skill Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", default="all", choices=list(DOMAIN_FILES.keys()) + ["all"])
    parser.add_argument("-n", "--num", type=int, default=5)
    args = parser.parse_args()

    print(f"## Framer Motion Skill — Search Results")
    print(f"**Query:** {args.query} | **Domain:** {args.domain}\n")

    if args.domain == "all":
        domains = list(DOMAIN_FILES.keys())
    else:
        domains = [args.domain]

    total = 0
    for domain in domains:
        results = search_domain(domain, args.query, args.num)
        if not results:
            continue
        print(f"---\n### 📁 Domain: `{domain}`\n**Found:** {len(results)} results\n")
        for i, (score, row) in enumerate(results, 1):
            print(format_result(domain, row, i))
            print()
        total += len(results)

    if total == 0:
        print("No results found. Try broader terms like: entrance, scroll, hover, spring, modal, list, page")

if __name__ == "__main__":
    main()

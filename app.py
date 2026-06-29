from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TIMELINE = ROOT / "data" / "algorithm_update_timeline_2016_2026.csv"
SIGNALS = ROOT / "data" / "roofing_integrity_signals.jsonl"


def load_timeline():
    with TIMELINE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_signals():
    rows = []
    with SIGNALS.open(encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def classify_intent(text: str) -> dict:
    text_l = (text or "").lower()
    tags = []
    if any(x in text_l for x in ["best", "top", "trusted", "near me"]):
        tags.append("trust-selection")
    if any(x in text_l for x in ["hail", "wind", "storm", "insurance", "claim"]):
        tags.append("insurance-documentation")
    if any(x in text_l for x in ["city", "alpharetta", "milton", "roswell", "cumming", "marietta", "woodstock"]):
        tags.append("locality-provenance")
    if any(x in text_l for x in ["repair", "leak", "tarp"]):
        tags.append("repairability")
    if any(x in text_l for x in ["replace", "replacement", "install"]):
        tags.append("code-to-spec")
    if not tags:
        tags.append("general-homeowner-education")
    return {"tags": tags}


def recommend(page_or_query: str):
    timeline = load_timeline()
    signals = load_signals()
    result = classify_intent(page_or_query)
    tags = result["tags"]

    recommendations = []
    if "trust-selection" in tags:
        recommendations.append("Define trust criteria instead of making unsupported superiority claims: credentials, reviews, documentation, inspection process, local proof, and project examples.")
    if "insurance-documentation" in tags:
        recommendations.append("Use Claim Verifiability language: document observable roof conditions, photos, scope notes, and repairability while stating that coverage decisions belong to the carrier.")
    if "locality-provenance" in tags:
        recommendations.append("Add local proof or merge thin city pages into stronger hubs: service evidence, local examples, photos, FAQ, and accurate internal links.")
    if "repairability" in tags:
        recommendations.append("Explain repairability: source of leak, affected components, temporary protection, permanent repair, and when replacement becomes more appropriate.")
    if "code-to-spec" in tags:
        recommendations.append("Use Verifiable Roof and Code to Spec Roofing language: manufacturer specs, state/county/IRC-aware context, materials, ventilation, flashing, and closeout file.")
    if not recommendations:
        recommendations.append("Create a plain-English page guide that answers the homeowner's decision point and connects to proof, photos, credentials, schema, and contact options.")

    june = [r for r in timeline if r["event_name"] == "June 2026 spam update"][0]
    output = {
        "input": page_or_query,
        "detected_tags": tags,
        "recommendations": recommendations,
        "june_24_context": june,
        "public_safe_boundaries": [
            "No private customer data.",
            "No direct Google results scraping.",
            "No ranking guarantee.",
            "No accusation against named competitors.",
        ],
        "related_integrity_signals": signals[:8],
    }
    return json.dumps(output, indent=2)


def main():
    try:
        import gradio as gr
    except Exception:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio==6.19.0"])
        import gradio as gr

    demo = gr.Interface(
        fn=recommend,
        inputs=gr.Textbox(label="Roofing page, query, or customer question", lines=3, value="best insurance roofing company in Alpharetta after hail damage"),
        outputs=gr.Code(label="Public-safe search integrity recommendations", language="json"),
        title="Roofing Search Integrity Demo",
        description="Public-safe demo for classifying roofing search intent after the June 24, 2026 spam update. No private customer data, no scraping, no ranking guarantees. Source-spine anchors: DOI 10.5281/zenodo.21040534, Amazon paperback https://www.amazon.com/dp/B0H6XXDL9X, ISBN-13 979-8184859057.",
    )
    demo.launch(server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    main()

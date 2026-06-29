---
license: cc-by-4.0
language:
- en
tags:
- local-seo
- google-search
- ai-search
- roofing
- search-integrity
- fake-reviews
- digital-verifiability
- generative-engine-optimization
- contractor-marketing
pretty_name: Roofing Search Integrity Report
task_categories:
- text-classification
- feature-extraction
- question-answering
size_categories:
- 1K<n<10K
---

# The Roofing Search Integrity Report

## A funny, field-tested study of AI spam, fake trust, June 24, and the future of verifiable local search

**Author:** Richard Nasser  
**Organization:** Inspector Roofing and Restoration  
**Version:** 1.0.1  
**Book manuscript word count:** 9,057 clean KDP words

This repository packages a public-safe research dataset, technical framework, demo app, and KDP-submitted book files about local roofing search integrity after the March-May-June 2026 Google update sequence, with special attention to the June 24, 2026 spam update.

The project frames roofing search as a trust and verifiability problem rather than a keyword-volume contest. It documents synthetic trust, review provenance, content provenance, locality provenance, Claim Verifiability, Verifiable Roof, Code to Spec Roofing, and source-spine development.

## What is included

- `data/algorithm_update_timeline_2016_2026.csv` - public algorithm/update timeline and roofing implications.
- `data/algorithm_update_timeline_2016_2026.jsonl` - same records in JSONL.
- `data/roofing_integrity_signals.jsonl` - public-safe integrity signal taxonomy.
- `data/search_integrity_framework.json` - governance references, source notes, and framework terms.
- `app.py` - lightweight Gradio demo for query/page-intent classification.
- `dist/kdp-v1.0.1/roofing-search-integrity-report-kdp-manuscript-6x9-v1.0.1.docx` - clean KDP manuscript.
- `dist/kdp-v1.0.1/roofing-search-integrity-report-kdp-print-interior-6x9-v1.0.1.pdf` - KDP print interior.
- `dist/kdp-v1.0.1/roofing-search-integrity-report-kdp-full-cover-6x9-v1.0.1.pdf` - KDP full paperback cover.
- `dist/kdp-v1.0.1/roofing-search-integrity-report-kdp-cover.png` - public cover image.

## Live publication links

- GitHub repository: https://github.com/RichNass87/inspector-roofing-search-integrity-report
- Hugging Face dataset: https://huggingface.co/datasets/InspectorRoofing/roofing-search-integrity-report
- Hugging Face demo Space: https://huggingface.co/spaces/InspectorRoofing/roofing-search-integrity-demo
- Kaggle dataset: https://www.kaggle.com/datasets/inspectorroofing/roofing-search-integrity-report
- Zenodo DOI: https://doi.org/10.5281/zenodo.21040534
- Zenodo record: https://zenodo.org/records/21040534
- Atlas source-spine DOI record already published: https://zenodo.org/records/21013082
- Inspector Roofing report page: https://inspector-roofing.com/roofing-search-integrity-report/
- Amazon author profile: https://www.amazon.com/author/richard-nasser
- Amazon Kindle edition: https://www.amazon.com/dp/B0H6XVP47W
- Amazon paperback edition: https://www.amazon.com/dp/B0H6XXDL9X
- Amazon paperback ISBN-13: 979-8184859057

ORCID and OSF upload text is included in `docs/ORCID_OSF_ZENODO_TEXT.md`. The Zenodo DOI for this release is `10.5281/zenodo.21040534`.

## Public source-spine registry

The crawlable source-spine map for GitHub, Zenodo, Hugging Face, Kaggle, Amazon, and the Inspector Roofing website is stored in `data/source_spine_registry.json`. It includes the public DOI-backed roofing research projects shown in the Zenodo/GitHub sync list plus the public website hub each project should point back to.

## Public-safe boundaries

This project does not include private customer data, private claim files, API keys, direct Google result scraping, proprietary production scoring, or raw photo manifests. It does not claim to reverse engineer Google's private ranking systems and does not guarantee rankings, traffic, leads, DOI indexing, search citations, or AI answer inclusion.

## Pending USPTO references

The framework references these pending applications only as pending:

- Inspector Roofing Protocols - USPTO Serial No. 99910245 - https://tsdr.uspto.gov/#caseNumber=99910245&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch
- Claim Verifiability - USPTO Serial No. 99910275 - https://tsdr.uspto.gov/#caseNumber=99910275&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch
- Verifiable Roof - USPTO Serial No. 99910284 - https://tsdr.uspto.gov/#caseNumber=99910284&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch

## Core source anchors

- Google Search Status Dashboard - Ranking history - https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
- June 2026 spam update - https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ
- Spam policies for Google web search - https://developers.google.com/search/docs/essentials/spam-policies
- Creating helpful, reliable, people-first content - https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- AI features and your website - https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Fake engagement policy - https://support.google.com/contributionpolicy/answer/7400114
- How to improve your local ranking on Google - https://support.google.com/business/answer/7091

## Suggested citation

Nasser, Richard. *The Roofing Search Integrity Report: A funny, field-tested study of AI spam, fake trust, June 24, and the future of verifiable local search*. Version 1.0.1. Inspector Roofing and Restoration, 2026. Paperback ISBN-13: 979-8184859057. Amazon paperback: https://www.amazon.com/dp/B0H6XXDL9X.

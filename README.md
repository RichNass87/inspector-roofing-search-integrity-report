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

![The Roofing Search Integrity Report by Richard Amir Nasser](https://inspector-roofing.com/wp-content/uploads/2026/07/roofing-search-integrity-report-richard-amir-nasser.png)

## A funny, field-tested study of AI spam, fake trust, June 24, and the future of verifiable local search

**Author:** Richard Amir Nasser  
**Organization:** Inspector Roofing and Restoration  
**Version:** 1.0.3  
**Book manuscript word count:** 9,057 clean KDP words

This repository packages a public-safe research dataset, technical framework, demo app, and KDP-submitted book files about local roofing search integrity after the March-May-June 2026 Google update sequence, with special attention to the June 24, 2026 spam update.

The project frames roofing search as a trust and verifiability problem rather than a keyword-volume contest. It documents synthetic trust, review provenance, content provenance, locality provenance, Claim Verifiability, Verifiable Roof, Code to Spec Roofing, and source-spine development.

## What is included

- `data/algorithm_update_timeline_2016_2026.csv` - public algorithm/update timeline and roofing implications.
- `data/algorithm_update_timeline_2016_2026.jsonl` - same records in JSONL.
- `data/roofing_integrity_signals.jsonl` - public-safe integrity signal taxonomy.
- `data/search_integrity_framework.json` - governance references, source notes, and framework terms.
- `data/public_source_spine_links.json` - canonical cross-platform identity and Q-data link contract.
- `docs/SOURCE_SPINE.md` - human-readable source-spine map.
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
- Zenodo DOI: https://doi.org/10.5281/zenodo.21045292
- Zenodo record: https://zenodo.org/records/21045292
- Atlas source-spine DOI record already published: https://zenodo.org/records/21013082
- Inspector Roofing report page: https://inspector-roofing.com/roofing-search-integrity-report/
- Richard Amir Nasser person hub: https://inspector-roofing.com/richard-nasser/
- Richard Amir Nasser bibliography: https://inspector-roofing.com/author-richard-nasser/
- Inspector Roofing Authority Stack: https://inspector-roofing.com/authority-stack/
- ORCID: https://orcid.org/0009-0000-2980-7543
- Wikidata report item: https://www.wikidata.org/wiki/Q140522693
- Amazon author profile: https://www.amazon.com/author/richard-nasser
- Amazon Kindle edition: https://www.amazon.com/dp/B0H6XVP47W
- Amazon paperback edition: https://www.amazon.com/dp/B0H6XXDL9X
- Amazon paperback ISBN-13: 979-8184859057

## Canonical source spine

The canonical identity is Richard Amir Nasser. The report entity is anchored to Wikidata item Q140522693 and connected to the official report page, ORCID, versioned GitHub source, Hugging Face dataset, Zenodo DOI record, bibliography hub, and Amazon author profile.

The cross-platform link contract is maintained in `data/public_source_spine_links.json` and documented in `docs/SOURCE_SPINE.md`. These are public provenance links, not independent certification or endorsement.

## Public source-spine registry

The crawlable source-spine map for GitHub, Zenodo, Hugging Face, Kaggle, Amazon, and the Inspector Roofing website is stored in `data/source_spine_registry.json`. It includes the public DOI-backed roofing research projects shown in the Zenodo/GitHub sync list plus the public website hub each project should point back to.

## Public-safe boundaries

This project does not include private customer data, private claim files, API keys, direct Google result scraping, proprietary production scoring, or raw photo manifests. It does not claim to reverse engineer Google's private ranking systems and does not guarantee rankings, traffic, leads, DOI indexing, search citations, or AI answer inclusion.

## Pending USPTO references

The framework references these pending applications only as pending:

- Inspector Roofing Protocols - USPTO Serial No. 99910245 - https://tsdr.uspto.gov/#caseNumber=99910245&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch
- Claim Verifiability - USPTO Serial No. 99910275 - https://tsdr.uspto.gov/#caseNumber=99910275&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch

## Related Clean Dataset

The cleaned roof-photo archive linked to the current public entity stack is:

- Roof Damage Atlas: Inspector Roofing Residential Roof Dataset
- Hugging Face: https://huggingface.co/datasets/InspectorRoofing/inspector-roofing-residential-storm-damage-dataset
- Clean archive size: 46,548 cleaned JPEG images
- Metadata-backed images: 46,521
- Safety filter: faces, readable letters and numbers, non-roof or uncertain images, and metal-roof-looking images were removed
- Zenodo companion record: https://doi.org/10.5281/zenodo.21045292

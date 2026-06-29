# Publish Log

## Completed

- GitHub repository published: https://github.com/RichNass87/inspector-roofing-search-integrity-report
- Hugging Face dataset published: https://huggingface.co/datasets/InspectorRoofing/roofing-search-integrity-report
- Hugging Face demo Space published: https://huggingface.co/spaces/InspectorRoofing/roofing-search-integrity-demo
- Kaggle dataset published and ready: https://www.kaggle.com/datasets/inspectorroofing/roofing-search-integrity-report
- Local KDP/source-spine ZIP created: `/Users/richardnasser/Desktop/inspector-roofing-search-integrity-report-kdp-source-spine-v1.0.0.zip`
- Inspector Roofing report page published: https://inspector-roofing.com/roofing-search-integrity-report/
- Amazon KDP submitted on 2026-06-29: Kindle eBook publishing/in review at $4.99 USD, ASIN B0H6XVP47W; paperback publishing at $9.99 USD, ASIN B0H6XXDL9X, ISBN-13 979-8184859057, public Amazon URL https://www.amazon.com/dp/B0H6XXDL9X.
- Hugging Face Space metadata fixed on 2026-06-29 with `sdk: gradio` and pinned Gradio requirements.
- GitHub release v1.0.1 published: https://github.com/RichNass87/inspector-roofing-search-integrity-report/releases/tag/v1.0.1
- Zenodo DOI minted from the GitHub release: https://doi.org/10.5281/zenodo.21040534
- Zenodo record: https://zenodo.org/records/21040534

## Built and verified

- 20,692-word KDP manuscript.
- DOCX rendered through LibreOffice to 42 pages.
- PDF interior rendered to 41 pages.
- Cover PNG generated and inspected.
- App smoke test passed.
- Unit tests passed.
- Kaggle file listing verified.

## Needs platform session or manual upload

- ORCID: use `docs/ORCID_OSF_ZENODO_TEXT.md` to create a work entry.
- OSF: use `docs/ORCID_OSF_ZENODO_TEXT.md` plus the ZIP. Prior OSF project state has shown platform review/spam-review friction.

## 2026-06-29 platform retry

- Zenodo reached the logged-in `New upload` page for `richard@inspector-roofing.com`.
- Zenodo upload controls were present, but the Chrome file chooser did not open from the visible upload card or the hidden multi-file input.
- Chrome, the Codex Chrome Extension, and the native host manifest all checked as installed and enabled after the upload failure, but browser control then timed out on the required lightweight retry.
- No DOI, ORCID work entry, or OSF project was confirmed from this retry. Use the manual field list in `docs/ORCID_OSF_ZENODO_TEXT.md` and the source ZIP on the Desktop to finish the three platform records.

## 2026-06-29 KDP and app sync

- KDP bookshelf confirmed the title "The Roofing Search Integrity Report: A funny, field-tested study of AI spam, fake trust, June 24, and the future of verifiable local search" under Richard Nasser.
- Kindle eBook status: In review.
- Paperback status: Publishing.
- Hardcover: not created.
- Kindle ASIN: B0H6XVP47W.
- Paperback ASIN: B0H6XXDL9X.
- Paperback ISBN-13: 979-8184859057.
- Public Amazon paperback URL: https://www.amazon.com/dp/B0H6XXDL9X.
- Hugging Face runtime compatibility fixed with `audioop-lts>=0.2.1` and `huggingface_hub<1.0` pins.
- Hugging Face Space records moved past the missing-SDK configuration error after README front matter was updated.
- GitHub release v1.0.1 created and Zenodo minted DOI 10.5281/zenodo.21040534.
- GitHub release v1.0.2 prepared after Amazon paperback listing went live, adding paperback ASIN B0H6XXDL9X, ISBN-13 979-8184859057, and public Amazon URL https://www.amazon.com/dp/B0H6XXDL9X across README, schema, Zenodo metadata, citation metadata, Kaggle metadata, and the source-spine registry.
- Hugging Face Spaces were updated to Gradio 6.19.0 after Gradio 4.x failed on the current Hugging Face Python runtime.

## Public-safe boundaries

This release intentionally avoids private customer data, private claim files, private photo manifests, API keys, direct Google result scraping, ranking guarantees, and claims that pending USPTO marks are registered.

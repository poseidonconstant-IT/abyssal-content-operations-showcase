# AI-Powered Multi-Platform Content Operations Platform

A public, portfolio-safe case study for **The Abyssal Capital**: a Python system
for AI-assisted financial-content operations. The production repository remains
private because it contains operational configuration and runtime data.

This repository intentionally contains **no credentials, API tokens, production
data, draft content, or publishing controls**.

## Problem

Publishing research-style financial content across several platforms can become
error-prone when source review, language consistency, scheduling, delivery
failures, and auditability are handled manually.

## Solution

The system turns source ingestion into a controlled delivery pipeline:

```text
RSS ingestion
  -> duplicate suppression and topic routing
  -> Gemini-assisted drafting and quality gates
  -> human approval / HOLD
  -> output-language validation and platform presentation
  -> Telegram + Facebook + X delivery
  -> per-channel retry queue and audit log
```

## Engineering decisions

- **Human approval:** scheduled releases are held for review rather than being
  published immediately.
- **Output-language guardrail:** invalid output blocks delivery instead of
  silently falling back to unchecked content.
- **Failure isolation:** results are tracked per platform; a successful channel
  is not posted again when another channel needs a retry.
- **Operational separation:** authenticated operations controls are separate
  from the read-only portfolio view.
- **Linux deployment:** Python services are managed with `systemd`, with logs,
  retention, and runtime configuration.

## Technology

Python · Streamlit · Gemini · Telegram Bot API · Facebook Graph API · X API v2 ·
RSS/feedparser · Pillow · systemd · unittest

## Safe demonstration

`showcase_app.py` is a standalone Streamlit visualization of the architecture.
It uses no network calls, credentials, or production files.

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run showcase_app.py
```

## Scope

Educational financial content only. This case study demonstrates software
architecture and operational controls; it does not provide investment advice.

## Repository policy

All rights reserved. No license is granted for reuse or redistribution without
the owner's written permission.

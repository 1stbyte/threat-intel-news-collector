# Threat Intel News Collector

Python-based SOC automation script that collects the latest cybersecurity intelligence from trusted threat research feeds and automatically generates a structured CSV dataset for analyst workflows.

## Overview

This tool aggregates cybersecurity alerts from multiple intelligence sources and converts them into structured CSV output to support:

* Threat awareness monitoring
* Detection engineering research
* SOC analyst daily briefings
* Investigation preparation workflows

The script demonstrates how lightweight automation can transform unstructured threat intelligence into actionable datasets usable in security operations environments.

## Features

* Collects threat intelligence from trusted security feeds
* Automatically generates structured CSV output
* Supports daily analyst threat-awareness tracking
* Enables detection engineering research workflows
* Lightweight Python-based SOC automation utility

## Intelligence Sources

Feeds collected include:

* CISA Alerts
* The Hacker News
* BleepingComputer
* SecurityWeek

## Output

Running the script generates:

cybersecurity_news.csv

The dataset includes:

| Source | Title | Published | Link |
| ------ | ----- | --------- | ---- |

This structured output supports:

* SOC daily threat briefings
* Threat intelligence tracking
* Detection engineering research
* Security operations knowledge sharing

## Installation

Install dependency:

pip install feedparser

## Usage

Run:

python cyber_news.py

Output file generated automatically:

cybersecurity_news.csv

## SOC Analyst Use Case

This project demonstrates how automation can convert unstructured threat intelligence feeds into structured datasets that support:

* Threat awareness monitoring
* Detection engineering research preparation
* Analyst investigation context gathering
* Security operations workflow enhancement

## Future Enhancements

Planned improvements:

* CVE extraction automation
* CISA KEV catalog correlation
* MITRE ATT&CK technique tagging
* Automated daily threat briefing generation
* SIEM hunting dataset integration

## Author

Security-focused automation project supporting SOC and Detection Engineering workflows.

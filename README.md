# MCP Tutorial

This repository contains the tutorial materials and example code for my **YouTube course on MCP (Model Context Protocol)**.
The course walks through the evolution of tool use in AI — from **Toolformer** to **MCP** — and then dives into practical examples of building MCP servers, clients, and agents.

## 📺 Course Overview

This repository follows along with the YouTube tutorial series:

### **Chapter 1 — How AI Uses Tools: From Toolformer to MCP**

* Who this course is for & prerequisites
* What a Tool is & why tools are needed
* Classical Tool Use – Toolformer (2023)
* Transition to MCP

### **Chapter 2 — MCP Fundamentals**

* Core Components — Host, Client, Server
* `tools/list` request
* `tools/call` request
* Protocol Mechanics — JSON-RPC 2.0
* Relationship with Function Calling Features

### **Chapter 3 — MCP Basics in Python**

* Setting up the MCP stdio server
* Defining MCP tools (e.g., Calculator)
* Setting up the MCP stdio client
* Calling MCP server tools from the client
* Setting up the MCP streamable HTTP server
* Setting up the MCP HTTP client

### **Chapter 4 — Connecting to Existing MCP Servers**

* Connecting to built-in servers such as **Filesystem**, **Git**, and **Tavily**

### **Chapter 5 — MCP + LLM Integration**

* How to connect MCP to an LLM (e.g., OpenAI API, LangChain/LangGraph)
* Security risks and safe design considerations

### **Chapter 6 — Future Outlook & Closing**

* What we didn’t cover and why
* Future outlook for MCP and related approaches

## 📂 Directory Structure

```
.
├── servers/     # MCP servers (stdio, HTTP, etc.)
├── clients/     # MCP clients (stdio, HTTP, etc.)
├── agents/      # Chatbot agents using OpenAI API or LangChain
└── assets/      # Slides & YouTube scripts
```


## 🚀 Getting Started

### 1. Install `uv`

Follow the instructions here: [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

For example, on macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (PowerShell):

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Run an Example

```bash
uv run clients/stdio_client.py
```

### 5. Environment Variables

Some examples(**tavily_client**, **agents**) in this project require API keys for external services (e.g., LLMs, search tools).

1. Copy `.env.example` to `.env`:
```
cp .env.example .env
```
2. Edit `.env` and replace with your own keys:
```
TAVILY_API_KEY=tvly-xxxxxx
OPENAI_API_KEY=sk-xxxxxx
```

You can get your keys here:

👉 Tavily API Key → https://app.tavily.com/

👉 OpenAI API Key → https://platform.openai.com/

## 🎯 Learning Goals

By the end of this tutorial project, you will:

* Understand what MCP is and why it matters.
* Learn how to build your own **MCP servers and clients**.
* Connect existing servers (Filesystem, Git, Tavily).
* Integrate MCP with LLMs safely.

## 📌 Notes

* This repo is designed to be **educational**, not production-ready.
* The `assets/` folder contains slides and scripts used in the videos.


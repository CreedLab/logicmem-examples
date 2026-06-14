# 🧠 LogicMem — AI Agents That Actually Remember

> **"Every AI forgets. LogicMem remembers."**

[![PyPI Version](https://img.shields.io/pypi/v/logicmem?color=blue)](https://pypi.org/project/logicmem/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Free Tier: 1,000 ops/mo](https://img.shields.io/badge/Free%20Tier-1%2C000%20ops%2Fmonth-orange)](https://logicmem.io/pricing)

**The memory layer your AI agents have been missing.** Store decisions, track outcomes, and retrieve what matters — with none of the "where did we leave off?" moments.

---

## ⚡ Quick Start

```bash
pip install logicmem

# Set your API key (free at https://logicmem.io)
export LOGICMEM_API_KEY=lm_your_key_here
```

```python
from logicmem import MemoryClient

client = MemoryClient()

# Store something important
client.store("Customer wants annual billing", outcome_score=0.9)

# Retrieve it later — weighted by outcome
results = client.retrieve("what does this customer want?")
```

**That's it.** 3 lines to add memory to any AI agent.

---

## ✨ Why LogicMem?

### 🎯 Outcome-Weighted Retrieval
Not all memories are equal. When you store an outcome score (0.0 = failed, 1.0 = succeeded), retrieval automatically boosts what actually worked.

```python
# First attempt
client.store("Suggested monthly plan", outcome_score=0.0)

# What worked
client.store("Suggested annual plan → customer bought", outcome_score=1.0)

# Retrieval knows which to surface
results = client.retrieve("what should we suggest?")
# → "Suggested annual plan → customer bought" (weighted higher)
```

### 📊 Usage Monitoring Built-In
Know exactly where you stand with `client.usage()`.

```python
usage = client.usage()
print(f"{usage['used']}/{usage['limit']} ops used")
# → "847/1000 ops used"
```

### 🔍 Semantic Search
Store anything. Retrieve by meaning — no exact matches required.

```python
client.store("Decided to use Stripe for payments")

# Retrieval understands context
results = client.retrieve("what payment processor did we pick?")
# → "Decided to use Stripe for payments" ✓
```

---

## 🔧 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                        Your AI Agent                             │
└─────────────────────────┬───────────────────────────────────────┘
                          │  1. client.store(text, outcome_score?)
                          │  2. client.retrieve(query)
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                       LogicMem API                               │
│                                                                 │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│   │   Vector DB  │◄──►│  Outcome     │◄──►│  Semantic    │    │
│   │  (storage)   │    │  Weights     │    │  Retrieval   │    │
│   └──────────────┘    └──────────────┘    └──────────────┘    │
│                                                                 │
│   Your data → encrypted at rest → delivered in milliseconds    │
└─────────────────────────────────────────────────────────────────┘
```

**1. Store** — Send text + optional outcome score (0.0–1.0) and importance (1–10)

**2. Weights** — Outcome scores train retrieval to favor successful patterns

**3. Retrieve** — Query in natural language, get back relevant memories ranked by score

---

## 🎁 Free Tier — No Credit Card Required

| | Free | Pro | Business |
|---|---|---|---|
| **Operations/month** | 1,000 | 50,000 | 500,000 |
| **Price** | $0 | $29/mo | $99/mo |
| **Credit card?** | ❌ No | $29 | $99 |
| **Outcome tracking** | ✅ | ✅ | ✅ |
| **Semantic search** | ✅ | ✅ | ✅ |
| **API access** | ✅ | ✅ | ✅ |

👉 **[Get your free API key at logicmem.io](https://logicmem.io)** (1,000 ops/month, forever)

---

## 📦 Installation

```bash
pip install logicmem
```

Requires Python 3.9+. No external dependencies — just the `logicmem` package.

---

## 🔑 Setup

1. **Get an API key** at [logicmem.io](https://logicmem.io) (free tier: 1,000 ops/month)
2. **Set the environment variable:**
   ```bash
   export LOGICMEM_API_KEY=lm_live_your_key_here
   ```
3. **Start building:**
   ```python
   from logicmem import MemoryClient
   client = MemoryClient()
   ```

---

## 📂 Examples

| Example | Description |
|---|---|
| [`01_quickstart.py`](examples/01_quickstart.py) | The 5-line memory agent |
| [`02_chatbot.py`](examples/02_chatbot.py) | Add memory to any chatbot |
| [`03_research_agent.py`](examples/03_research_agent.py) | Research agent that remembers |
| [`04_outcome_tracking.py`](examples/04_outcome_tracking.py) | The DPO pattern (outcome-weighted retrieval) |
| [`05_usage_monitoring.py`](examples/05_usage_monitoring.py) | Monitor your usage + upgrade prompt |

---

## 🚀 Use Cases

- **Customer Support Agents** — Remember preferences, past issues, what worked
- **Research Agents** — Don't re-search what you already found
- **Sales Agents** — Track pitch outcomes, learn from wins
- **Coding Assistants** — Remember architectural decisions, why you chose X
- **Autonomous Agents** — Build institutional memory that persists across sessions

---

## 📚 Full Documentation

- **[API Reference](https://logicmem.io/docs/api)** — All endpoints, parameters, responses
- **[Quick Start Guide](https://logicmem.io/docs/quickstart)** — Step-by-step integration
- **[Outcome Tracking Guide](https://logicmem.io/docs/outcomes)** — The DPO pattern explained
- **[Pricing](https://logicmem.io/pricing)** — Free forever tier + upgrades

---

## 💬 Community

Questions? Ideas? Want to contribute examples?

[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord)](https://logicmem.io/discord)

---

## 📄 License

MIT License — use it in personal projects, commercial products, whatever you want.

---

**Built with persistence** — because your AI should remember.

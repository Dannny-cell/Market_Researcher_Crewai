# 🧠 Market Researcher CrewAI

A production-ready **multi-agent AI system** built with [crewAI](https://crewai.com) that autonomously conducts end-to-end market research, competitive intelligence, customer insights, product strategy, and business analysis — all in a single pipeline.

---

## 🚀 What It Does

Five specialized AI agents work sequentially, each producing a professional-grade report:

| Agent | Role | Output |
|---|---|---|
| 🔍 Market Research Specialist | TAM/SAM/SOM sizing, trends, segmentation | Market Research Report |
| 🕵️ Competitive Intelligence Analyst | Competitor profiles, feature matrix, threat heatmap | Competitive Intelligence Briefing |
| 👥 Customer Insights Researcher | Personas, journey maps, unmet needs | Customer Insights Report |
| 🧭 Product Strategy Adviser | Vision, strategic bets, roadmap | Product Strategy Document |
| 📊 Senior Business Analyst | Unit economics, financial projections, ROI | Business & Financial Analysis |

---

## 📋 Expected Output

When you run `crewai run` with the default inputs (`AutoAgentX` / `Autonomous AI Agents`), the crew produces five sequential reports covering:

**1. Market Research Report**
- TAM projected at ~$13.4B by 2025, CAGR of 34.6%
- 5 customer segments: automotive (40%), aerospace (20%), healthcare (15%), industrial automation (10%), consumer electronics (5%)
- Top white-space: autonomous agents for industrial automation (~$4.2B opportunity)
- Key risks: regulatory uncertainty, cybersecurity, technological disruption

**2. Competitive Intelligence Briefing**
- Competitor tiers: Leaders (NVIDIA, Intel), Challengers (Microsoft, Google, Amazon), Niche (Siemens, Rockwell, ABB)
- Feature comparison matrix across 7 capability dimensions
- Recent signals: acquisitions, partnerships, and product launches (2020–present)
- Strategic recommendation: differentiate via industrial automation focus

**3. Customer Insights Report**
- 5 detailed personas across automotive, aerospace, healthcare, industrial, and consumer segments
- End-to-end journey map: Awareness → Consideration → Evaluation → Purchase → Post-purchase
- Top pain points: regulatory uncertainty, high dev costs, integration complexity, cybersecurity
- Loyalty levers: reliability, customer support, continuous innovation

**4. Product Strategy Document**
- Vision: become the leading autonomous agent provider for industrial automation
- North star: 20% market share, $2.5B revenue by 2028
- 3 strategic bets: industrial automation, healthcare, consumer autonomous vehicles
- 6–12 month roadmap with milestones and resourcing asks

**5. Business & Financial Analysis**
- Unit economics benchmarked against industry (CAC, LTV, gross margins)
- 3 financial scenarios: base, upside, downside (3–5 year horizon)
- ROI analysis for each strategic initiative
- Prioritized recommendations to optimize margins and accelerate growth

---

## 🛠️ Installation

### Prerequisites
- Python `>=3.10, <3.14`
- [uv](https://docs.astral.sh/uv/) package manager

### Install uv
```bash
pip install uv
```

### Install dependencies
```bash
crewai install
```

---

## ⚙️ Configuration

### 1. Set up `.env`
```env
OPENAI_API_BASE=https://api.groq.com/openai/v1   # Remove this line if using OpenAI directly
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL_NAME=llama-3.3-70b-versatile         # Or gpt-4o-mini for OpenAI
SERPER_API_KEY=your_serper_key_here
```

> ⚠️ **Groq free tier** has a 12,000 TPM limit. For full pipeline runs, upgrade to Groq Dev Tier or use OpenAI (`gpt-4o-mini`).

### 2. Customize inputs (`main.py`)
```python
def get_inputs():
    return {
        'product_or_company_name':           'YourCompany',
        'target_market_or_industry':         'Your Industry',
        'your_company_or_product_name':      'YourCompany',
        'target_customer_segment_or_use_case': 'Your Target Segment',
        'industry_or_market_context':        'Your Market Context',
        'product_name_or_category':          'Your Product',
        'target_market_or_customer_segment': 'Your Target Customer',
        'industry_or_competitive_context':   'Your Competitive Context',
        'company_name_or_business_objectives': 'Your Business Goal',
    }
```

### 3. Customize agents & tasks
- `src/market_researcher_crew/config/agents.yaml` — agent roles, goals, backstories
- `src/market_researcher_crew/config/tasks.yaml` — task descriptions and expected outputs
- `src/market_researcher_crew/crew.py` — tools, logic, agent-task wiring
- `src/market_researcher_crew/main.py` — input variables

---

## ▶️ Running the Project

```bash
crewai run
```

### Other commands

| Command | Description |
|---|---|
| `crewai run` | Run the full 5-agent pipeline |
| `crewai test -n 3 -m gpt-4o` | Test crew over 3 iterations |
| `crewai train -n 5 -f training.json` | Train the crew |
| `crewai replay -t <task_id>` | Replay from a specific task |
| `crewai log-tasks-outputs` | View latest task outputs |
| `crewai reset-memories -a` | Clear all agent memories |

---

## 🗂️ Project Structure

```
market_researcher_crew/
├── src/market_researcher_crew/
│   ├── config/
│   │   ├── agents.yaml          # Agent definitions
│   │   └── tasks.yaml           # Task definitions
│   ├── tools/
│   │   └── custom_tool.py       # Custom tool implementations
│   ├── crew.py                  # Crew orchestration
│   └── main.py                  # Entry point & inputs
├── knowledge/
│   └── user_preference.txt      # User context for agents
├── .env                         # API keys (git-ignored)
├── .gitignore
├── pyproject.toml
└── uv.lock
```

---

## 🤝 Support

- 📖 [crewAI Documentation](https://docs.crewai.com)
- 💬 [Join the Discord](https://discord.com/invite/X4JWnZnxPb)
- 🐛 [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- 🔍 [Groq Console](https://console.groq.com) — manage your API keys and usage
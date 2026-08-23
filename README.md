# Sovereign-Agent-Swarm 🧠🤝🤖

### Adaptive Human-Agent Teaming (HAT) & Smart Company (SmC) Infrastructure

This repository implements a **Human-Model-Free adaptive agent architecture**. Instead of relying on rigid, computationally expensive human behavioral models, the system leverages real-time trajectory analysis and the **Cross-Entropy Method (CEM)** to dynamically adapt agent policies. This guarantees resilient Human-Agent Teaming (HAT) even under noisy, volatile, or sub-optimal human behavior.

---

### 🚀 Architectural Highlights

* **Human-Model-Free Inference:** Uses a sliding window over human actions to infer intent and select the optimal complementary agent policy in real time ($< 50\text{ ms}$).
* **Cross-Entropy Metric (CEM):** Computes log-likelihood over human trajectories against a pre-trained policy library for implicit intent recognition without communication overhead.
* **Smart Company (SmC) AOEA:** Implements Agent-Oriented Enterprise Architecture using specialized FIPA-compliant nodes:
* **MAA (Member Advisor Agent):** Manages local unit resources and autonomous contract negotiations.
* **GAA (Group Advisor Agent):** Coordinates global supply chains and cross-agent ontology mapping.


* **Zero-Friction Adaptation:** Mitigates reward hacking and gracefully accommodates human cognitive shifts during complex collaborative tasks (e.g., Team Space Fortress benchmarks).

---

### 🧮 Mathematical Engine (CEM)

The inference engine evaluates the Cross-Entropy similarity for a human trajectory $\tau$ over a sliding window $T$ against a policy library $\pi_L$:

$$\text{CEM}(\pi_L, \tau) = \frac{1}{T} \sum_{t=1}^{T} \log P(a_t \mid s_t, \pi_L)$$

Once the implicit human policy $C$ is identified, the Meta-Arbiter transitions the AI agent to the optimal complementary policy $D$ using a pre-computed **Self-Play Performance Matrix**.

---

### 🛠 Quick Start

```bash
# Clone the repository
git clone https://github.com/Sega757/Sovereign-Agent-Swarm.git
cd Sovereign-Agent-Swarm

# Install dependencies
pip install -r requirements.txt

# Run the adaptive inference simulation
python -m core.inference_engine

```

---

### 📂 Repository Structure

```text
Sovereign-Agent-Swarm/
├── README.md                  # Project overview and documentation
├── requirements.txt           # Project dependencies
├── docs/
│   └── whitepaper.md          # Technical whitepaper on HAT & Smart Company
└── core/
    ├── __init__.py
    ├── inference_engine.py    # CEM-based dynamic adaptation engine
    └── smart_company.py       # MAA & GAA multi-agent coordination logic

```

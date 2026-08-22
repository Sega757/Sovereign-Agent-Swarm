# Sovereign-Agent-Swarm 🧠🤝🤖

**Adaptive Human-Agent Teaming (HAT) & Smart Company (SmC) Infrastructure**

This repository implements a **Human-Model-Free** adaptive agent architecture. Instead of relying on rigid, computationally expensive human behavioral models, the system utilizes real-time trajectory analysis and the **Cross-Entropy Method (CEM)** to dynamically switch agent policies. This ensures seamless Human-Agent Teaming (HAT) even when human actors exhibit noisy, volatile, or sub-optimal behavior.

## 🚀 Architectural Highlights

*   **Human-Model-Free Inference:** Uses a sliding window of human actions to identify the optimal complementary agent policy in real-time ($< 50\text{ ms}$).
*   **Cross-Entropy Metric (CEM):** Calculates the logarithmic likelihood of human trajectories against a pre-trained Policy Library to identify intent without explicit communication.
*   **Smart Company (SmC) AOEA:** Implements Agent-Oriented Enterprise Architecture via specialized FIPA-compliant nodes:
    *   **MAA (Member Advisor Agent):** Manages local unit resources and contract negotiations.
    *   **GAA (Group Advisor Agent):** Coordinates global supply chains and cross-agent ontology mapping.
*   **Zero-Friction Adaptation:** Prevents "Reward Hacking" and gracefully handles human cognitive shifts during complex missions (e.g., Team Space Fortress benchmarks).

## 🧮 Mathematical Engine (CEM)

The inference engine calculates the Cross-Entropy similarity for a human trajectory $\tau$ over a sliding window against a library of policies:

$$ CEM(\pi_L, \tau) = \frac{1}{T} \sum_{t=1}^{T} \log P(a_t | s_t, \pi_L) $$

Once the human's implicit policy $C$ is identified, the Meta-Arbiter instantly switches the AI to the optimal complementary policy $D$ using a pre-computed Self-Play Performance Matrix.

## 🛠 Quick Start

```bash
git clone [https://github.com/YourUser/Sovereign-Agent-Swarm.git](https://github.com/YourUser/Sovereign-Agent-Swarm.git)
cd Sovereign-Agent-Swarm
pip install -r requirements.txt

# Run the adaptive inference simulation
python -m core.inference_engine

Sovereign-Agent-Swarm/
├── README.md                  # Витрина проекта
├── requirements.txt           # Зависимости
├── docs/
│   └── whitepaper.md          # Твой полный текст про HAT и Smart Company
└── core/
    ├── __init__.py
    ├── inference_engine.py    # Движок CEM (Cross-Entropy Method) для адаптации
    └── smart_company.py       # Логика MAA и GAA агентов
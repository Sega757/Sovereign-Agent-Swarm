import numpy as np
import time
from typing import List, Dict

class CrossEntropyInferenceEngine:
    """
    Движок бессмодельного инференса (Human-Model-Free).
    Анализирует траекторию действий человека через скользящее окно
    и подбирает комплементарную политику ИИ.
    """
    def __init__(self):
        # Библиотека известных политик (стилей поведения человека)
        self.policy_library = ["Aggressive_Bait", "Cautious_Bait", "Erratic_Novice"]
        
        # Матрица комплементарности (Self-play Performance Table)
        # Какая стратегия ИИ лучше всего подходит под стиль человека
        self.complementary_map = {
            "Aggressive_Bait": "Defensive_Shooter_AI",
            "Cautious_Bait": "Aggressive_Shooter_AI",
            "Erratic_Novice": "Mirror_Shooter_AI" # Зеркальная подстраховка для новичков
        }

    def calculate_cem_similarity(self, human_trajectory: List[float], window_size: int = 150) -> str:
        """
        Имитация расчета кросс-энтропии (CEM).
        На практике здесь вычисляется логарифмическое правдоподобие действий.
        """
        # Берем последние кадры (скользящее окно)
        recent_actions = human_trajectory[-window_size:] if len(human_trajectory) > window_size else human_trajectory
        
        # Эмуляция математического вывода: 
        # Если дисперсия действий высокая -> человек новичок/хаотичен
        variance = np.var(recent_actions)
        mean_action = np.mean(recent_actions)

        if variance > 0.8:
            return "Erratic_Novice"
        elif mean_action > 0.6:
            return "Aggressive_Bait"
        else:
            return "Cautious_Bait"

    def adapt_agent_policy(self, human_trajectory: List[float]) -> Dict[str, str]:
        """Полный цикл: Оценка -> Идентификация -> Переключение политики"""
        start_time = time.perf_counter()
        
        # 1. Инференс намерений человека
        identified_human_style = self.calculate_cem_similarity(human_trajectory)
        
        # 2. Подбор комплементарной стратегии ИИ
        target_ai_policy = self.complementary_map.get(identified_human_style, "Safe_Fallback_AI")
        
        latency_ms = (time.perf_counter() - start_time) * 1000

        return {
            "human_inferred_style": identified_human_style,
            "ai_complementary_policy": target_ai_policy,
            "inference_latency_ms": round(latency_ms, 4)
        }

if __name__ == "__main__":
    engine = CrossEntropyInferenceEngine()
    
    # Симулируем траекторию человека (например, очень агрессивные действия)
    dummy_human_trajectory = np.random.normal(0.8, 0.1, 200).tolist()
    
    print("[*] Адаптивный модуль HAT (Human-Agent Teaming) запущен...")
    result = engine.adapt_agent_policy(dummy_human_trajectory)
    
    print(f" -> Распознанный стиль человека: {result['human_inferred_style']}")
    print(f" -> Активирована роль ИИ: {result['ai_complementary_policy']}")
    print(f" -> Задержка переключения (Latency): {result['inference_latency_ms']} ms")
4. core/smart_company.py (Архитектура MAA и GAA)
Этот код показывает структуру «Умной компании» (AOEA), где агенты распределяют ресурсы.

Python
class MemberAdvisorAgent:
    """Агент-советник участника (MAA). Отвечает за локальные ресурсы."""
    def __init__(self, node_id: str, resources: int):
        self.node_id = node_id
        self.resources = resources

    def propose_contract(self, requested_resources: int) -> bool:
        if self.resources >= requested_resources:
            self.resources -= requested_resources
            return True
        return False

class GroupAdvisorAgent:
    """Групповой агент-советник (GAA). Координирует коалиции MAA."""
    def __init__(self):
        self.members = []

    def register_member(self, maa: MemberAdvisorAgent):
        self.members.append(maa)
        print(f"[GAA] Зарегистрирован новый узел: {maa.node_id}")

    def execute_mission(self, total_required_resources: int):
        print(f"[GAA] Запрос на выполнение миссии. Требуется ресурсов: {total_required_resources}")
        allocated = 0
        for member in self.members:
            if allocated >= total_required_resources:
                break
            # Простой Contract Net Protocol (CNP)
            if member.propose_contract(10):
                allocated += 10
                print(f" -> Узел {member.node_id} выделил 10 единиц.")
        
        if allocated >= total_required_resources:
            print("[GAA] Миссия успешно обеспечена ресурсами коалиции.")
        else:
            print("[GAA] Отказ: недостаточно ресурсов в Smart Company.")

if __name__ == "__main__":
    gaa = GroupAdvisorAgent()
    gaa.register_member(MemberAdvisorAgent("Node_Alpha", 50))
    gaa.register_member(MemberAdvisorAgent("Node_Beta", 20))
    
    print("\n--- Запуск распределения ресурсов ---")
    gaa.execute_mission(60)
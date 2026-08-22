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
import world as w
import if_fz as fz
import random as rd
import rwmx as rw
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

is_bj = os.path.join(BASE_DIR, "背景.txt")
is_name = os.path.join(BASE_DIR, "characters")
is_name_list = ["阿格莱雅","阿那克萨戈拉斯","丹恒","海列屈拉","卡厄斯兰那","刻律德菈","迈德漠斯","赛法利娅","缇里西庇俄丝","昔涟","瑕蝶","雅辛忒丝","长月夜","长老院","来古士","民众"]
character_data = {}
agent = {}
# 全局可选行为
ACTIONS_REGISTRY = {
    # ================= 核心剧情 / 主线 =================
    "探索奥赫玛废墟": lambda w: {"anomaly": 5, "data_integrity": -0.02},
    "与黄金裔交谈": lambda w: {**({"memory": True} if w.internal else {}), "anomaly": 3},
    "研究黑潮的源头": lambda w: {"anomaly": 10, **({"black_tide_triggered": True} if w.anomaly > 50 else {})},
    "尝试打破轮回": lambda w: {"internal": True, "anomaly": 20, "data_integrity": -0.05},
    "守护民众": lambda w: {"data_integrity": 0.2, "anomaly": -10},
    "寻找权杖的线索": lambda w: {"memory": True, "anomaly": 8},
    "向天外发出信号": lambda w: {**({"external": True} if not w.external else {}), "anomaly": 15},
    "重启世界引擎": lambda w: {"data_integrity": 0.4, "anomaly": 10, "internal": True},

    # ================= 探索 / 资源 / 生存 =================
    "修复古代终端": lambda w: {"data_integrity": 0.05, "anomaly": -2},
    "净化污染区": lambda w: {"anomaly": -10, "data_integrity": -0.03},
    "安抚恐慌的难民": lambda w: {"data_integrity": 0.08, "anomaly": -3},
    "收集黑潮样本": lambda w: {"anomaly": 7, **({"data_integrity": 0.02} if w.external else {})},
    "搜刮废弃补给站": lambda w: {"data_integrity": 0.04, "anomaly": 2},
    "建立临时避难所": lambda w: {"data_integrity": 0.1, "anomaly": -1, **({"data_integrity": -0.05} if w.anomaly > 80 else {})},

    # ================= 战斗 / 冲突 / 高风险 =================
    "审问黑潮信徒": lambda w: {"memory": True, "anomaly": 6, **({"data_integrity": -0.05} if w.data_integrity < 0.5 else {})},
    "潜入深渊实验室": lambda w: {"anomaly": 12, "memory": True, **({"black_tide_triggered": True} if w.anomaly > 70 else {})},
    "摧毁异常信标": lambda w: {"anomaly": -15, "data_integrity": -0.04},
    "拦截黑潮先锋": lambda w: {"anomaly": -8, "data_integrity": -0.06, **({"data_integrity": 0.02} if w.memory else {})},
    "引爆能量核心": lambda w: {"anomaly": 30, "data_integrity": -0.15, "black_tide_triggered": True},

    # ================= 科研 / 技术 / 解谜 =================
    "破解加密日志": lambda w: {"memory": True, "data_integrity": -0.01},
    "启动防御矩阵": lambda w: {"data_integrity": 0.15, "anomaly": 5},
    "追踪时空裂缝": lambda w: {"anomaly": 18, "memory": True, **({"external": True} if w.internal else {})},
    "校准重力发生器": lambda w: {"anomaly": -4, "data_integrity": 0.03},
    "逆向解析黑潮代码": lambda w: {"memory": True, "anomaly": 12, **({"internal": True} if w.data_integrity > 0.8 else {})},

    # ================= 精神 / 内省 / 特殊 =================
    "与AI核心辩论": lambda w: {"internal": True, "anomaly": 8, **({"data_integrity": 0.05} if w.memory else {})},
    "进入休眠舱冥想": lambda w: {"internal": True, "anomaly": -5, "data_integrity": 0.03},
    "直视深渊之眼": lambda w: {"anomaly": 25, "internal": True, "data_integrity": -0.1, **({"memory": True} if w.anomaly < 20 else {})},
    "献祭自身数据": lambda w: {"data_integrity": -0.2, "anomaly": -30, "memory": True, "black_tide_triggered": False},

    # ================= 势力 / 阵营博弈 =================
    "贿赂黑市商人": lambda w: {"data_integrity": -0.05, "anomaly": 2, **({"memory": True} if w.data_integrity > 0.6 else {})},
    "加入机械飞升教派": lambda w: {"internal": True, "anomaly": 12, "data_integrity": -0.08},
    "向反抗军提供情报": lambda w: {"data_integrity": 0.1, "anomaly": -6, "memory": True},
    "暗杀教派领袖": lambda w: {"anomaly": 20, "data_integrity": -0.12, "black_tide_triggered": True},

    # ================= 深度探索 / 遗迹 =================
    "潜入遗忘之海": lambda w: {"anomaly": 15, **({"external": True} if w.memory else {"data_integrity": -0.05})},
    "唤醒沉睡的旧神": lambda w: {"anomaly": 35, "data_integrity": -0.2, "black_tide_triggered": True},
    "破解创世者遗书": lambda w: {"memory": True, "internal": True, "data_integrity": 0.05},
    "穿越镜像迷宫": lambda w: {"anomaly": 10, **({"internal": True} if w.anomaly > 40 else {})},

    # ================= 极端生存 / 献祭 =================
    "吞噬黑潮结晶": lambda w: {"anomaly": 12, "data_integrity": -0.08, "memory": True},
    "燃烧记忆换取力量": lambda w: {"anomaly": -10, "data_integrity": -0.25, "memory": False},
    "启动自毁协议": lambda w: {"data_integrity": -0.4, "anomaly": -100, "black_tide_triggered": False},
    "与深渊意志交易": lambda w: {"external": True, **({"memory": True} if w.data_integrity < 0.3 else {"data_integrity": -0.1})},

    # ================= 时空 / 悖论操作 =================
    "篡改过去的自己": lambda w: {"internal": True, "anomaly": 30, "data_integrity": -0.15},
    "观测平行宇宙": lambda w: {"anomaly": 18, "memory": True, "external": True},
    "重置局部时间线": lambda w: {"anomaly": -15, "data_integrity": 0.1, "memory": False},
    "锚定当前现实": lambda w: {"data_integrity": 0.15, "anomaly": -10, "internal": False},

    # ================= 日常 / 休闲 =================
    "在酒馆听吟游诗人": lambda w: {"data_integrity": 0.05, "anomaly": -2},
    "修理同伴的机械臂": lambda w: {"data_integrity": 0.08, "anomaly": 1},
    "仰望人造星空": lambda w: {"internal": True, "anomaly": -3},
    "记录今日见闻": lambda w: {"memory": True, "data_integrity": 0.02},
    "星神诞生的时刻": lambda w: {"memory": True, "anomaly": 8},
}
GLOBAL_ACTIONS = list(ACTIONS_REGISTRY.keys())
# game_controller.py
import world as w
import if_fz as fz
import random as rd
import rwmx as rw
import os

class GameController:
    def __init__(self, callback=None):
        self.world = w.World()
        self.callback = callback  # 每轮结束后调用的回调函数，接收状态字符串
        self.ended = False

        # 加载角色（同原 main.py）
        self.agent = {}
        is_name_list = ["阿格莱雅","阿那克萨戈拉斯","丹恒","海列屈拉","卡厄斯兰那","刻律德菈","迈德漠斯","赛法利娅","缇里西庇俄丝","昔涟","瑕蝶","雅辛忒丝","长月夜","长老院","来古士","民众"]
        character_data = {}
        for dirpath, dirnames, filenames in os.walk("黄金裔"):
            for filename in filenames:
                name = os.path.splitext(filename)[0]
                matched = next((n for n in is_name_list if n == name or name.startswith(n)), None)
                if matched:
                    with open(os.path.join(dirpath, filename), "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        character_data.setdefault(matched, []).append(content)
        with open("背景.txt", "r", encoding="utf-8") as f:
            global_background = f.read().strip()
        for name, contents in character_data.items():
            prompt = global_background + "\n\n" + "\n\n".join(contents)
            # 这里会用到 rwmx，我们稍后改造它
            self.agent[name] = rw.Rw(name=name, prompt=prompt)

        # 故事节点列表（同原 main.py）
        self.all_story_nodes = [
            fz.track, fz.tramd,
            fz.internal_1, fz.internal_2, fz.internal_3, fz.internal_4, fz.internal_5,
            fz.tide_1, fz.tide_2, fz.tide_3, fz.tide_4, fz.tide_5,
            fz.data_1, fz.data_2, fz.data_3, fz.data_4, fz.data_5,
            fz.external_1, fz.external_2, fz.external_3, fz.external_4, fz.external_5,
            fz.external_6, fz.external_7, fz.external_8, fz.external_9, fz.external_10,
            fz.internal_6, fz.internal_7, fz.internal_8, fz.internal_9, fz.internal_10,
            fz.tide_6, fz.tide_7, fz.tide_8, fz.tide_9, fz.tide_10,
            fz.data_6, fz.data_7, fz.data_8, fz.data_9, fz.data_10,
            fz.main_1, fz.main_2, fz.main_3, fz.main_4, fz.main_5,
            fz.main_6, fz.main_7, fz.main_8, fz.main_9, fz.main_10, fz.main_30, fz.custom_event
        ]

        # 动作注册表（原 ACTIONS_REGISTRY）
        self.actions_registry = {
            # ... 将原 ACTIONS_REGISTRY 完整复制过来（太长，略）
        }
        self.global_actions = list(self.actions_registry.keys())

    def get_active_agents(self):
        # 同原 main.py 中的函数，此处直接复制
        golden_ones = [...]
        constants = [...]
        candidates = []
        for name in golden_ones:
            if name in self.agent: candidates.append(name)
        for name in constants:
            if name in self.agent: candidates.append(name)
        if self.world.external:
            if "长夜月" in self.agent: candidates.append("长夜月")
            if "丹恒" in self.agent: candidates.append("丹恒")
        if not candidates: return []
        return [rd.choice(candidates)]

    def step(self):
        """执行一轮游戏，返回本轮摘要字符串，若结束则返回 None"""
        if self.ended:
            return None

        self.world.round += 1
        self.world.data_integrity = min(1.0, self.world.data_integrity + 0.01)
        self.world.anomaly = max(0, self.world.anomaly - 1)

        log_lines = []
        log_lines.append(f"--- 第 {self.world.round} 轮 ---")
        log_lines.append(f"异常: {self.world.anomaly} | 数据: {self.world.data_integrity:.2f} | 内部: {self.world.internal} | 外部: {self.world.external} | 黑潮: {self.world.black_tide_triggered} | 记忆: {self.world.memory}")

        # 角色行动
        active = self.get_active_agents()
        if active:
            log_lines.append("【角色行动阶段】")
        for name in active:
            rw_agent = self.agent[name]
            # 调用 rw_agent 的 think_and_act，返回行动索引
            choice = rw_agent.think_and_act(self.world, self.global_actions)
            chosen_action = self.global_actions[choice - 1]
            effect = self.actions_registry[chosen_action](self.world)
            if effect:
                log_lines.append(f"  {name} 行动: {chosen_action}")
                self.world.apply_effect(effect)
            else:
                log_lines.append(f"  {name} 行动: {chosen_action}（无实质影响）")

        # 故事触发
        rd.shuffle(self.all_story_nodes)
        triggered = False
        for node in self.all_story_nodes:
            if node.can_trigger(self.world):
                log_lines.append(f"【事件触发】{node.name}")
                log_lines.append(f"【事件描述】{node.story_text}")
                self.world.triggered_nodes.add(node.name)
                self.world.apply_effect(node.effects)
                self.world.is_game_over_run()
                triggered = True
                break
        if not triggered:
            log_lines.append("【事件】风平浪静的一轮。")

        # 检查是否结束
        if self.world.ended:
            self.ended = True
            log_lines.append("\n=== 游戏结束 ===")
            log_lines.append(f"结局原因: {self.world.end_reason}")

        # 调用回调（如果有）
        full_log = "\n".join(log_lines)
        if self.callback:
            self.callback(full_log, self.ended)
        return full_log
    
with open(is_bj, "r", encoding="utf-8") as f:
    global_background = f.read().strip()

for  dirpath, dirnames, filenames in os.walk(is_name):
    for filename in filenames:
        is_names = os.path.splitext(filename)[0]        # 获取文件名
        matched_name = None
        for name in is_name_list:       # 匹配文件名
            if is_names == name or is_names.startswith(name):       # 匹配文件名
                matched_name = name     # 匹配成功
                break

        if matched_name:       # 匹配成功
            full_path = os.path.join(dirpath, filename)     # 获取文件路径
            with open (full_path, "r", encoding="utf-8") as f:      # 读取文件
                is_nr = f.read().strip()
                if matched_name not in character_data:       # 匹配成功
                    character_data[matched_name] = []       # 创建字典
                character_data[matched_name].append(is_nr)      # 添加数据
                print(f"已加载 {matched_name} 的数据。")     
        
for name,contents in character_data.items():
    is_prompt = global_background + "\n\n" + "\n\n".join(contents)
    agent[name] = rw.Rw(name=name, prompt=is_prompt)
    print(f"已创建 {name} 的角色。")
def run_game():
    my_world = w.World()
    print("=== 轮回开始 ===")

    all_story_nodes = [
    fz.track, fz.tramd,
    fz.internal_1, fz.internal_2, fz.internal_3, fz.internal_4, fz.internal_5,
    fz.tide_1, fz.tide_2, fz.tide_3, fz.tide_4, fz.tide_5,
    fz.data_1, fz.data_2, fz.data_3, fz.data_4, fz.data_5,
    fz.external_1, fz.external_2, fz.external_3, fz.external_4, fz.external_5,
    fz.external_6, fz.external_7, fz.external_8, fz.external_9, fz.external_10,
    fz.internal_6, fz.internal_7, fz.internal_8, fz.internal_9, fz.internal_10,
    fz.tide_6, fz.tide_7, fz.tide_8, fz.tide_9, fz.tide_10,
    fz.data_6, fz.data_7, fz.data_8, fz.data_9, fz.data_10,
    fz.main_1, fz.main_2, fz.main_3, fz.main_4, fz.main_5,
    fz.main_6, fz.main_7, fz.main_8, fz.main_9, fz.main_10,fz.main_30
    ,fz.custom_event
]  # 包含所有节点

    # 决定每轮参与行动的角色
    def get_active_agents(world):
    # 黄金裔列表（共10位，来自 is_name_list）
        golden_ones = [
            "阿格莱雅", "阿那克萨戈拉斯", "卡厄斯兰那", "刻律德菈","海列屈拉",
            "迈德漠斯", "赛法利娅", "缇里西庇俄丝", "昔涟", "瑕蝶", "雅辛忒丝"
        ]
        # 无条件常驻角色
        constants = ["来古士", "长老院", "民众"]
        
        candidates = []
        # 加入黄金裔（只加载了的）
        for name in golden_ones:
            if name in agent:
                candidates.append(name)
        # 加入常驻
        for name in constants:
            if name in agent:
                candidates.append(name)
        # 若外部接触（列车到达），加入丹恒
        if world.external:
            if "长夜月" in agent:
                candidates.append("长夜月")
            if "丹恒" in agent:
                candidates.append("丹恒")
    
        # 如果没有任何候选（理论上不会），返回空
        if not candidates:
            return []
        
        # 随机选择一个角色
        chosen = rd.choice(candidates)
        return [chosen]

    while not my_world.ended:
        print(f"状态 | 异常: {my_world.anomaly} | 数据: {my_world.data_integrity:.2f} | 内部: {my_world.internal} | 外部: {my_world.external} | 黑潮: {my_world.black_tide_triggered} | 记忆: {my_world.memory}")
        my_world.round += 1
        print(f"\n--- 第 {my_world.round} 轮 ---")
        my_world.data_integrity = min(1.0, my_world.data_integrity + 0.01)
        my_world.anomaly = max(0, my_world.anomaly - 1)

        # ---- 角色行动阶段 ----
        active_agents = get_active_agents(my_world)
        if active_agents:
            print("【角色行动阶段】")
        for name in active_agents:
            rw_agent = agent[name]
            # 让角色思考并选择一个行动
            choice = rw_agent.think_and_act(my_world, GLOBAL_ACTIONS)
            chosen_action = GLOBAL_ACTIONS[choice - 1]
            # 根据选择的行动产生效果（这里需要映射行动到效果，可以自定义）
            action_effect = ACTIONS_REGISTRY[chosen_action](my_world)
            if action_effect:
                print(f"  {name} 行动: {chosen_action}")
                my_world.apply_effect(action_effect)
            else:
                print(f"  {name} 行动: {chosen_action}（无实质影响）")

        # ---- 故事节点触发阶段 ----
        rd.shuffle(all_story_nodes)
        triggered = False
        for node in all_story_nodes:
            if node.can_trigger(my_world):
                print(f"【事件触发】{node.name}")
                print(f"【事件描述】{node.story_text}")
                my_world.triggered_nodes.add(node.name)  
                my_world.apply_effect(node.effects)
                my_world.is_game_over_run()
                triggered = True
                break
        if not triggered:
            print("【事件】风平浪静的一轮。")

    print("\n=== 游戏结束 ===")
    print(f"结局原因: {my_world.end_reason}")

if __name__ == "__main__":
    run_game()
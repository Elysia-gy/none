# main_kivy.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from game_controller import GameController

class GameUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # 日志显示区域（可滚动）
        self.log_label = Label(
            text="点击「下一轮」开始游戏",
            size_hint_y=None,
            halign='left', 
            valign='top',
            font_name='Roboto',          
            font_size='14sp',              # 调整字号
            text_size=(380, None)          # 【解决换行】：窗口宽400，留出边距，遇到380像素自动换行
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        
        scroll = ScrollView(size_hint=(1, 0.9))
        scroll.add_widget(self.log_label)
        self.add_widget(scroll)

        # 按钮区域
        btn_layout = BoxLayout(size_hint=(1, 0.1))
        # 【解决按钮乱码】：按钮继承 Label 属性，加 font_name 确保按钮文字显示中文
        self.next_btn = Button(text="下一轮", font_name='msyh.ttc')
        self.next_btn.bind(on_press=self.on_next)
        btn_layout.add_widget(self.next_btn)
        self.add_widget(btn_layout)

        self.controller = None
        self.running = False
        self.start_game()

    def start_game(self):
        def init():
            self.controller = GameController(callback=self.update_log)
            Clock.schedule_once(lambda dt: setattr(self.next_btn, 'disabled', False), 0)
        threading.Thread(target=init, daemon=True).start()
        self.next_btn.disabled = True
        self.log_label.text = "正在加载游戏数据..."

    def on_next(self, instance):
        if self.controller and not self.controller.ended:
            threading.Thread(target=self.controller.step, daemon=True).start()
            instance.disabled = True

    def update_log(self, text, ended):
        def upd(dt):
            self.log_label.text += "\n" + text
            # 自动滚动到底部
            scroll = self.log_label.parent
            scroll.scroll_y = 0
            # 恢复按钮状态
            if not ended:
                self.next_btn.disabled = False
            else:
                self.next_btn.disabled = True
                self.next_btn.text = "游戏结束"  # 因为设置了字体，这里也不会乱码了
        Clock.schedule_once(upd, 0)

class OmphalosApp(App):
    def build(self):
        Window.size = (400, 700)
        return GameUI()

if __name__ == "__main__":
    OmphalosApp().run()
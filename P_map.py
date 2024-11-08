from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('Apartment_Hallway.png')
        self.original_width = 639  # 원본 이미지 크기
        self.original_height = 360
        self.window_left = 0  # 스크롤 위치
        self.window_width = 800  # 화면 크기
        self.window_height = 600

    def set_center_object(self, boy):
        self.center_object = boy

    def update(self):
        if self.center_object:
            boy = self.center_object
            if boy.x > 400 and self.window_left + self.window_width < self.original_width:
                self.window_left = min(boy.x - 400, self.original_width - self.window_width)
            elif boy.x < 400 and self.window_left > 0:
                self.window_left = max(boy.x - 400, 0)

    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, 0,
            self.original_width, self.original_height,
            0, 0, self.window_width, self.window_height  # 화면 크기로 확대
        )

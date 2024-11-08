from pico2d import *
from P_state_machine import StateMachine, right_down, left_down, right_up, left_up, down_down, up_down, space_down, landed

class Boy:
    def __init__(self):
        self.x, self.y = 400, 240
        self.frame = 0
        self.image = load_image('Character_Zero_c.png')
        self.scale = 0.5  # 크기 축소 비율
        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions({
            Idle: {right_down: Run, left_down: Run, down_down: Crouch, space_down: Jump},
            Run: {right_up: Idle, left_up: Idle, space_down: Jump},
            Crouch: {up_down: Idle},
            Jump: {landed: Idle}
        })

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()

# 상태 클래스 정의
class Idle:
    frame_count = 10  # Idle 상태는 10 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Idle.frame_count  # Idle 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 70, 900, 70, 70,  # Idle 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )


class Run:
    frame_count = 10  # Run 상태는 10 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Run.frame_count  # Run 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 600, 100, 100,  # Run 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )

class Crouch:
    frame_count = 4  # Crouch 상태는 4 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Crouch.frame_count  # Crouch 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 400, 100, 100,  # Crouch 스프라이트 위치 (행을 조정하세요)
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )


class Walk:
    frame_count = 8  # Walk 상태는 8 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Walk.frame_count  # Walk 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 500, 100, 100,  # Walk 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )


class Jump:
    frame_count = 4  # Jump 상태는 4 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Jump.frame_count  # Jump 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 300, 100, 100,  # Jump 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )


class Fall:
    frame_count = 4  # Fall 상태는 4 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Fall.frame_count  # Fall 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 200, 100, 100,  # Fall 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )


class Attack:
    frame_count = 7  # Attack 상태는 7 프레임

    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % Attack.frame_count  # Attack 애니메이션

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(
            boy.frame * 100, 100, 100, 100,  # Attack 스프라이트 위치
            boy.x, boy.y, 100 * boy.scale, 100 * boy.scale
        )

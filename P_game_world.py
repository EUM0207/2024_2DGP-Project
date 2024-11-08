world = [[], []]  # 레이어 구조: [0: 배경, 1: 캐릭터 및 오브젝트]

def add_object(o, depth):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for obj in layer:
            obj.update()

def render():
    for layer in world:
        for obj in layer:
            obj.draw()

def clear():
    for layer in world:
        layer.clear()

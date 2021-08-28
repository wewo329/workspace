from random import *

class Unit:
    def __init__(self, name, hp, speed, damage=0):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(name))
        # self.damage = damage
        # print("{} 유닛이 생성".format(self.name))
        # print("체력 : {}, 공격력 : {}".format(self.hp, self.damage))
    
    def move(self, location):
        # print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 : {}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 유닛이 파괴되었습니다.".format(self.name))
            del self

    def profile(self):
        print("{} : [남은 체력 : {}] [공격력 : {}] [이동 속도 : {}]".format(self.name, self.hp, self.damage, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed, damage)

    def attack(self, location):
        print("{} : {} 방향으로 공격합니다 [공격력 : {}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. [체력 10 감소] [남은 체력 : {}]".format(self.name, self.hp))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다. [남은 체력 : {}]".format(self.name, self.hp))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            self.damage *= 2
            self.seize_mode = True
        else:
            self.damage /= 2
            self.sieze_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 : {}]".format(name, location, self.flying_speed))

class FlyAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
            # Unit.__init__(valkyrie, name, hp)
                # valkyrie.name = name
                # valkyrie.hp = hp
            # valkyrie.damage = damage
            # print("{} : 유닛이 생성되었습니다.\n".format(self.name))
        Flyable.__init__(self, flying_speed)
            # valkyrie.flying_speed = flying_speed

    def move(self, location):
        # print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyAttackUnit):
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocking = False

    def set_clocking(self):
        if self.clocking == False:
            print("{} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocking = True
        else:
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocking = False

def game_start():
        print("새로운 게임을 시작합니다.")

def game_over():
        print("Player1 : gg")
        print("[Player1] 님이 퇴장하셨습니다.")

if __name__ == "__main__":

    # 게임 시작
    game_start()

    # 유닛 생성
    m1 = Marine()
    m2 = Marine()
    m3 = Marine()
    m4 = Marine()

    t1 = Tank()
    t2 = Tank()

    w1 = Wraith()

    # 유닛 일괄 처리
    Units = []
    Units.append(m1)
    Units.append(m2)
    Units.append(m3)
    Units.append(m4)
    Units.append(t1)
    Units.append(t2)
    Units.append(w1)

    # 유닛 일괄 이동
    for unit in Units:
        unit.move("2시")

    # 탱크 시즈 모드 개발
    Tank.seize_developed = True
    print(Tank.seize_developed)
    print("[알림] 탱크 시즈 모드 개발이 되었습니다.")

    # 전군 공격 준비
    # 탱크는 시즈모드, 레이스는 클로킹 모드, 마린은 스팀팩 모드
    for unit in Units:
        if isinstance(unit, Marine):
            unit.stimpack()
        elif isinstance(unit, Tank):
            unit.set_seize_mode()
        elif isinstance(unit, Wraith):
            unit.set_clocking()

    # 전군 일괄 공격 시작
    for unit in Units:
        unit.attack("10시")

    # 공격 받음
    for i in range(1, 4):
        for unit in Units:
            unit.damaged(randint(5, 21))
    
    # 게임 종료
    game_over()
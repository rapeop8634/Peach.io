class Item():
    """Building off of"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n====\n{}nValue:".format(self.name,self.description, self.value)

class Crown(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Crown",
                         description="Peach lost her crown, looks like you found it!",
                         value=self.amt)
        
class Assistance(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

        def __str__(self):
            return "{}\n====\n{}nValue: {}\nDamage: {}".format(self.name, self.description, self. value, self.damage)

class Toad(Assistance):
    def __init__(self):
        super().__init__(name="Toad",
                         description="Toad is Peach's right hand man, he'd do anything for her.",
                         value=2,
                         damage=2)

class Luigi(Assistance):
    def __init__(self):
        super().__init__(name="Luigi",
                         description="Luigi is Mario's inept brother, he can help a little.",
                         value=2,
                         damage=5)

class Mario(Assistance):
    def __init__(self):
        super().__init__(name="Mario",
                         description="Peach's lover he will surely help her.",
                         value=10,
                         damage=10)

class Yoshi(Assistance):
    def __init__(self):
        super().__init__(name="Yoshi",
                         description="Mario's dino, can help a little.",
                         value=1,
                         damage=1)

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

class Bowser(Enemy):
    def __init__(self):
        super().__init__(name="Bowser", health=50, damage=45)

class KoopaTroopa(Enemy):
    def __init__(self):
        super().__init__(name="Koopa Troopa", health=10, damage=7)

class MiniBowser(Enemy):
    def __init__(self):
        super().__init__(name="Mini Bowser", health=20, damage=105) 
            
class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def intro_text(self):
    raise NotImplementedError()

def modify_player(self,player):
    raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        Welcome to Peachio! Peach has been caught by Bowser once again, she is trapped in a room in the castle! 
        Peach is tired of waiting for Mario to save her, and has decided to take things into her own hands.
        Proceed through the halls of the castle with the assistance of friends to defeat Bowser, Koopa Troopa, and Mini Bowser!
        Let's Begin!
        """
    def modify_player(self,player):
        #Room has no action on player
        pass

class CrownRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self,player):
        player.inventory.append(self.item)
        def modify_player(self, player):
            self.add_loot(player)

class AssistanceRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_assistance(self,player):
        player.inventory.append(self.item)
        def modify_player(self, player):
            self.assistance(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.health = the_player.health - self.enemy.damage
            print("Enemy does {} damage. You have {} Health remaining, be careful and get assistance if needed!".format(self.enemy.damage, the_player.health))

class EmptyHallway(MapTile):
    def intro_text(self):
        return """
        Empty hallways, keep on trying to escape.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class BowsersFortress(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Enemy.Bowser())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Bowser has been awaiting you, he won't let you escape, you are to be his queen.
            """
        else:
            return """
            Bowser has passed out, quick retreat and make your escape.
            """

class KoopaTroopaRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Enemy.KoopaTroopa())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The whole crew is lying in wait for you, they're all taunting you, surrounding them. Try your best to defeat them!
            """
        else:
            return """
            They're all are napping now.
            """
class MiniBowserRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Enemy.MiniBowser())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You turn the corner and see the spitting image of Bowser standing in front of you. Quick get him!
            """
        else:
            return """
            He's out for now...
            """
        
class ToadRoom(AssistanceRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Assistance.Toad())

    def intro_text(self):
        return """
        You see your bff Toad! Enlist him to help you in your quest to escape!
        """

class LuigiRoom(AssistanceRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Assistance.Luigi())

    def intro_text(self):
        return """
        You see your hot lover's brother, Luigi. You don't think he can help very much.
        But go ahead and bring him along, maybe he can help.
        """    

class YoshiRoom(AssistanceRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Assistance.Yoshi())

    def intro_text(self):
        return """
        Mario's dino is here....but where is Mario?! Grab Yoshi just in case he can help!
        """

class MarioRoom(AssistanceRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Assistance.Mario())

    def intro_text(self):
        return """
        Your pipe welding lover, at last, a sight for sore eyes he is. Since Women run the world,
        grab your lover just in case you need to order him around to defeat Bowser and his crew.
        """

world = {}
starting_position = (0, 0)

def load_tiles():
    """Brings the Map Layout together with the MapTiles definitions."""
    with open('U:\Shared\GIS\StuData\RAPEOP8634\Python\PythonProject\Castle.txt', 'r') as f:
        rows = f.readlines()
        x_max = len(rows[0].split('\t'))
        for y in range(len(rows)):
            cols = rows[y].split('\t')
            for x in range(x_max):
                if title_name == 'StartingRoom':
                    global starting_position
                    starting_position = (x, y)
                _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
                
def tile_exists(x, y):
    return _world.get((x, y))

class Player():
    def __init__(self):
        self.inventory = [item.Crown(30), item.Assistance()]
        self.health = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.health > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

def move(self, dx, dy):
    self.location_x += dx
    self.location_y += dy
    print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
def move_north(self):
    self.move(dx=0, dy=-1)
 
def move_south(self):
    self.move(dx=0, dy=1)
 
def move_east(self):
    self.move(dx=1, dy=0)
 
def move_west(self):
    self.move(dx=-1, dy=0)

def attack(self, enemy):
    best_weapon = None
    max_dmg = 0
    for i in self.inventory:
        if isinstance(i, item.Assistance):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
 
    print("You get assistance from {} against {}!".format(best_weapon.name, enemy.name))
    enemy.health -= best_weapon.damage
    if not enemy.is_alive():
        print("You defeated {} temperorily, quick escape!".format(enemy.name))
    else:
        print("{}'s health is at {}, get him to 0 for defeat.".format(enemy.name, enemy.health))

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveUp(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move Peach up', hotkey='w')
 
 
class MoveDown(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move Peach down', hotkey='s')
 
 
class MoveRight(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move Peach right', hotkey='d')
 
 
class MoveLeft(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move Peach left', hotkey='a')
 
 
class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View Peachs inventory', hotkey='i')
        
class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

def adjacent_moves(self):
    """Returns all move actions for adjacent tiles."""
    moves = []
    if world.tile_exists(self.x + 1, self.y):
        moves.append(actions.MoveRight())
    if world.tile_exists(self.x - 1, self.y):
        moves.append(actions.MoveLeft())
    if world.tile_exists(self.x, self.y - 1):
        moves.append(actions.MoveUp())
    if world.tile_exists(self.x, self.y + 1):
        moves.append(actions.MoveDown())
    return moves
 
def available_actions(self):
    """Returns all of the available actions in this room."""
    moves = self.adjacent_moves()
    moves.append(actions.ViewInventory())
 
    return moves

def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)

class Player:
    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

class Run(Action):
    def __init__(self, tile):
        super().__init__(method=Player.run, name="Run away!", hotkey='r', tile=tile)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
 
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Run(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class LeaveCastle(MapTile):
    def intro_text(self):
        return """
        Peach has finally escaped the evil Bowser, with the help of her friends of course!
        Congrats Peach on being independent and not needing Mario to help you!
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True

def play():
    world.load_tiles()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("Choose what to make Peach do next:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                
if __name__ == "__main__":
    play()
       

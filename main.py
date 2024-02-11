from collections import namedtuple

from entitas import entity, Context, Matcher

Position = namedtuple('Position', 'x y')
Health = namedtuple('Health', 'value')
Movable = namedtuple('Movable', '')



context = Context()
def move(entity, new_comp):
    print("move")
context.get_group(Matcher(Position)).on_entity_added += move

entity = context.create_entity()
entity.add(Position, 3, 7)
entity.add(Health, 100)

entities = context.entities
for e in entities:
    print(e)

en = context.get_group(Matcher(Position)).entities
print(en)

entity.add(Movable)



from ycappuccino.core.model.decorators import Item,  Property, Reference, ItemReference, Empty
from ycappuccino.core.model.model import Model

@Empty()
def empty():
    _empty = Member()
    _empty.id("test")
    _empty.name("yaiba")
    _empty.role("test")
    _empty.band("yblues")
    return _empty

@Item(collection="members",plural="members",name="member", secureWrite=True, app="yblues")
@ItemReference(field="_band", item="band")
class Member(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._band = None
        self._name = None
        self._role = None

    @Property(name="name")
    def name(self, a_value):
        self._name = a_value

    @Property(name="role")
    def role(self, a_value):
        self._role = a_value

    @Reference(name="band")
    def band(self, a_value):
        self._band = a_value

empty()
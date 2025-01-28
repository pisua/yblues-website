from ycappuccino.core.model.decorators import Item, Property, Reference, ItemReference, Empty
from ycappuccino.core.model.model import Model

@Empty()
def empty():
    _empty = Lyrics()
    _empty.id("45_reasons")
    _empty.music("45 reasons")
    _empty.lyrics("test")
    return _empty

@Item(collection="lyrics",plural="lyrics", name="lyric", secureWrite=True, app="yblues")
@ItemReference(field="_music", item="music")
class Lyrics(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._music = None
        self._lyrics = None

    @Reference(name="music")
    def music(self, a_value):
        self._music = a_value

    @Property(name="lyrics")
    def lyrics(self, a_value):
        self._lyrics = a_value

empty()
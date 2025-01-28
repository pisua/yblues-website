from ycappuccino.core.model.decorators import Item, Property, Reference, ItemReference, Empty
from ycappuccino.core.model.model import Model

@Empty()
def empty():
    _empty = Music()
    _empty.id("test")
    _empty.name("test")
    _empty.author("author")
    _empty.composer("test")
    _empty.album("test")
    _empty.arrangment("toto,tata,tutu")
    _empty.feat("ben")
    _empty.album("opus")
    return _empty


@Item(collection="musics",plural="musics",name="music", secureWrite=True, app="yblues")
@ItemReference(field="_album", item="album")
class Music(Model):
    """ bean that represent a music of an album(or not) """
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._name = None
        self._author = None
        self._composer = None
        self._album = None
        self._arrangment = None
        self._feat = None
        self._album_properties = None

    @Property(name="name")
    def name(self, a_value):
        self._name = a_value

    @Property(name="author")
    def author(self, a_value):
        self._author = a_value

    @Property(name="composer")
    def composer(self, a_value):
        self._composer = a_value

    @Property(name="arrangment")
    def arrangment(self, a_value):
        self._arrangment = a_value

    @Property(name="feat")
    def feat(self, a_value):
        self._feat = a_value

    @Reference(name="album")
    def album(self, a_value, a_properties=None):
        self._album = a_value
        self._album_properties = a_properties

empty()
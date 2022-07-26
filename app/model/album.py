from ycappuccino.core.model.decorators import Item, Property, Reference, ItemReference
from ycappuccino.core.model.model import Model
import datetime, time

_empty = None
def empty():
    _empty = Album()
    _empty.id("test")
    _empty.name("test")
    _empty.band("test")
    _empty.producer("test")
    _empty.cover("test")
    _empty.release_date("01/12/2020")
    _empty.label("test")


@Item(collection="albums",plural="albums",name="album", secureWrite=True, app="yblues")
@ItemReference(field="_band", item="band")
class Album(Model):
    """ bean that represent an album """
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._name = None
        self._producer = None
        self._cover = None
        self._release_stamp = None
        self._label = None
        self._band = None

    @Property(name="name")
    def name(self, a_value):
        """ name of the opus """
        self._name = a_value

    @Reference(name="band")
    def band(self, a_value):
        """ id of the ref band if exists  """
        self._band = a_value

    @Property(name="producer")
    def producer(self, a_value):
        """ productors of the opus"""
        self._producer = a_value

    @Property(name="cover")
    def cover(self, a_value):
        """ url thunb image of cover"""
        self._cover = a_value

    @Property(name="release_stamp")
    def release_stamp(self, a_value):
        """ stamp of the release date"""
        self._release_stamp = a_value

    def release_date(self, a_value):
        """ stamp of the release date with format by default %d/%m/%Y (01/12/2020)"""
        self.release_stamp(time.mktime(datetime.datetime.strptime(a_value, "%d/%m/%Y").timetuple()))

    @Property(name="label")
    def label(self, a_value):
        """ label if exists """
        self._label = a_value

empty()
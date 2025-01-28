from ycappuccino.core.model.decorators import Item, Property, Empty
from ycappuccino.core.model.model import Model

from datetime import datetime

@Empty()
def empty():
    _empty = Gig()
    _empty.id("test")
    _empty.name("test")
    _empty.address("test")
    _empty.city("test")
    _empty.place("test")
    _empty.date("20/01/2020")
    _empty.stamp("20/01/2020")
    _empty.bands("yblues, test")
    return _empty

@Item(collection="gigs",plural="gigs",name="gig", secureWrite=True, app="yblues")
class Gig(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._name = None
        self._address = None
        self._city = None
        self._stamp = None
        self._place = None
        self._date = None
        self._bands = None


    @Property(name="name")
    def name(self, a_value):
        self._name = a_value
        
    @Property(name="address")
    def address(self, a_value):
        self._address = a_value

    @Property(name="city")
    def city(self, a_value):
        self._city = a_value

    @Property(name="stamp", private=True)
    def stamp(self, a_value):
        self._stamp = a_value

    @Property(name="place")
    def place(self, a_value):
        self._place = a_value

    @Property(name="date")
    def date(self, a_value):
        self._date = a_value
        self.stamp(datetime.strptime(self._date,'%d/%m/%Y').timestamp())

    @Property(name="bands")
    def bands(self, a_value):
        self._bands = a_value

empty()

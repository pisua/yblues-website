from ycappuccino.core.model.decorators import Item, Property, Reference, ItemReference
from ycappuccino.core.model.model import Model

@Item(collection="videos", plural="videos",name="video", secureWrite=True, app="yblues")
@ItemReference(field="_music", item="music")
class Video(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._name = None
        self._music = None
        self._url = None

    @Property(name="name")
    def name(self, a_value):
        self._name = a_value

    @Property(name="url")
    def url(self, a_value):
        self._url = a_value

    @Reference(name="music")
    def music(self, a_value):
        self._music = a_value

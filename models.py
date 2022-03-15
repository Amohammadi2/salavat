from neomodel import (DateProperty, StringProperty, IntegerProperty, StructuredNode, RelationshipFrom, RelationshipTo)

class Contributor(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    salavats = RelationshipTo('SalavatCollection', 'HAS_SENT')

class SalavatCollection(StructuredNode):
    number = IntegerProperty(required=True)
    date_contributed = DateProperty(required=True)
    contributor = RelationshipFrom(Contributor, 'HAS_SENT')
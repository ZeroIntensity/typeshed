from braintree.address import Address as Address
from braintree.resource import Resource as Resource

class MetaCheckoutCard(Resource):
    def __init__(self, gateway, attributes) -> None: ...
    @property
    def expiration_date(self): ...
    @property
    def masked_number(self): ...
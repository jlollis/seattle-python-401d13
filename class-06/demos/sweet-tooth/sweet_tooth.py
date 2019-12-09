class SweetTooth:
    def __init__(self, sweets=[]):
        self.sweets = sweets or ['snickers','gelato','raisinettes']


    def feed(self, ingestible):
        if ingestible not in self.sweets:
            raise NotSweetError('Sweets only!!!')

        # val = 1/0

        return True


class NotSweetError(ValueError):
    pass

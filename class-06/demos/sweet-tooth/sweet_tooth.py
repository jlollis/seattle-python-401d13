
class SweetTooth:
    def __init__(self):
        self.sweets = ['snickers','gelato','raisinettes']

    def feed(self, ingestible):
        if ingestible not in self.sweets:
            raise NotSweetError('Sweets only!')

        # do other stuff
        2/0 # breaking on purpose

        return True


class NotSweetError(ValueError):
    pass

if __name__ == "__main__":
    st = SweetTooth()

    try:
        st.feed('celery')
    except NotSweetError as nse: # good way
        print('I tried to feed healthy!')
        print(nse)
    except:
        print('uh ohs')


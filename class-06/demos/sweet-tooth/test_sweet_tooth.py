import pytest
from sweet_tooth import SweetTooth, NotSweetError

def test_good_sweet():
    st = SweetTooth()
    expected = True
    actual = st.feed('snickers')


def test_bad_sweet():
    st = SweetTooth()

    with pytest.raises(NotSweetError, match='Sweets only!'):
        st.feed('celery')



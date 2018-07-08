import pytest
import time

from catinabox import catactivities


def test__cat_nap__satisfying_nap(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    catactivities.cat_nap(360)
    mock_sleep.assert_called_with(360)


def test__cat_nap__not_satisfying(mocker):
    mock_sleep = mocker.patch.object(time, "sleep", autospec=True)
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(10)
    assert mock_sleep.call_count = 0

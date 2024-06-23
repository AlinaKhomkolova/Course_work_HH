from unittest.mock import MagicMock, patch
import pytest
from requests.models import Response

from src.classes.HhAPI import HhAPI
from src.classes.Vacancy import Vacancy


@pytest.fixture()
def mock_requests_get():
    mock_response = MagicMock(spec=Response)
    mock_response.raise_for_status.return_value = None
    mock_get = MagicMock(return_value=mock_response)

    return mock_get


def test_fetch_vacancies(mock_requests_get):
    hh_api = HhAPI()
    count_page = 1

    vacancies = hh_api.fetch_vacancies(count_page)

    assert isinstance(vacancies, list)
    assert len(vacancies) == 10

    vacancy = vacancies[0]
    assert isinstance(vacancy, Vacancy)


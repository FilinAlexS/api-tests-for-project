import pytest
from data.params import params_for_fail_v1, params_for_fail_v2


@pytest.mark.xfail
@pytest.mark.parametrize('url, params', params_for_fail_v1,
                         ids=['api_v1_without_token', 'api_v1_404', 'api_v1_country_instead_of_airport',
                              'api_v1_invalid_date', 'api_v1_invalid_name_airport', 'api_v1_invalid_currency'])
def test_fail_api_v1(travel_api_v1, url, params):
    """Имитация разных ошибок для API v1 и проверка на статус-код 200"""
    response = travel_api_v1.get_api_fail(url=url, params=params)
    travel_api_v1.check_status_code(response)


@pytest.mark.xfail
@pytest.mark.parametrize('url, params', params_for_fail_v2,
                         ids=['api_v2_without_token', 'api_v2_404', 'api_v2_country_instead_of_airport',
                              'api_v2_invalid_date', 'api_v2_invalid_name_airport', 'api_v2_invalid_currency'])
def test_fail_api_v2(travel_api_v2, url, params):
    """Имитация разных ошибок для API v2 и проверка на статус-код 200"""
    response = travel_api_v2.get_api_fail(url=url, params=params)
    travel_api_v2.check_status_code(response)

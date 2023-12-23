import pytest
from data.schemas import schema_cheap, schema_calendar, schema_monthly, schema_city
from data.params import params_for_cheap_and_direct, params_for_calendar, params_for_monthly, params_for_city


@pytest.mark.parametrize('params', params_for_cheap_and_direct,
                         ids=["no_return_date", "no_air_service", "all_destination", "currency_usd"])
def test_cheap(travel_api_v1, params):
    """Возвращает самые дешевые билеты без пересадок, а также билеты с 1 или 2 пересадками по
       выбранному маршруту с фильтрами дат отправления/возврата."""
    response = travel_api_v1.get_api('prices/cheap', params=params)
    travel_api_v1.check_status_code(response)
    travel_api_v1.validate_schema(response, schema_cheap)


@pytest.mark.parametrize('params', params_for_cheap_and_direct,
                         ids=["no_return_date", "no_air_service", "all_destination", "currency_usd"])
def test_direct(travel_api_v1, params):
    """Возвращает самые дешевые прямые билеты по выбранному маршруту с фильтрами дат отправления/возврата."""
    response = travel_api_v1.get_api('prices/direct', params=params)
    travel_api_v1.check_status_code(response)
    travel_api_v1.validate_schema(response, schema_cheap)


@pytest.mark.parametrize('params', params_for_calendar,
                         ids=["sort_departure_date", "with_length(travel_time)", "sort_return_date", "currency_rub"])
def test_calendar(travel_api_v1, params):
    """Возвращает самые дешевые прямые рейсы, рейсы с одной или двумя пересадками по выбранному маршруту для каждого дня выбранного месяца."""
    response = travel_api_v1.get_api('prices/calendar', params=params)
    travel_api_v1.check_status_code(response)
    travel_api_v1.validate_schema(response, schema_calendar)


@pytest.mark.parametrize('params', params_for_monthly,
                         ids=["MOW_to_BCN_rub", "LON_to_AYT_usd"])
def test_monthly(travel_api_v1, params):
    """Возвращает самые дешевые билеты без пересадок, а также билеты с 1 или 2 остановками по выбранному маршруту, сгруппированные по месяцам."""
    response = travel_api_v1.get_api('prices/monthly', params=params)
    travel_api_v1.check_status_code(response)
    travel_api_v1.validate_schema(response, schema_monthly)


@pytest.mark.parametrize('params', params_for_city,
                         ids=["MOW_rub", "AYT_usd"])
def test_city_directions(travel_api_v1, params):
    """Возвращает самые популярные направления из указанного города."""
    response = travel_api_v1.get_api('city-directions', params=params)
    travel_api_v1.check_status_code(response)
    travel_api_v1.validate_schema(response, schema_city)

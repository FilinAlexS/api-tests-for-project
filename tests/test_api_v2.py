import pytest
from data.schemas import schema_latest_and_matrix
from data.params import params_for_latest, params_for_month_matrix, params_for_week_matrix


@pytest.mark.parametrize('params', params_for_latest,
                         ids=["all_destination__sort_price", "departure_LED__show_to_affiliates_false",
                              "sorting_route", "one_way_true__beginning_of_period"])
def test_latest(travel_api_v2, params):
    """Возвращает список цен, найденных пользователями за последние 48 часов, в соответствии с использованными фильтрами."""
    response = travel_api_v2.get_api('latest', params=params)
    travel_api_v2.check_status_code(response)
    travel_api_v2.validate_schema(response, schema_latest_and_matrix)


@pytest.mark.parametrize('params', params_for_month_matrix,
                         ids=["without_month", "with_month__show_to_affiliates_false"])
def test_month_matrix(travel_api_v2, params):
    """Возвращает цены за каждый день месяца, сгруппированные по количеству пересадок."""
    response = travel_api_v2.get_api('month-matrix', params=params)
    travel_api_v2.check_status_code(response)
    travel_api_v2.validate_schema(response, schema_latest_and_matrix)


@pytest.mark.parametrize('params', params_for_week_matrix,
                         ids=["with_depart_and_return_date", "with_depart_date", "with_return_date"])
def test_week_matrix(travel_api_v2, params):
    """Возвращает цены на ближайшие даты к целевым."""
    response = travel_api_v2.get_api('week-matrix', params=params)
    travel_api_v2.check_status_code(response)
    travel_api_v2.validate_schema(response, schema_latest_and_matrix)

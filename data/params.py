params_for_cheap_and_direct = [
    {'origin': 'MOW', 'destination': 'HKT', 'depart_date': '2023-12', 'return_date': '', },
    {'origin': 'EWB', 'destination': 'LON', 'depart_date': '2023-12', 'return_date': '2024-01', },
    {'origin': 'MOW', 'destination': '-', 'depart_date': '2023-12', 'return_date': '2024-01', },
    {'origin': 'MOW', 'destination': 'NBE', 'depart_date': '2023-12', 'return_date': '2024-01', "currency": "usd"}
]

params_for_calendar = [
    {"depart_date": "2023-12", "origin": "AYT", "destination": "LON", "calendar_type": "departure_date"},
    {"depart_date": "2023-12", "origin": "AYT", "destination": "LON", "calendar_type": "departure_date",
     "length": "10"},
    {"depart_date": "2023-12", 'return_date': '2024-01', "origin": "AYT", "destination": "LON",
     "calendar_type": "return_date",
     "currency": "rub"},
    {"depart_date": "2024-01", "origin": "MOW", "destination": "AYT", "calendar_type": "departure_date",
     "currency": "usd"}
]

params_for_monthly = [
    {"origin": "MOW", "destination": "BCN", "currency": "rub"},
    {"origin": "LON", "destination": "AYT", "currency": "usd"}
]

params_for_city = [
    {"origin": "MOW", "currency": "rub"},
    {"origin": "AYT", "currency": "usd"}
]

params_for_latest = [
    {"currency": "usd", "period_type": "year", "page": "1", "limit": "30", "show_to_affiliates": "true",
     "sorting": "price", "trip_class": "0"},
    {"origin": "LED", "period_type": "year", "page": "1", "limit": "30", "show_to_affiliates": "false",
     "sorting": "price", "trip_class": "0"},
    {"origin": "MOW", "period_type": "year", "page": "1", "limit": "30", "show_to_affiliates": "true",
     "sorting": "route", "trip_class": "0"},
    {"origin": "AYT", "period_type": "month", "page": "1", "limit": "30", "one_way": "true",
     "beginning_of_period": "2024-02-01", "show_to_affiliates": "true", "sorting": "route", "trip_class": "0"}
]

params_for_month_matrix = [
    {"currency": "usd", "show_to_affiliates": "true", "origin": "LED", "destination": "HKT"},
    {"currency": "rub", "show_to_affiliates": "false", "origin": "MOW", "destination": "HKT", "month": "2024-03-12"}
]

params_for_week_matrix = [
    {"currency": "usd", "origin": "LED", "destination": "MOW", "show_to_affiliates": "true",
     "depart_date": "2023-12-28", "return_date": "2024-01-18"},
    {"origin": "AYT", "destination": "MOW", "show_to_affiliates": "true",
     "depart_date": "2023-12-28"},
    {"currency": "usd", "origin": "OSS", "destination": "MOW", "show_to_affiliates": "true",
     "depart_date": "2023-12-28", "return_date": "2024-01-18"},
]

params_for_fail_v1 = [
    ('city-directions', {"origin": "MOW"}),
    ('city-directions___', {"origin": "MOW"}),
    ('prices/cheap', {'origin': 'MOW', 'destination': 'MNT', 'depart_date': '2023-12', 'return_date': '2024-01-18',
                      'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('prices/cheap', {'origin': 'MOW', 'destination': 'LED', 'depart_date': '2023.12', 'return_date': '2024-01-18',
                      'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('prices/cheap', {'origin': 'M__W', 'destination': 'LED', 'depart_date': '2023-12', 'return_date': '2024-01-18',
                      'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('prices/monthly', {"origin": "MOW", "destination": "BCN", "currency": "v1run",
                        'token': '0bf89475db3bf28f09c630217e711ec2'},),
]

params_for_fail_v2 = [
    ('week-matrix', {"origin": "MOW"}),
    ('week-matrix___', {"origin": "MOW"}),
    ('week-matrix', {"currency": "usd", "origin": "LED", "destination": "MNT", "show_to_affiliates": "true",
                     "depart_date": "2023-12-28", "return_date": "2024-01-18",
                     'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('week-matrix', {"currency": "usd", "origin": "LED", "destination": "MOW", "show_to_affiliates": "true",
                     "depart_date": "2023.12.28", 'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('month-matrix', {"currency": "usd", "show_to_affiliates": "true", "origin": "L__D", "destination": "HKT",
                      'token': '0bf89475db3bf28f09c630217e711ec2'},),
    ('latest', {"currency": "v2run", "period_type": "year", "page": "1", "limit": "30", "show_to_affiliates": "true",
                'token': '0bf89475db3bf28f09c630217e711ec2'},),
]

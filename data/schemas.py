schema_cheap = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "propertyNames": {
                "maxLength": 3,
                "minLength": 3,
                "pattern": "^([A-ZА-Я]*)$"
            },
            "additionalProperties": {"type": "object"},
            "properties": {
                "HTH": {
                    "type": "object",
                    "properties": {
                        "0": {
                            "type": "object",
                            "properties": {
                                "airline": {
                                    "type": "string"
                                },
                                "departure_at": {
                                    "type": "string"
                                },
                                "return_at": {
                                    "type": "string"
                                },
                                "expires_at": {
                                    "type": "string"
                                },
                                "price": {
                                    "type": "integer"
                                },
                                "flight_number": {
                                    "type": "integer"
                                }
                            }
                        }
                    }
                }
            }
        },
        "currency": {
            "type": "string"
        },
        "success": {
            "type": "boolean"
        }
    },
    "required": [
        "data",
        "currency",
        "success"
    ]
}

schema_calendar = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "propertyNames": {
                "maxLength": 10,
                "minLength": 10,
                "pattern": "^((19|20)?[0-9]{2})[-](0?[1-9]|1[012])[-](0?[1-9]|[12][0-9]|3[01])$"
            },
            "additionalProperties": {
                "type": "object"
            },
            "properties": {
                "2024-12-03": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string"
                        },
                        "destination": {
                            "type": "string"
                        },
                        "airline": {
                            "type": "string"
                        },
                        "departure_at": {
                            "type": "string"
                        },
                        "return_at": {
                            "type": "string"
                        },
                        "expires_at": {
                            "type": "string"
                        },
                        "price": {
                            "type": "integer"
                        },
                        "flight_number": {
                            "type": "integer"
                        },
                        "transfers": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "origin",
                        "destination",
                        "airline",
                        "departure_at",
                        "return_at",
                        "expires_at",
                        "price",
                        "flight_number",
                        "transfers"
                    ]
                },
                "currency": {
                    "type": "string"
                },
                "success": {
                    "type": "boolean"
                }
            }
        }
    },
    "required": [
        "data",
        "currency",
        "success"
    ]
}

schema_monthly = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "propertyNames": {
                "maxLength": 7,
                "minLength": 7,
                "pattern": "^((19|20)?[0-9]{2})[-](0?[1-9]|1[012])$"
            },
            "additionalProperties": {
                "type": "object"
            },
            "properties": {
                "2024-12-03": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string"
                        },
                        "destination": {
                            "type": "string"
                        },
                        "airline": {
                            "type": "string"
                        },
                        "departure_at": {
                            "type": "string"
                        },
                        "return_at": {
                            "type": "string"
                        },
                        "expires_at": {
                            "type": "string"
                        },
                        "price": {
                            "type": "integer"
                        },
                        "flight_number": {
                            "type": "integer"
                        },
                        "transfers": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "origin",
                        "destination",
                        "airline",
                        "departure_at",
                        "return_at",
                        "expires_at",
                        "price",
                        "flight_number",
                        "transfers"
                    ]
                },
                "currency": {
                    "type": "string"
                },
                "success": {
                    "type": "boolean"
                }
            }
        }
    },
    "required": [
        "data",
        "currency",
        "success"
    ]
}

schema_city = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "data": {
            "propertyNames": {
                "maxLength": 3,
                "minLength": 3,
                "pattern": "^([A-ZА-Я]*)$"
            },
            "additionalProperties": {
                "type": "object"
            },
            "properties": {
                "777": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string"
                        },
                        "destination": {
                            "type": "string"
                        },
                        "airline": {
                            "type": "string"
                        },
                        "departure_at": {
                            "type": "string"
                        },
                        "return_at": {
                            "type": "string"
                        },
                        "expires_at": {
                            "type": "string"
                        },
                        "price": {
                            "type": "integer"
                        },
                        "flight_number": {
                            "type": "integer"
                        },
                        "transfers": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "origin",
                        "destination",
                        "airline",
                        "departure_at",
                        "return_at",
                        "expires_at",
                        "price",
                        "flight_number",
                        "transfers"
                    ]
                },
                "currency": {
                    "type": "string"
                },
                "success": {
                    "type": "boolean"
                }
            }
        }
    },
    "required": [
        "data",
        "currency",
        "success"
    ]
}

schema_latest_and_matrix = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "currency": {
            "type": "string"
        },
        "error": {
            "type": "string"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "depart_date": {
                            "type": "string"
                        },
                        "origin": {
                            "type": "string"
                        },
                        "destination": {
                            "type": "string"
                        },
                        "gate": {
                            "type": "string"
                        },
                        "return_date": {
                            "type": "string"
                        },
                        "found_at": {
                            "type": "string"
                        },
                        "trip_class": {
                            "type": "integer"
                        },
                        "value": {
                            "type": "integer"
                        },
                        "number_of_changes": {
                            "type": "integer"
                        },
                        "duration": {
                            "type": "integer"
                        },
                        "distance": {
                            "type": "integer"
                        },
                        "show_to_affiliates": {
                            "type": "boolean"
                        },
                        "actual": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "depart_date",
                        "origin",
                        "destination",
                        "gate",
                        "return_date",
                        "found_at",
                        "trip_class",
                        "value",
                        "number_of_changes",
                        "duration",
                        "distance",
                        "show_to_affiliates",
                        "actual"
                    ]
                }
            ]
        },
        "success": {
            "type": "boolean"
        }
    },
    "required": [
        "currency",
        "data",
        "success"
    ]
}

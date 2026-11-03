from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'], description=data['description']))

    # Create CarModel instances with the corresponding CarMake instances
    nissan, mercedes, audi, kia, toyota = car_make_instances

    # (name, type, year, car_make)
    # Type values match CarModel.CAR_TYPES ("SEDAN", not "Sedan")
    car_model_data = [
        ("Pathfinder", "SUV", 2023, nissan),
        ("Qashqai", "SUV", 2023, nissan),
        ("XTRAIL", "SUV", 2023, nissan),
        ("A-Class", "SUV", 2023, mercedes),
        ("C-Class", "SUV", 2023, mercedes),
        ("E-Class", "SUV", 2023, mercedes),
        ("A4", "SUV", 2023, audi),
        ("A5", "SUV", 2023, audi),
        ("A6", "SUV", 2023, audi),
        ("Sorrento", "SUV", 2023, kia),
        ("Carnival", "SUV", 2023, kia),
        ("Cerato", "SEDAN", 2023, kia),
        ("Corolla", "SEDAN", 2023, toyota),
        ("Camry", "SEDAN", 2023, toyota),
        ("Kluger", "SUV", 2023, toyota),
        # Add more CarModel instances as needed
    ]

    for name, car_type, year, car_make in car_model_data:
        CarModel.objects.create(name=name, car_make=car_make,
                                type=car_type, year=year)

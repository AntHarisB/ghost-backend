import random
from django.utils import timezone
from django_seed import Seed
from PerformanceTab.models import ProjectInformation

seeder = Seed.seeder()

project_creation_options = ['prodaja', 'partnerstvo', 'preporuka']
type_of_project_options = ['fixed', 'on-going']
year_options = [2019, 2020, 2021, 2022, 2023]

seeder.add_entity(ProjectInformation, 15, {
    'project_name': lambda x: f"Projekat {x}",
    'project_value': lambda: round(random.uniform(1000, 1000000), 2),
    'team_size': lambda: random.randint(1, 10),
    'velocity': lambda: random.randint(1, 10),
    'weeks_over_ddl': lambda: random.randint(0, 30),
    'hourly_price': lambda: random.randint(10, 100),
    'year': lambda: random.choice(year_options),
    'lead_closing': lambda: round(random.uniform(4, 20), 2),
    'project_creation': lambda: random.choice(project_creation_options),
    'type_of_project': lambda: random.choice(type_of_project_options),
    'hours_available': lambda: random.randint(100, 1000),
    'hours_billed': lambda: random.randint(50, 1000),
})

inserted_pks = seeder.execute()
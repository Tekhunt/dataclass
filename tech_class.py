from dataclasses import dataclass, field

@dataclass
class Technology:
    name: str
    years_experience: int = 0
    project_url: str = None

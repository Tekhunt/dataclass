from dataclasses import dataclass, field
from tech_class import Technology

@dataclass
class SoftwareEngineer:
    name: str
    skills: list = field(default_factory=list)
    technologies: list = field(default_factory=list)

    def add_technology(self, technology_name: str, years_experience: int = 0, project_url: str = None):
        technology = Technology(technology_name, years_experience, project_url)
        self.technologies.append(technology)

    def get_technologies(self):
        if self.technologies:
            return self.technologies
        return 'No technologies added'

    def add_skills(self,skill):
        self.skills.append(skill)

    def get_skills(self):
        if self.skills:
            return self.skills
        return 'No skills added'

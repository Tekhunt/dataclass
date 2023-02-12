# create instances and call methods

from engr_class import SoftwareEngineer


smith = SoftwareEngineer("Private Smith")
print('Instance of smith =>',smith)
josh = SoftwareEngineer("Toch Josh")
smith.add_technology("Python", 5, "https://github.com/tekhunt/peer-to-peer-payment")
josh.add_technology("Python", 5, "https://github.com/tekhunt/peer-to-peer-payment")
josh.add_skills('leadership')
josh.add_skills('time mgt')
smith.get_technologies()
smith.technologies
print('compare instances =>', josh.technologies == smith.technologies)
print(josh.get_skills())
print(smith.get_technologies())
print('smith object => ', smith)
print('josh object => ', josh)

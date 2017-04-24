people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
# print people

def split_title_and_name(person):
	return person.split(' ')[0] + ' ' + person.split(' ')[-1]

persons = list(map(split_title_and_name, people))
print persons
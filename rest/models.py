import csv


class Student:
    def __init__(self, number, id, place, sleep, sport, experience, effect, hygiene, outside, videogame, gamesay, study,
                 social, nap, cluster, dormitory, password):
        self.number = number
        self.id = id
        self.place = place
        self.sleep = sleep
        self.sport = sport
        self.experience = experience
        self.effect = effect
        self.hygiene = hygiene
        self.outside = outside
        self.videogame = videogame
        self.gamesay = gamesay
        self.study = study
        self.social = social
        self.nap = nap
        self.cluster = cluster
        self.dormitory = dormitory
        self.password = password

    def to_str(self):
        return "-".join([self.place, self.sleep, self.sport,
                         self.experience, self.effect,
                         self.hygiene, self.outside,
                         self.videogame, self.gamesay,
                         self.study, self.social, self.nap])


def student_encoder(p):
    if isinstance(p, Student):
        return vars(p)
    raise TypeError('Object of type Person is not JSON serializable')


def read_csv(filename):
    students = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # skip header row
        for row in reader:
            student = Student(*row)
            students.append(student)
    return students

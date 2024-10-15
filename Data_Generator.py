import random

# Lists
# for Teachers & Students
Female_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
               "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", "Aria", "Scarlett", "Luna",
               "Chloe", "Lily", "Eleanor", "Hazel", "Grace", "Penelope", "Nora", "Riley", "Zoe", "Victoria", "Stella",
               "Lillian", "Aurora", "Lucy", "Anna", "Leah", "Savannah", "Madison", "Ruby", "Natalie", "Audrey",
               "Claire", "Elena", "Maya", "Aaliyah", "Lydia", "Bella", "Violet", "Hannah", "Layla", "Emilia", "Nova",
               "Zara", "Aria", "Gianna", "Jasmine", "Skylar", "Alexa", "Delilah", "Samantha", "Sarah", "Ariana",
               "Gabriella", "Isabelle", "Kayla", "Hailey", "Autumn", "Mackenzie", "Serena", "Harmony", "Julia",
               "Elise", "Daisy", "Adeline", "Catherine", "Valentina", "Nina", "Fiona", "Ivy", "Anna", "Katarzyna",
               "Marta", "Agnieszka", "Magdalena", "Monika", "Joanna", "Aleksandra", "Ewa", "Dorota", "Beata", "Kinga",
               "Malgorzata", "Natalia", "Izabela", "Weronika", "Karolina", "Barbara", "Patrycja", "Justyna", "Julia",
               "Zofia", "Kamila", "Aneta", "Gabriela", "Renata", "Helena", "Emilia", "Oliwia", "Dominika", "Elzbieta",
               "Lucja", "Marcelina", "Ola", "Paulina", "Sylwia", "Jolanta", "Anita", "Alicja", "Klaudia", "Lidia",
               "Hanna", "Daria", "Kornelia", "Nadia", "Roksana", "Monika", "Adrianna", "Malwina", "Aurelia",
               "Penelope", "Naomi", "Lydia", "Vivian", "Miranda", "Hazel", "Autumn", "Paige", "Brooke", "Lila",
               "Summer", "Elise", "Fiona", "Ariel", "Celeste", "Juniper", "Gemma", "Nina", "Sierra", "Dahlia", "Lana",
               "Raven", "Olive", "Esme", "Mira", "Willow", "Simone", "Tessa", "Ivy", "Ayla", "Marina", "Poppy",
               "Callie", "Aurora", "Sage", "Amara", "Rowan", "Thea", "Phoebe", "Daphne", "Cleo", "Sylvia", "Anika",
               "Giselle", "Joelle", "Eloise", "Marina", "Camille", "Brielle", "Alina"]
Male_names = ["Wojciech", "Jan", "Pawel", "Michal", "Mateusz", "Kacper", "Jakub", "Adam", "Piotr", "Szymon", "Tomasz",
             "lukasz", "Damian", "Marek", "Adrian", "Andrzej", "Rafal", "Krzysztof", "Bartosz", "Robert", "Grzegorz",
             "Daniel", "Marcin", "Dominik", "Artur", "Alexander", "William", "James", "John", "Benjamin", "Lucas",
             "Liam", "Ethan", "Noah", "Oliver", "Jacob", "Matthew", "Daniel", "David", "Samuel", "Michael",
             "Christopher", "Gabriel", "Joseph", "Thomas", "Ryan", "Andrew", "Nathan", "Isaac", "Nicholas",
             "Aleksander", "Filip", "Igor", "Oskar", "Patryk", "Przemyslaw", "Radoslaw", "Arkadiusz", "Cezary",
             "Hubert", "Dariusz", "Zygmunt", "Wiktor", "Bogdan", "Henryk", "Waldemar", "Kazimierz", "Ireneusz",
             "Leszek", "Zbigniew", "Alexander", "Max", "Leo", "Henry", "Sebastian", "Julian", "Adam", "Oscar", "Jack",
             "Aiden", "Mason", "Caleb", "Jackson", "Elijah", "Evan", "Connor", "Wyatt", "Zachary", "Carter", "Logan",
             "Eli", "Gavin", "Nathaniel", "Isaiah", "Jonathan", "Ezekiel", "Aaron", "Theodore", "Hugo", "Landon",
             "Cole", "Dominic", "Xavier", "Bryce", "Hunter", "Austin", "Dylan", "Elias", "Colton", "Brody", "Tristan",
             "Seth", "Asher", "Blake", "Tyler", "Nolan", "Jaxon", "Ryder", "Miles", "Roman", "Gage", "Harrison", "Kai",
             "Zane", "Victor", "Patrick", "Joel", "Simon", "Toby", "Evan", "Ian", "Marcus", "Peter", "Finn", "Cameron",
             "Axel", "Louis", "George", "Spencer", "Bruce", "Derek", "Maxwell", "Russell", "Walter", "Edwin", "Barry",
             "Franklin", "Ronald", "Leonardo", "Vincent", "Phillip", "Eduardo", "Hector", "Antonio", "Javier",
             "Giovanni", "Ricardo", "Marco", "Fabio", "Diego", "Fernando", "Pedro", "Manuel", "Joaquin", "Luis",
             "Roberto", "Emilio", "Raul", "Mateo", "Carlos", "Santiago", "Juan", "Ramon", "Pablo", "Enrique", "Andres",
             "Mario", "Hugo", "Adrian", "Rodrigo", "Cesar", "Victor", "Felipe", "Alberto", "Esteban", "Miguel",
             "Rafael", "Jorge", "Ivan", "Alexis", "Sergio", "Armando", "Julio", "Francisco", "Angel", "Omar",
             "Lorenzo", "Dante", "Leon", "Angelo", "Bruno", "Gustavo", "Hugo", "Ignacio", "Jaime", "Javier",
             "Mauricio", "Nicolas", "Oscar", "Raul", "Salvador", "Tomas", "Xavier", "Yahir", "Zacharias", "Amir",
             "Bryant", "Cesar", "Dario", "Erick", "Fernando", "Gilberto", "Hector", "Iker", "Julian", "Kevin", "Luis",
             "Martin", "Nestor", "Orlando", "Pedro", "Quentin", "Ricardo", "Samuel", "Tristan", "Ulises", "Vicente",
             "Walter", "Xander", "Yael", "Zion", "Aaron", "Bryan", "Carlos"]
Surnames = ["Nowak", "Kowalski", "Wisniewski", "Dabrowski", "Lewandowski", "Wojcik", "Kaminski", "Kowalczyk",
           "Zielinski", "Szymanski", "Wozniak", "Kozlowski", "Jankowski", "Mazur", "Wojciechowski", "Kwiatkowski",
           "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Zajac", "Pawlowski", "Michalski", "Nowakowski",
           "Adamczyk", "Duda", "Krol", "Wieczorek", "Jablonski", "Majewski", "Olszewski", "Stepien", "Malinowski",
           "Jaworski", "Wrobel", "Pawlik", "Walczak", "Staszewski", "Baran", "Gorecki", "Rutkowski", "Michalak",
           "Sikora", "Ostrowski", "Baranowski", "Turek", "Rogowski", "Zawadzki", "Serafin", "Tomczak", "Smith",
           "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
           "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark",
           "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez",
           "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts",
           "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Nowak", "Kowalski",
           "Wisniewski", "Dabrowski", "Lewandowski", "Wojcik", "Kaminski", "Kowalczyk", "Zielinski", "Szymanski",
           "Wozniak", "Kozlowski", "Jankowski", "Mazur", "Wojciechowski", "Kwiatkowski", "Krawczyk", "Kaczmarek",
           "Piotrowski", "Grabowski", "Zajac", "Pawlowski", "Michalski", "Nowakowski", "Adamczyk", "Duda", "Krol",
           "Wieczorek", "Jablonski", "Majewski", "Olszewski", "Stepien", "Malinowski", "Jaworski", "Wrobel", "Pawlik",
           "Walczak", "Staszewski", "Baran", "Gorecki", "Rutkowski", "Michalak", "Sikora", "Ostrowski", "Baranowski",
           "Turek", "Rogowski", "Zawadzki", "Serafin", "Tomczak", "Smith", "Johnson", "Williams", "Jones", "Brown",
           "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris",
           "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker",
           "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams",
           "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell",
           "Parker", "Evans", "Edwards", "Collins"]
Cities = ["Sopot", "Gdynia", "Pruszcz Gdanski", "Banino", "Pszczolki", "Juszkowo", "Straszyn"]
Streets = ["Aleja Jana Pawla II", "ulica Nowy swiat", "ulica Marszalkowska", "Plac Zamkowy", "ulica Krakowska",
          "ulica Pulawska", "ulica swietokrzyska", "ulica Pilsudskiego", "ulica Chmielna", "ulica Woloska",
          "ulica Koszykowa", "ulica Wilcza", "ulica swietojanska", "Plac Konstytucji", "ulica Hoza", "ulica Targowa",
          "ulica Foksal", "ulica Nowogrodzka", "ulica Krucza", "ulica Sienkiewicza", "ulica Emilii Plater",
          "ulica Marszalkowska", "ulica Franciszkanska", "ulica Wiejska", "ulica Zlota", "ulica Marszalkowska",
          "ulica Mokotowska", "ulica Nowy swiat", "ulica Miodowa", "ulica Poznanska", "ulica Marszalkowska",
          "ulica Wspolna", "ulica Zgoda", "ulica Wierzbowa", "ulica Nowy swiat", "ulica Warecka", "ulica Piekna",
          "ulica Smolna", "ulica Nowy swiat", "ulica Prozna", "ulica Krucza", "ulica Zamenhofa", "ulica swietokrzyska",
          "ulica Marszalkowska", "ulica Chmielna", "ulica Senatorska", "ulica Dluga", "ulica Nowy swiat",
          "ulica Nowogrodzka", "ulica Hoza", "ulica Wilcza", "ulica swietojanska", "ulica Emilii Plater",
          "ulica Foksal", "ulica Marszalkowska", "ulica Targowa", "ulica Koszykowa", "ulica Sienkiewicza",
          "ulica Krucza", "ulica Nowy swiat", "ulica Marszalkowska", "ulica Pulawska", "ulica Hoza", "ulica Wiejska",
          "ulica Nowogrodzka", "ulica Chmielna", "ulica Piekna", "ulica Marszalkowska", "ulica Zgoda", "ulica Zlota",
          "ulica Krakowskie Przedmiescie", "ulica Dluga", "ulica Nowy swiat", "ulica Senatorska", "ulica Wierzbowa",
          "ulica Hoza", "ulica Nowy swiat", "ulica swietojanska", "ulica Marszalkowska", "ulica Emilii Plater",
          "ulica Pilsudskiego", "ulica Chmielna", "ulica Marszalkowska", "ulica Targowa", "ulica Marszalkowska",
          "ulica Koszykowa", "ulica Hoza", "ulica Nowogrodzka", "ulica Wilcza", "ulica Sienkiewicza",
          "ulica Nowy swiat", "ulica Marszalkowska", "ulica swietojanska", "ulica Chmielna", "ulica Nowy swiat",
          "ulica Targowa", "ulica Piekna", "ulica Marszalkowska", "ulica Wilcza"]
Ed_levels = ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate Degree",
            "Vocational/Technical Training", "Professional Certification"]
methods = ["M", "I", "G"]
Universities = ["University of Warsaw", "Jagiellonian University", "Adam Mickiewicz University in Poznan",
               "University of Wroclaw", "AGH University of Science and Technology", "Warsaw University of Technology",
               "University of Gdansk", "Nicolaus Copernicus University in Torun", "University of lodz",
               "University of Silesia in Katowice", "Poznan University of Technology",
               "Wroclaw University of Science and Technology", "University of Warmia and Mazury in Olsztyn",
               "Lublin University of Technology", "Pomeranian Medical University in Szczecin",
               "Medical University of Warsaw", "University of Opole", "Kazimierz Wielki University in Bydgoszcz",
               "Gdansk University of Technology", "University of Zielona Gora"]
Mails = ["wp.pl", "gmail.com", "onet.pl", "gugu.com"]
polish_middle_schools = [
   "Gimnazjum im. Henryka Sienkiewicza nr 1 w Gdansku",
   "Gimnazjum im. Maria Sklodowska-Curie nr 2 w Gdansku",
   "Gimnazjum im. Tadeusza Kosciuszki nr 3 w Gdansku",
   "Gimnazjum im. Fryderyka Chopina nr 4 w Gdansku",
   "Gimnazjum im. Ignacego Paderewskiego nr 5 w Gdansku",
   "Gimnazjum im. Stanislawa Wyspianskiego nr 6 w Gdansku",
   "Gimnazjum im. Juliusza Slowackiego nr 7 w Gdansku",
   "Gimnazjum im. Leopolda Staffa nr 8 w Gdansku",
   "Gimnazjum im. Czeslawa Milosza nr 9 w Gdansku",
   "Gimnazjum im. Jozefa Pilsudskiego nr 10 w Gdansku",
   "Gimnazjum im. Janusza Korczaka nr 11 w Gdansku",
   "Gimnazjum im. Stanislawa Moniuszki nr 12 w Gdansku",
   "Gimnazjum im. Zofii Nalkowskiej nr 13 w Gdansku",
   "Gimnazjum im. Jana Pawla II nr 14 w Gdansku",
   "Gimnazjum im. Boleslawa Prusa nr 15 w Gdansku",
   "Gimnazjum im. Gabrieli Zapolskiej nr 16 w Gdansku",
   "Gimnazjum im. Juliusza Tuwima nr 17 w Gdansku",
   "Gimnazjum im. Stanislawa Ignacego Witkiewicza nr 18 w Gdansku",
   "Gimnazjum im. Cypriana Kamila Norwida nr 19 w Gdansku",
   "Gimnazjum im. Marii Konopnickiej nr 20 w Gdansku",
   "Gimnazjum im. Kazimierza Przerwy-Tetmajera nr 21 w Gdansku",
   "Gimnazjum im. Jana Brzechwy nr 22 w Gdansku",
   "Gimnazjum im. Mikolaja Kopernika nr 23 w Gdansku",
   "Gimnazjum im. Anity Wlodarczyk nr 24 w Gdansku",
   "Gimnazjum im. Jana Kasprowicza nr 25 w Gdansku",
   "Gimnazjum im. Marii Dabrowskiej nr 26 w Gdansku",
   "Gimnazjum im. Tadeusza Boya-zelenskiego nr 27 w Gdansku",
   "Gimnazjum im. Jozefa Wybickiego nr 28 w Gdansku",
   "Gimnazjum im. Adama Asnyka nr 29 w Gdansku",
   "Gimnazjum im. Boleslawa Lesmiana nr 30 w Gdansku",
   "Gimnazjum im. Wincentego Pola nr 31 w Gdansku",
   "Gimnazjum im. Gabriela Narutowicza nr 32 w Gdansku",
   "Gimnazjum im. Czeslawa Milosza nr 33 w Gdansku",
   "Gimnazjum im. Jana Pawla II nr 34 w Gdansku",
   "Gimnazjum im. Stanislawa Staszica nr 35 w Gdansku",
   "Gimnazjum im. Zbigniewa Herberta nr 36 w Gdansku",
   "Gimnazjum im. Stanislawa Moniuszki nr 37 w Gdansku",
   "Gimnazjum im. Henryka Sienkiewicza nr 38 w Gdansku",
   "Gimnazjum im. Juliusza Slowackiego nr 1 w Gdyni",
   "Gimnazjum im. Jana Pawla II nr 2 w Gdyni",
   "Gimnazjum im. Boleslawa Prusa nr 3 w Gdyni",
   "Gimnazjum im. Gabrieli Zapolskiej nr 4 w Gdyni",
   "Gimnazjum im. Juliusza Tuwima nr 5 w Gdyni",
   "Gimnazjum im. Stanislawa Ignacego Witkiewicza nr 6 w Gdyni",
   "Gimnazjum im. Cypriana Kamila Norwida nr 7 w Gdyni",
   "Gimnazjum im. Marii Konopnickiej nr 8 w Gdyni",
   "Gimnazjum im. Kazimierza Przerwy-Tetmajera nr 1 w Sopocie",
   "Gimnazjum im. Jana Brzechwy nr 2 w Sopocie",
   "Gimnazjum im. Henryka Sienkiewicza nr 3 w Sopocie",
   "Gimnazjum im. Stanislawa Wyspianskiego nr 4 w Sopocie"
]

# for Classes, Courses, Lessons
Profiles = [["Mathematics-Geography-Civics", [0, 2, 4, 6, 10, 12, 18, 22], [1, 2, 4, 6, 10, 19, 20, 23, 26],
            [1, 2, 4, 6, 10, 19, 23, 24, 28, 35]],
           ["Mathematics-Physics-Computer Science", [0, 2, 4, 6, 8, 12, 14, 20], [1, 2, 4, 6, 8, 13, 18, 21],
            [1, 2, 4, 6, 8, 13, 18, 21, 35]],
           ["Literature-History-Civics", [0, 2, 4, 6, 10, 14, 16, 18, 22, 30], [0, 3, 4, 7, 10, 12, 18, 23, 26, 31],
            [0, 3, 4, 7, 10, 12, 18, 23, 27, 31]],
           ["Biology-Chemistry-English", [0, 2, 4, 6, 10, 12, 14, 16, 18, 30], [0, 2, 5, 6, 10, 15, 17, 18, 26],
            [0, 2, 5, 6, 10, 15, 17, 18, 22]],
           ["English-German-Spanish", [0, 2, 4, 6, 8, 10, 18, 22, 14, 26], [0, 2, 5, 6, 9, 11, 18, 20, 30],
            [0, 2, 5, 6, 9, 11, 18, 22]],
           ["Biology-Mathematics-Computer Science-", [0, 2, 4, 6, 8, 12, 14, 16, 20, 22, 34],
            [1, 2, 4, 6, 8, 15, 16, 21, 18, 35], [1, 2, 4, 6, 8, 15, 16, 21, 35]],
           ["Physics-Chemistry-Mathematics", [0, 2, 4, 6, 8, 12, 14, 16, 18, 20], [1, 2, 4, 6, 8, 13, 14, 17, 18, 22],
            [1, 2, 4, 6, 8, 13, 14, 17, 22]],
           ["Business", [0, 2, 4, 8, 14, 16, 18, 22, 24, 28, 32], [0, 2, 5, 6, 8, 18, 20, 22, 25, 27, 29],
            [0, 2, 5, 6, 8, 22, 25, 27, 29, 33]]]
Subjects = ["Mathematics", "Literature", "English", "History", "German", "Spanish", "Physics", "Biology", "Chemistry",
           "Geography", "Computer Science", "Civics", "Accounting", "Negotiations", "Corporate Finance", "Philosophy",
           "MicroEconomy", "Discrete Mathematics"]
classrooms = ["101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115",
             # Floor 1
             "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215",
             # Floor 2
             "301", "302", "303", "304", "305", "306", "307", "308", "309", "310", "311", "312", "313", "314", "315",
             # Floor 3
             "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415"
             # Floor 3
             ]

monthing = [random.randint(1, 20) - 10 for _ in range(10)]

# FUNCTIONS:

# that returns the index of particular profile
def index_of_profile(profiles, name):
   for i in range(len(profiles)):
       if name == profiles[i][0]:
           return i
   return None


# that generates phone number
def generate_number():
   num = ""
   num += str(random.randint(100, 999)) + "-"
   num += str(random.randint(100, 999)) + "-"
   num += str(random.randint(100, 999))
   return num


# that generates Birth Date
def generate_BirthDate(year):
   month = random.randint(1, 12)
   if month == 2:
       day = str(random.randint(1, 28))
   elif month in [4, 6, 9, 11]:
       day = str(random.randint(1, 30))
   else:
       day = str(random.randint(1, 31))
   date = str(year) + "-" + str(month) + "-" + day
   return date


# that generates Address
def generate_Address():
   prob = random.randint(1, 10)
   if prob > 8:
       city = random.choice(Cities)
   else:
       city = "Gdansk"
   Street = random.choice(Streets)
   PostalCode = str(random.randint(10, 99)) + "-" + str(random.randint(100, 999))
   no = random.randint(1, 80)
   result = city + ", " + PostalCode + ", " + Street + " " + str(no)
   return result


# that returns the year at the time when the given course is conducted
def year_lesson(classes, course):
   for clas in classes:
       if clas[0] == course:
           return clas[1]


# that finds a teacher that is already working at the school at the time when the course is conducted
def findTeacher(teachers, year):
   while True:
       teacher = random.choice(teachers)
       if teacher[1] < year:
           return teacher[0]


# Beginning and Ending of the Time Snapshots
beginning = 2014
ending = 2023  # TS2
FirstSnapshot = 2018  # TS1
# ids
cID = 0  # course_ID
sID = 0  # student_ID
lID = 0  # lesson_ID
eID = 0  # exam_id

min_res = 50
max_res = 60
min_att = 20
max_att = 60
min_time = 70
max_time = 120
min_sat = 3
max_sat = 6
change_sat = 0
boundaries = {year: [[0]*8 for _ in range(10)] for year in range(beginning, ending + 1)}

# Set initial values for the first month of the first year
boundaries[beginning][0] = [min_res, max_res, min_time, max_time, min_att, max_att, min_sat, max_sat]

boundaries[beginning][0] = [min_res,max_res,min_time,max_time,min_att,max_att,min_sat, max_sat]
for year in range(beginning, ending+1):
   for month in range(0,10):
       change_res = random.randint(-5,5)
       change_time = random.randint(-8,8)
       change_att = random.randint(-5,6)
       if year == beginning and month == 0:
           continue
       if month == 0:
           change_sat = random.choice([-1,1,2])
           boundaries[year][month][0] = boundaries[year-1][9][0] + change_res
           boundaries[year][month][1] = boundaries[year-1][9][1] + change_res
           boundaries[year][month][2] = boundaries[year-1][9][2] + change_time
           boundaries[year][month][3] = boundaries[year-1][9][3] + change_time
           boundaries[year][month][4] = boundaries[year-1][9][4] + change_att
           boundaries[year][month][5] = boundaries[year-1][9][5] + change_att
           boundaries[year][month][6] = boundaries[year-1][9][6] + change_sat
           boundaries[year][month][7] = boundaries[year-1][9][7] + change_sat
       else:
           boundaries[year][month][0] = boundaries[year][month-1][0] + change_res
           boundaries[year][month][1] = boundaries[year][month-1][1] + change_res
           boundaries[year][month][2] = boundaries[year][month-1][2] + change_time
           boundaries[year][month][3] = boundaries[year][month-1][3] + change_time
           boundaries[year][month][4] = boundaries[year][month-1][4] + change_att
           boundaries[year][month][5] = boundaries[year][month-1][5] + change_att
           boundaries[year][month][6] = boundaries[year][month-1][6] + change_sat
           boundaries[year][month][7] = boundaries[year][month-1][7] + change_sat
           




# monthing = [random.randint(0, 20) - 10 for _ in range(10)]
# yearing = [random.randint(0,5) for _ in range(ending - beginning + 1)]

# Creating Inserts for Subject Table
with open("Subjects.txt", "w") as file:
   for i in range(len(Subjects)):
       row_basic = (str(sID) + "," + Subjects[i] + "," + Subjects[i] + "BasicSyllabus.pdf,Basic")
       file.write(row_basic + "\n")
       sID += 1
       row_expanded = (str(sID) + "," + Subjects[i] + "," + Subjects[i] + "ExpandedSyllabus.pdf,Expanded")
       sID += 1
       file.write(row_expanded + "\n")

# Creating Inserts for Teachers Table (for Database and Excel)
Teachers = []
names=[]
with open("Excel/Sheet2-TS1.csv", "w") as Excel:
   with open("Excel/Sheet2-TS2.csv", "w") as Excel2:
       with open("1TS/TeachersTS1.txt", "w") as fileTeachersTS1:
           with open("2TS/TeachersTS2.txt", "w") as fileTeachersTS2:
               Titles_Sheet2 = "Teacher|Salary|Mail|Phone Number|University|Date Of Employment"
               Excel.write(Titles_Sheet2 + "\n")
               Excel2.write(Titles_Sheet2 + "\n")
               for tID in range(200):
                   gender = random.choice(["Female", "Male"])
                   if gender == "Female":
                       Name = random.choice(Female_names)
                   else:
                       Name = random.choice(Male_names)
                   Surname = random.choice(Surnames)
                   while Name +Surname in names:
                       Surname = random.choice(Surnames)
                   Education_Level = random.choice(Ed_levels)
                   Office_No = random.choice(classrooms)
                   Teaching_method = random.choice(methods)
                   row_teacher = (
                               str(tID) + "," + Name + "," + Surname + "," + gender + "," + Education_Level + "," + str(
                           Office_No) + "," + Teaching_method)
                   # Data about teachers needed for Excel
                   Phone = generate_number()
                   Salary = random.randint(40, 70) * 100
                   Mail = Surname + "." + Name + "@" + random.choice(Mails)
                   University = random.choice(Universities)
                   row_excel = str(tID) + "|" + str(Salary) + "|" + Mail + "|" + Phone + "|" + University + "|"
                   year = random.randint(2005, ending)
                   date = generate_BirthDate(year)
                   if year < FirstSnapshot:
                       fileTeachersTS1.write(row_teacher + "\n")
                       row_excel += date
                       Excel.write(row_excel + "\n")
                   else:
                       fileTeachersTS2.write(row_teacher + "\n")
                       row_excel += date
                       Excel2.write(row_excel + "\n")
                   Teachers.append([tID, year])

# Each node in Classes - [Class_ID, Starting_Year, Number of free places, Profile of Class, [Course_ID, Year_of_Course, []]]
# Creating Inserts for Classes, Courses and Lessons Table
Classes = []
# Node in Classes - [Class_ID, Starting_Year, Free places in class, Profile, [Course_ID,Course_Year,[Lessons...]]]
Students = [[], []]
names_students=[]
# Node in 
with open("2TS/ClassesTS2.txt", "w") as FileClasses2:
   with open("1TS/ClassesTS1.txt", "w") as FileClasses1:
       with open("2TS/CourseTS2.txt", "w") as FileCourse2:
           with open("1TS/CourseTS1.txt", "w") as FileCourse1:
               with open("2TS/LessonsTS2.txt", "w") as FileLessons2:
                   with open("1TS/LessonsTS1.txt", "w") as FileLessons1:
                       # loop in range of (period of database * number of profiles) to create each profile for each year
                       for i in range((ending - beginning + 1) * len(Profiles)):
                           year = i // len(Profiles) + beginning  # Starting year of class
                           profile = Profiles[i % len(Profiles)][0]  # Name of the class's profile
                           row_class = (str(i) + "," + str(year) + "," + profile)
                           enum = 0
                           if year > FirstSnapshot:
                               FileClasses2.write(row_class + "\n")  # Adding line to the "Classes.txt" file
                           else:
                               FileClasses1.write(row_class + "\n")  # Adding line to the "Classes.txt" file
                           Classes.append([i, year, random.randint(25, 35), i % len(Profiles), []])
                           # GENERATING COURSES' ROWS
                           for academic_year in range(3):
                               if year + academic_year > ending:
                                   break
                               for subject in Profiles[i % len(Profiles)][academic_year + 1]:
                                   row_course = str(cID) + "," + str(year + academic_year) + "," + str(i) + "," + str(
                                       findTeacher(Teachers, year + academic_year)) + "," + str(subject)
                                   Classes[i][4].append([cID, year + academic_year, []])
                                   if year + academic_year > FirstSnapshot:
                                       FileCourse2.write(row_course + "\n")
                                   else:
                                       FileCourse1.write(row_course + "\n")
                                   # GENERATING LESSONS' ROWS
                                   for month in range(10):
                                       hours = random.randint(18, 20)
                                       row_lessons = str(lID) + "," + str((month + 8) % 12 + 1) + "," + str(
                                           hours) + "," + random.choice(classrooms) + "," + str(cID)
                                       if year + academic_year > FirstSnapshot:
                                           FileLessons2.write(row_lessons + "\n")
                                       else:
                                           FileLessons1.write(row_lessons + "\n")
                                       Classes[i][4][enum][2].append([lID, hours])
                                       lID += 1
                                   enum += 1
                                   cID += 1

sID = 0  # student_id
# STUDENTS, SATISFACTION, EXAMS, ATTENDANCE
with open("2TS/Students.txt", "w") as FStudents2:
    with open("1TS/StudentsTS1.txt", "w") as FStudents1:
        with open("2TS/SatisfactionTS2.txt", "w") as FSatisfaction2:
            with open("1TS/SatisfactionTS1.txt", "w") as FSatisfaction1:
                with open("2TS/ExamsTS2.txt", "w") as FExams2:
                    with open("1TS/ExamsTS1.txt", "w") as FExams1:
                        with open("2TS/AttendanceTS2.txt", "w") as FAttendance2:
                            with open("1TS/AttendanceTS1.txt", "w") as FAttendance1:
                                while True:
                                    gender = random.choice(["Female", "Male"])
                                    if gender == "Female":
                                        name = random.choice(Female_names)
                                    else:
                                        name = random.choice(Male_names)
                                    surname = random.choice(Surnames)
                                    while name + surname in names_students:
                                        surname = random.choice(Surnames)
                                    names_students.append(name + surname)
                                    to_delete = False
                                    for clas in Classes:
                                        if clas[2] > 0:
                                            klasa = clas
                                            clas[2] -= 1
                                            break
                                        else:
                                            to_delete = True
                                    if to_delete:
                                        Classes.remove(Classes[0])
                                    # calculating birth year of student based on class's starting year
                                    # 20% chance that given student start education year earlier
                                    year = str(klasa[1] - 16 + random.randint(1, 10) // 9)
                                    date = generate_BirthDate(year)
                                    row_students = str(
                                        sID) + "," + name + "," + surname + "," + gender + "," + date + "," + str(
                                        klasa[0])
                                    if klasa[1] > FirstSnapshot:
                                        FStudents2.write(row_students + "\n")
                                        Students[1].append(sID)
                                    else:
                                        FStudents1.write(row_students + "\n")
                                        Students[0].append(sID)

                                    # GENERATING ROWS FOR EXAMS, ATTENDANCE AND SATISFACTION LEVEL
                                    for course in klasa[4]:
                                        sat_lvl = random.randint(boundaries[course[1]][0][6],boundaries[course[1]][0][7])
                                        if sat_lvl > 10:
                                            sat_lvl = 10
                                        if sat_lvl < 0:
                                            sat_lvl = 0
                                        row_satisfaction = str(sID) + "," + str(course[0]) + "," + str(
                                           random.randint(1, 10))
                                        if course[1] > FirstSnapshot:
                                            FSatisfaction2.write(row_satisfaction + "\n")
                                        else:
                                            FSatisfaction1.write(row_satisfaction + "\n")
                                        for months in range(10):
                                            threshold = 9 + months%2
                                            passed = random.randint(1, 10)
                                            if passed < threshold:
                                                result = random.randint(boundaries[course[1]][months][0],boundaries[course[1]][months][1])
                                                time_taken = random.randint(boundaries[course[1]][months][2],boundaries[course[1]][months][3])
                                                if result >100:
                                                    result = 100
                                                if result < 0:
                                                    result = 0
                                                if time_taken > 180:
                                                    time_taken=180
                                                if time_taken < 0:
                                                    time_taken=0
                                            else:
                                                result = random.randint(0, 50)
                                                time_taken = random.randint(0, 180)
                                            if months == 9:
                                                row_exam = str(eID) + ",6," + str(result) + "," + str(
                                                    time_taken) + ",F," + str(sID) + "," + str(course[0])
                                            else:
                                                row_exam = str(eID) + "," + str((months + 8)% 12 + 1) + "," + str(
                                                    result) + "," + str(time_taken) + ",M," + str(sID) + "," + str(
                                                    course[0])
                                            if course[1] > FirstSnapshot:
                                                FExams2.write(row_exam + "\n")
                                            else:
                                                FExams1.write(row_exam + "\n")
                                            eID += 1
                                        for id, lesson in enumerate(course[2]):
                                            # assuming that each student has above 60% attendance rate
                                            hoursAttended = round(random.randint(boundaries[course[1]][id][4],boundaries[course[1]][id][5])*lesson[1] / 100)
                                            row_attendance = str(sID) + "," + str(lesson[0]) + "," + str(hoursAttended)  # +","+str(round(hoursAttended/lesson[1],2))
                                            if course[1] > FirstSnapshot:
                                                FAttendance2.write(row_attendance + "\n")
                                            else:
                                                FAttendance1.write(row_attendance + "\n")

                                    sID += 1
                                    if len(Classes) == 0:
                                        break

# EXCEL SHEET 1
StudentsExcel = [[], []]

with open("Excel/Sheet1-TS1.csv", "w") as Excel:
   with open("Excel/Sheet1-TS2.csv", "w") as Excel2:
       Titles_Sheet = "Student|Address|Previous School|Average Exams|Average Grades|Contact 1|Contact2|Family Status"
       Excel.write(Titles_Sheet + "\n")
       Excel2.write(Titles_Sheet + "\n")
       for i in range(len(Students)):
           for student in Students[i]:
               diff = random.randint(1, 10)
               if diff > 8:
                   status = random.choice(["Separated family", "One parent", "No parents"])
               else:
                   status = "Full family"

               row = str(student) + "|" + generate_Address() + "|" + random.choice(polish_middle_schools) + "|" + str(
                   random.randint(60, 100)) + "|" + str(
                   random.randint(35, 60) / 10) + "|" + generate_number() + "|" + generate_number() + "|" + status
               StudentsExcel[i].append(row.split("|"))
               if i == 0:
                   Excel.write(row + "\n")
               else:
                   Excel2.write(row + "\n")

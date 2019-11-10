import random

capitals = {
   'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

number_of_exams = 5
number_of_questions = 10


for n in range(number_of_exams):

    quizfile = open('capitalsquiz%s.txt' % (n + 1), 'w')
    answefile = open('capitalsquiz_answers%s.txt' % (n + 1), 'w')

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (n + 1))
    quizfile.write('\n\n')
    states = list(capitals.keys())
    cap = list(capitals.items())
    # random.shuffle(states)

    for r in range(number_of_questions):

        # writing question quiz
        answers = random.sample(states, 3)
        right_answer = capitals.get(states[r])
        while right_answer in answers:
            answers = random.sample(states, 3)
        answers.append(right_answer)
        random.shuffle(answers)
        quizfile.write('What is the capital of ' + states[r] + '\n\n')
        for i in range(4):
            quizfile.write(('ABCD'[i])+ ') ' + answers[i] + '\n')
        quizfile.write('\n')

        # writing answer file
        index = answers.index(capitals.get(states[r]))
        answefile.write(str(r + 1) + '. ' + 'ABCD'[index] + '\n')
    quizfile.close()
    answefile.close()



class ResultfForView(object):

    def __init__(self, question, answerID, answerResult, answerRight):
        self.question = question
        self.answerID = answerID
        self.answerResult = answerResult
        self.answerRight = answerRight

class ResultfTestAdmin(object):

    def __init__(self, id_question, question, answer1, answer2, answer3, answer4, answerRight, done ,answerUser):
        self.id_question = id_question
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.answerRight = answerRight
        self.done = done
        self.answerUser=answerUser


class ResultAnswer(object):

    def __init__(self, id_question, question, answerSend):
        self.id_question = id_question
        self.question = question
        self.answerSend = answerSend

class AllTest(object):

    def __init__(self, test, countchange,continuechange):
        self.test = test
        self.countchange = countchange
        self.continuechange=continuechange

class AllResult(object):

    def __init__(self, name, category, idResult1, idResult2, result1, result2):
        self.name = name
        self.category = category
        self.idResult1 = idResult1
        self.idResult2 = idResult2
        self.result1 = result1
        self.result2 = result2

class AllResultCover(object):

    def __init__(self, nameTest, nameCategory, results):
        self.nameTest = nameTest
        self.nameCategory = nameCategory
        self.results = results

class AllResultsUser(object):

    def __init__(self, idRes, result, number):
        self.idRes = idRes
        self.result = result
        self.number = number

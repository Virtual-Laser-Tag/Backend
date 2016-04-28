class User:
    user_dictionary = {}
    def __init__(self, name): # newly-created class instance
        self.name = name
        self.scores = []
        self.score=0
        User.user_dictionary[self.name] = self;
    def score_list(self,score): #store the new score in to user's record
        import datetime
        data = "^"+self.name+"^ "+str(datetime.datetime.now())+": "+str(score)
        self.scores.append(data)
#        f=open('G:\Zhenwei Wu\CS\User information.txt','a')
#        f.write(data+'\n')
        self.score=score
        return score
    def print_all_record(self,number): #print the required number of scores
        result =self.name + "'s " + str(number) +" records:" + '\n'
        if(number > len(self.scores)):
            for x in xrange(len(self.scores)):
                result += self.scores[len(self.scores)-1-x] + '\n'
        else:
            for x in xrange(number):
                result += self.scores[len(self.scores)-1-x] + '\n'
        return result
    def start_again(self):
        self.score=0
    def setpassword(self,password):
        self.password=password
    __setpassword=setpassword #private copy of setpassword method
    @staticmethod
    def winner(): #print the winner of 2 players game
        users = User.user_dictionary.values()
        users = sorted(users, key=lambda user:int(user.score))
        if(len(users) < 1):
            return ""
        return users[-1].name

    @staticmethod
    def get_users():
        users = User.user_dictionary.values()
        users = sorted(users, key=lambda user:int(user.score))
        if(len(users) < 1):
            return ""
        return users;


if __name__ == "__main__":
    sally = User("sally")
    joe = User("joe")
    sally.score_list(100)
    joe.score_list(500)
    print User.winner()
    sally.score_list(999)
    print User.winner()
    joe.score_list(10000)
    print User.winner()

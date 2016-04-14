class User:
    user_dictionary = {}
    def __init__(self, name, password): # newly-created class instance
        self.name = name
        self.__setpassword(password)
        self.scores = []
        self.score=0
        User.user_dictionary[self.name] = self;
    def score_list(self,score): #store the new score in to user's record
        import datetime
        data = "^"+self.name+"^ "+str(datetime.datetime.now())+": "+str(score)
        self.scores.append(data)
        f=open('G:\Zhenwei Wu\CS\User information.txt','a')
        f.write(data+'\n')
        self.score=score
    def print_all_record(self,number): #print the required number of scores
        result =self.name + "'s " + str(number) +" records:" + '\n'
        if(number > len(self.scores)):
            for x in xrange(len(self.scores)):
                result += self.scores[len(self.scores)-1-x] + '\n'
        else:
            for x in xrange(number):
                result += self.scores[len(self.scores)-1-x] + '\n'
        print result
    def start_again(self):
        self.score=0
    def setpassword(self,password):
        self.password=password
    __setpassword=setpassword #private copy of setpassword method
    @staticmethod
    def winner(): #print the winner of 2 players game
        users = User.user_dictionary.values()
        sorted(users, key=lambda user:user.score)
        print users[0].name

   

        
        
    

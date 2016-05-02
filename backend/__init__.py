from User import User
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self,user_name):
        return {'hello': user_name}

    def put(self, user_name):
        x = User(user_name)
        return {"user_name": user_name}

class Score(Resource):
    def get(self,user_name):
        return {'user_name':user_name,
                'score': User.user_dictionary[user_name].score}

    def put(self,user_name):
        new_score = request.form['data']
        if user_name not in User.user_dictionary.keys():
            User(user_name)
        User.user_dictionary[user_name].score_list(new_score)
        return {"user_name": user_name,
                "new_score": new_score}

class UserScored(Resource):
    def post(self, user_name):
        if user_name not in User.user_dictionary.keys():
            User(user_name)
        User.user_dictionary[user_name].score +=10
        return {"user_name": user_name,
                "new_score": User.user_dictionary[user_name].score}

class AllScores(Resource):
    def get(self):
        score_dic = dict()
        for user_name in User.user_dictionary.keys():
            score_dic[x]=User.user_dictionary[user_name].score
        return score_dic

class Winner(Resource):
    def get(self):
        return {'winner_name': User.winner()}

class Results(Resource):
    def get(self):
        ret = {};
        for u in User.get_users():
            ret[u.name] = u.score;
        return ret;


@app.route('/')
def home():
    user_list = User.user_dictionary.values()#sorted(User.user_dictionary.values(), 
                       #key=lambda user:int(user.score),
                      # reverse=True)
    winner = User.winner()
    return render_template('index.html',users=user_list,winner=winner)


api.add_resource(Users, '/user/<string:user_name>')
api.add_resource(UserScored, '/userscored/<string:user_name>')
api.add_resource(Score, '/score/<string:user_name>')
api.add_resource(AllScores, '/allscores')
api.add_resource(Winner, '/winner')
api.add_resource(Results, '/results')


if __name__ == '__main__':
    app.run(debug=True)


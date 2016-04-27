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

class Winner(Resource):
    def get(self):
        return {'winner_name': User.winner()}

@app.route('/')
def home():
    user_list = sorted(User.user_dictionary.values(), 
                       key=lambda user:int(user.score),
                       reverse=True)
    winner = User.winner()
    return render_template('index.html',users=user_list,winner=winner)


api.add_resource(Users, '/user/<string:user_name>')
api.add_resource(Score, '/score/<string:user_name>')
api.add_resource(Winner, '/winner')


if __name__ == '__main__':
    app.run(debug=True)


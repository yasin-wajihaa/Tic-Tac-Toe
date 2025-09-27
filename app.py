from flask import Flask, render_template

app = Flask(__name__)

grid_list = [' '] * 9
first_player = "X"
second_player = "O"
player_turn = first_player

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/start_game/<mode>")
def start_game(mode):
    if mode == "pvp":
        return pvp_game()
 
def pvp_game():
    global grid_list, player_turn
    grid_list = [' '] * 9
    player_turn = first_player
    return render_template("game.html", grid_list=grid_list)


@app.route("/pvp/move/<int:number>")
def player_move(number):
    global player_turn
    grid_list[number] = player_turn
    winner = winner_check()
    if winner:
        return render_template("game.html", message=f"{winner} is the winner!", grid_list=grid_list)
    elif ' ' not in grid_list:
        return render_template("game.html", message="It's a draw!", grid_list=grid_list)
    else:
        player_turn = second_player if player_turn == first_player else first_player
        return render_template("game.html", grid_list=grid_list)


def winner_check():
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for i in win_conditions:
        if grid_list[i[0]] == grid_list[i[1]] == grid_list[i[2]] != ' ':
            return grid_list[i[0]]  
    return False




if __name__ == "__main__" :
    app.run(host="0.0.0.0" , debug=True)


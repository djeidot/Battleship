import requests

baseUrl = "10.44.37.98:9000"


def _url(path):
    return "http://" + baseUrl + "/" + path


class Api:

    @staticmethod
    def startGame(player1, player2):
        body = {"player1": player1, "player2": player2}
        r = requests.post(_url("games/"), json=body)
        return r.json()

    @staticmethod
    def getGames():
        r = requests.get(_url("games/"))
        return r.json()

    @staticmethod
    def getGame(game_id):
        r = requests.get(_url("games/" + game_id + "/"))
        return r.json()

    @staticmethod
    def getPlayerInfo(player):
        r = requests.get(_url("players/" + player))
        if r.status_code == 404:
            return None
        return r.json()

    @staticmethod
    def makeMove(api_id, player, grid_ref):
        body = {"player": player}
        r = requests.put(_url("games/" + api_id + "/" + grid_ref + "/"), json=body)
        return r.json()
    
    @staticmethod
    def deleteGame(game_id):
        r = requests.delete(_url("games/" + game_id + "/"))
        return r.status_code == 204

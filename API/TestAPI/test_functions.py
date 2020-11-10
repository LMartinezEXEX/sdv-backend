import json
import pytest
from main import app
from pony.orm import db_session, select
from Database.database import *
from fastapi.testclient import TestClient

client = TestClient(app)

'''
Global values to keep track cuantity of games and players in DB
'''
total_players = 0
games = 0


@db_session()
def game_factory(players_cuantity: int, turns_cuantity: int,
                 game_state: int = 1, dead_player: bool = False, dead_cuantity: int = 0,
                 fenix_promulgation: int = 0, death_eater_promulgation: int = 0):
    global total_players
    global games

    users = []
    # Create users
    for user in range(players_cuantity):
        user = User(email='usuario{}@gmail.br'.format(total_players),
                    username='User_{}'.format(total_players),
                    password="fachero".encode(),
                    icon="".encode(),
                    creation_date=datetime.datetime.today(),
                    last_access_date=datetime.datetime.today(),
                    is_validated=True)

        users.append(user)
        total_players += 1

    owner = User['usuario{}@gmail.br'.format(total_players - players_cuantity)]

    # Create game and Board
    game = Game(name='test_game_{}'.format(games),
                owner=owner,
                min_players=5,
                max_players=10,
                creation_date=datetime.datetime.today(),
                state=game_state)
    games += 1

    Board(game=game,
          fenix_promulgation=fenix_promulgation,
          death_eater_promulgation=death_eater_promulgation,
          election_counter=0,
          spell_available=False)
    commit()

    game_id = game.id

    players = []
    turn = 1
    # Join players in game
    for user in users:

        is_Fenix = turn % 2 == 0
        player = Player(turn=turn,
                        user=user,
                        rol='Fenix' if is_Fenix else 'Mortifago',
                        loyalty='Fenix' if is_Fenix else 'Mortifago',
                        is_alive=True,
                        chat_enabled=True,
                        is_investigated=False,
                        game_in=game)
        players.append(player)
        turn += 1

    # Kill first 'dead_cuantity' players
    if dead_player:
        player_index = 0
        for _ in range(dead_cuantity):
            player = players[player_index]
            player.is_alive = False
            player_index += 1
    commit()

    for _ in range(turns_cuantity):
        response = client.put('game/{}/select_MM'.format(game_id))

    return [game_id, players[0].id]


def make_vote_and_start_new_turn(
        game_id: int, players_to_vote: int, first_player_id: int, result: bool, dead_count: int = 0):
    # Vote the formula
    for i in range(players_to_vote):
        player_vote(
            game_id=game_id,
            player_id=first_player_id + dead_count + i,
            vote=result)

    client.put('game/{}/result'.format(game_id))

    # Now minister id is game_data[1]+4
    start_new_turn(game_id)


def start_new_turn(game_id):
    return client.put('game/{}/select_MM'.format(game_id))


def get_3_cards(game_id):
    return client.put('/game/{}/get_cards'.format(game_id))


def check_game_state(game_id):
    return client.get('game/{}/check_game'.format(game_id))


def get_director_candidates(game_id):
    return client.get('/game/{}/director_candidates'.format(game_id))


def execute_spell(game_id: int, spell: str, minister_id: int, player_id: int):
    return client.put('/game/{}/execute_spell?spell={}'.format(game_id, spell), json={
        "minister_id": minister_id,
        "player_id": player_id
    }
    )

def player_vote(game_id, player_id, vote):
    return client.put('/game/{}/vote'.format(game_id), json={
        "id": player_id,
        "vote": vote
    }
    )


def minister_promulgate(game_id, minister_id, card_type):
    return client.put('/game/{}/promulgate'.format(game_id), json={
        "candidate_id": minister_id,
        "to_promulgate": card_type
    }
    )


def set_director_candidate(game_id, minister_id, director_id):
    return client.put('/game/{}/select_director_candidate'.format(game_id), json={
        "minister_id": minister_id,
        "director_id": director_id
    }
    )

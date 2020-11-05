from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, EmailStr, ValidationError, validator
from fastapi import Depends, HTTPException
from Database import database
from Database.game_functions import *
from API.Model.gameExceptions import *
from Database.turn_functions import create_first_turn



class GameParams(BaseModel):
    email: EmailStr
    name: str
    min_players: int
    max_players: int


class EmailParameter(BaseModel):
    email: EmailStr


def create_new_game(game_params: GameParams):
    check_create_conditions(user_email=game_params.email, name=game_params.name,
                            min_players=game_params.min_players, max_players=game_params.max_players)
    game_id = save_new_game(owner=game_params.email, name=game_params.name,
                            min_players=game_params.min_players,
                            max_players=game_params.max_players)
    player_id = put_new_player_in_game(user=game_params.email, game_id=game_id)
    return {"Game_Id": game_id, "Player_Id": player_id}


def join_game_with_keys(game_id: int, user_email: EmailStr):
    check_join_conditions(game_id=game_id, user_email=user_email)
    player_id = put_new_player_in_game(user=user_email, game_id=game_id)
    return {"Player_Id": player_id}


def init_game_with_ids(game_id: int, player_id: int):
    check_init_conditions(game_id=game_id, player_id=player_id)
    minister_id = create_first_turn(game_id=game_id)
    return {"Minister_Id": minister_id}
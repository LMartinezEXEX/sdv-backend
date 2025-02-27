from fastapi import HTTPException, status

register_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Could not register the user"
)

asset_file_icon_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Could not open and read default icon file"
)

passwords_dont_match_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Passwords provided didn't match"
)

update_icon_format_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Failed to update icon. Formats allowed: jpeg, png, bmp, webp"
)

update_icon_size_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Failed to update icon. Largest size allowed is 2 MB"
)

incorrect_email_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email",
)

incorrect_password_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect password",
)

not_authenticated_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Not authenticated"
)

expired_signature_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Expired signature, you need to login again"
)

invalid_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid JWT token"
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)

user_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found"
)

game_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Game not found"
)

player_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Player not found"
)

player_not_in_game_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The player is not in the game"
)

player_already_in_game_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The user is already in game"
)

all_spaces_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Game's name must have at least one word"
)

less_than_five_players_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game must have at least 5 players"
)

more_than_ten_players_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game must have less than 10 players"
)

min_player_not_reach_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game has not reach the minimum amount of players"
)

not_the_owner_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="You cant start the game, you are not the owner!"
)

max_players_reach_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game has reach the maximum amount of players"
)

game_has_started_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game has started"
)

game_has_finished_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game has finished"
)

game_not_deleted_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The game has not been deleted"
)

game_not_started_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Game hasn't started"
)

incoherent_amount_of_players_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The minimum of players is higher than the maximum"
)

inconsistent_amount_of_players_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The amount of players is inconsistent to assign roles"
)

not_games_available_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="There are no games available"
)

invalid_player_in_game_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player is not in this game"
)

player_is_dead_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player is dead"
)

player_already_voted_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player already voted"
)

votes_missing_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Vote's missing"
)

cards_taken_in_current_turn_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Already taken the cards in this turn"
)

cards_not_taken_in_current_turn_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Cards were not taken by minister in this turn"
)

turn_hasnt_started_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="No turn started yet"
)

already_promulgated_in_turn_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Director already promulgated in this turn"
)

player_isnt_minister_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player is not minister"
)

didnt_promulgate_in_turn_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Must promulgate in current turn before execute a spell"
)

no_spell_available_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The requirements to cast the spell are not met"
)

player_already_investigated_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player has been already investigated"
)

spell_not_used_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="A spell is available and need to be used before start of next turn"
)

director_candidate_already_set_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Already set director candidate in current turn"
)

invalid_card_type_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The type of the card to discard is invalid"
)

player_isnt_director_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Player is not director"
)

not_discarded_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Card was not discarded"
)

expelliarmus_already_set = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Expelliarmus was already set in current turn"
)

expelliarmus_promulgations_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Expelliarmus requires 5 death eater promulgations"
)

expelliarmus_not_set_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Director didnt propose a Expelliarmus"
)

cant_promulgate_expelliarmus_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Expelliarmu's set, must wait for minister consent before promulgate"
)

consent_already_given_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Consent already given"
)

player_not_killed_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="The player is still alive"
)

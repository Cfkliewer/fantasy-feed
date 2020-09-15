from graphene import ObjectType, String, List, Int
import json

class Roster(ObjectType):
    starters = List(String)
    rosterId = Int()
    players = List(String)
    ownerId = String()
    leagueId = String()

    def __init__(self, starters, roster_id, players, owner_id, league_id, **kwargs):
        self.starters = starters
        self.rosterId = roster_id
        self.players = players
        self.ownerId = owner_id
        self.leagueId = league_id

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)
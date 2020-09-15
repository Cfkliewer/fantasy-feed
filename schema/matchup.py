from graphene import ObjectType, String, List
import json

class Matchup(ObjectType):
    starters = List(String)
    rosterId = String()
    points = String()
    players = List(String)
    matchupId = String()
    customPoints = String()

    def __init__(self, starters, roster_id, points, players, matchup_id, custom_points, **kwargs):
        self.starters = starters
        self.rosterId = roster_id
        self.points = points
        self.players = players
        self.matchupId = matchup_id
        self.customPoints = custom_points

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)
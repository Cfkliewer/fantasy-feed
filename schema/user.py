from graphene import ObjectType, String
import json

class UserType(ObjectType):
    name = String()
    leagueId = String()
    avatar = String()

    def __init__(self, name, league_id, avatar, **kwargs):
        self.name = name
        self.leagueId = league_id
        self.avatar = avatar

    @classmethod
    def from_json(cls, json_string):
        return cls(**json_string)
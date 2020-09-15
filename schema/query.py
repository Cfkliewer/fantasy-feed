from graphene import ObjectType, String, Schema, Field, List, Int
from schema.user import UserType
from schema.matchup import Matchup
from schema.roster import Roster
from sleeper_wrapper import League, User

class Query(ObjectType):

    user = Field(List(UserType), id=String())
    matchups = Field(List(Matchup), leagueId = String(), week = Int())
    rosters = Field(List(Roster), leagueId = String())

    def resolve_user(parent, info, id):
        user = User(id)
        league_info = user.get_all_leagues("nfl", 2020)
        info_list = []
        for i in league_info:
            info = UserType.from_json(i)
            info_list.append(info)

        return info_list
    
    def resolve_matchups(parent, info, leagueId, week):
        league = League(leagueId)
        leagueMatchups = league.get_matchups(week)
        match_list = []
        
        for i in leagueMatchups:
            matches = Matchup.from_json(i)
            match_list.append(matches)

        return match_list

    def resolve_rosters(parent, info, leagueId):
        league = League(leagueId)
        leagueRosters = league.get_rosters()
        roster_list = []

        for i in leagueRosters:
            rosters = Roster.from_json(i)
            roster_list.append(rosters)
        
        return roster_list


schema = Schema(query=Query)
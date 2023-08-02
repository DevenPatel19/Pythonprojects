players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Forward", 
    	"team": "Philadelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    
# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's 
# information instead of individual arguments for the attributes.

player1 = Player({
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
})

# print(player1.name) # Kevin Durant
# print(player1.age) # 34
# print(player1.position) # small forward
# print(player1.team) # Brooklyn Nets

# Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# print(player_kevin.name) # Kevin Durant
# print(player_jason.age) # 24
# print(player_kyrie.position) # Point Guard
# print(player_jason.team) # Boston Celtics

# ... (class definition and large list of players here) = line 1 - line 44
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
    
def populateNewTeam(players):
    for player in players:
        new_team.append(player)
    print(new_team)

populateNewTeam(players)



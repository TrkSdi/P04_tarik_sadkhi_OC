from models.test import end_message
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from datetime import datetime
import sys


class Controller:
    def __init__(self, view):
        self.players = []
        self.tournaments = []
        self.view = view
        
    def launch_program(self):
        while True:
            option = self.view.main_menu()
            if option == "1":
                self.tournament_program()   
            elif option == "2":
                self.players_menu()
            elif option == "3":
                self.report_menu()
            elif option == "0":
                self.quit_program()
            else:
                print("Entrez un choix valide")
        
    def tournament_program(self):
        #while True:
            option = self.view.tournament_menu()
            if option == "1":
                self.start_tournament()
                #continue
            elif option  == "2":
                self.launch_program()
            else:
                print("Entrez un choix valide")
            
    
    def players_menu(self):
        pass
    
    def report_menu(self):
        pass
    
    def quit_program(self):
        return sys.exit()
    
    def start_tournament(self):
        data = self.view.input_tournament()
        self.current_tournament = Tournament(data["tournament_name"], data["place"], data["start_date"], data["end_date"], data["description"], data["number_round"]) 
        print(self.current_tournament)
        self.add_players()
        while self.current_tournament.number_round != len(self.current_tournament.rounds):
            self.start_round()
            
        
    def start_round(self):
            matchs_pair = []
            while True:
                if len(self.current_tournament.rounds) == 0:
                    # c'est le premier round
                    round = Round("Round 1", datetime.now())
                    print("")
                    print(round)
                    matchs_pair = self.generate_pairs_round_1()
                    for pair in matchs_pair:
                        print(f"{pair[0]} \nVS {pair[1]}")   
                    self.current_tournament.rounds.append(round)
                    self.add_score(matchs_pair)
                elif len(self.current_tournament.rounds)  < self.current_tournament.number_round:
                    round = Round(f"Round {len(self.current_tournament.rounds) + 1}", datetime.now())
                    print("")
                    print(round)
                    matchs_pair = self.generate_pairs_remains_round()   
                    for pair in matchs_pair:
                        print(f"{pair[0]} \nVS {pair[1]}")
                    self.current_tournament.rounds.append(round)
                    self.add_score(matchs_pair)
                else:    
                    self.display_score(matchs_pair)
                    self.add_rank(matchs_pair)
                    self.display_rank(matchs_pair)
                    end_message()
                    self.launch_program()
        
        # A ajouter : Le score final des joueurs et leur classement
        # A ajouter : retour au launch program avec message de fin
        
            
        
    def add_players(self):
        MAX_NUM_PLAYERS = 4
        while len(self.current_tournament.players) < MAX_NUM_PLAYERS:
            data = self.view.input_player()
            player = Player(data["last_name"], data["first_name"], data["birth_date"], data["gender"], data["rank"])
            self.current_tournament.players.append(player)
        # Vérification des données des joueurs
        #for player in self.current_tournament.players:
        #    print(player)
        
        
    def generate_pairs_round_1(self):
        sorted_list = sorted(self.current_tournament.players, key=lambda x: x.rank)
        paired_list = [(sorted_list[0], sorted_list[2]),
                       (sorted_list[1], sorted_list[3])]
        return paired_list
    
    
    def generate_pairs_remains_round(self):
        # A vérifier ordre des paires 
        sorted_list = sorted(self.current_tournament.players, key=lambda x: (-x.score, x.rank))
        paired_list = [(sorted_list[0], sorted_list[1]),
                       (sorted_list[2], sorted_list[3])
                       ]
        return paired_list
        
    
    def add_score(self, matchs_pair):
        for pair in matchs_pair:
            for player in pair:
                data = self.view.input_score(player)
                player.score += float(data)
        # Vérification des scores
        #for player in self.current_tournament.players:
        #   print(player)
    
    def add_rank(self, matchs_pair):
        for pair in matchs_pair:
            for player in pair:
                data = self.view.input_rank(player)
                player.rank = data
                
    def display_rank(self, matchs_pair):
        for pair in matchs_pair:
            for player in pair:
                print(f"----- {player}")
        
    
    
    def display_score(self, matchs_pair):
        for pair in matchs_pair:
            for player in pair:
                print(player)
    
    @staticmethod          
    def end_message():
        return print("\n=====================================\nFELICITATIONS, LE TOURNOI EST TERMINE\n=====================================")
                

    
    
    
    
    def run(self):
           
        self.launch_program()
        
        

"""
[
(sorted_list[0], sorted_list[4]),
(sorted_list[1], sorted_list[5]),
(sorted_list[2], sorted_list[6]),
(sorted_list[3], sorted_list[7])
]
"""
"""
[
(sorted_list[0], sorted_list[1]),
(sorted_list[2], sorted_list[3]),
(sorted_list[4], sorted_list[5]),
(sorted_list[6], sorted_list[7])
]

"""
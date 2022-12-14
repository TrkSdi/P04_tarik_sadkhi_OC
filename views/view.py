

class View:

    def main_menu(self):
        print("")
        print("-----------------------------")
        print("Bienvenue au tournoi d'échecs")
        print("-----------------------------")
        print("")
        print("1 - Tournois")
        print("2 - Modifier classement")
        print("3 - Rapports")
        print("0 - Quitter")
        print("")
        return input("Faites votre choix: ")

    def tournament_menu(self):
        print("")
        print("--------------------------------")
        print("1 - Commencer un nouveau tournoi")
        print("2 - Continuer un tournoi")
        print("0 - Menu principal")
        print("--------------------------------")
        print("")
        return input("Faites votre choix: ")

    def input_tournament(self):
        print("")
        tournament_name = input("Entrez le nom du tournoi: ")
        place = input("Indiquez le lieu: ")
        start_date = input("Indiquez la date de début: ")
        end_date = input("Indiquez la date de fin (appuyez sur entrée si même date): ")
        if end_date == "":
            end_date = start_date
        description = input("Entrez une description: ")
        number_round = input("Entre le nombre de tours, sinon 4 par défaut: ")
        if number_round == "":
            number_round = 4
        else:
            number_round = int(number_round)
        return {
            "tournament_name": tournament_name,
            "place": place,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "number_round": number_round
        }

    def input_player(self, current_tournament):
        last_name = input("Entrez le nom du joueur: ")
        while last_name == "":
            print("Le nom du joueur est obligatoire")
            last_name = input("Entrez le nom du joueur: ")
        first_name = input("Entrez le prénom du joueur: ")
        birth_date = input("Entrez la date de naissance du joueur: ")
        gender = input("Entrez le sexe du joueur: ")
        while True:
            rank = input("Entrez son classement: ")
            if not rank.isdigit():
                print("Veuillez entrez un choix valide")
                continue
            elif rank == "":
                print("Veuillez entrez un choix valide")
                continue
            elif rank in current_tournament.rank_list:
                print("Classement déjà assigné")
                continue
            else:
                current_tournament.rank_list.append(rank)
                break

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "gender": gender,
            "rank": rank
        }

    def input_score(self, player):
        print("")
        valid_score = ["1", "0.5", "0"]
        while True:
            score = input(f"Entrez le score du joueur {player.last_name}: ")
            if score == "":
                print("L'ajout du score est nécessaire")
            elif not score.replace('.', '', 1).isdigit():
                print("Le format saisi n'est pas valide")
            elif score not in valid_score:
                print("Le score n'est pas valide")
            else:
                break
        return score

    def input_rank(self, player):
        print("")
        rank = input(f"Entrez le classement du joueur {player.last_name}: ")
        return rank

    def input_report(self):
        print("")
        print("--------------------------------------------------")
        print("1 - Liste de tous les joueurs (alphanumérique)")
        print("2 - Liste de tous les joueurs (classement)")
        print("3 - Liste de tournois")
        print("4 - Liste des joueurs par tournoi (alphanumérique)")
        print("5 - Liste des joueurs par tournoi (classement)")
        print("6 - Liste des tours par tournoi")
        print("7 - Liste des matchs par tournoi")
        print("0 - Menu principal")
        print("--------------------------------------------------")
        print("")

        return input("Faites votre choix: ")

    def input_choice(self):
        print("")

        return input("Faites votre choix: ")

    def select_player(self):
        print("")

        return input("Séléctionnez un joueur: ")

    def change_rank(self):
        print("")

        return input("Entrez le nouveau classement: ")

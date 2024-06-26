class Pandemic:
    import time
    import random
    global epi_count
    epi_count = 4
    global player_data
    player_data = {
        1 : [True, []],
        2 : [True, []],
        3 : [False, []],
        4 : [False, []]
    }
    
    city_color_dict = {
        'Baghdad' : 'Black',
        'Mexico City' : 'Yellow',
        'Buenos Aires' : 'Yellow',
        'Riyadh' : 'Black',
        'Ho Chi Minh City' : 'Red',
        'Los Angeles' : 'Yellow',
        'Bangkok' : 'Red',
        'Moscow' : 'Black',
        'Essen' : 'Blue',
        'Chicago' : 'Blue',
        'Lima' : 'Yellow',
        'Milan' : 'Blue',
        'Madrid' : 'Blue', 
        'Lagos' : 'Yellow', 
        'Tehran' : 'Black', 
        'Shanghai' : 'Red',
        'Algiers' : 'Black',
        'Chennai' : 'Black', 
        'Dehli' : 'Black', 
        'Istanbul' : 'Black',
        'San Fransisco' : 'Blue',
        'Montreal' : 'Blue',
        'Johannesburg' : 'Yellow',
        'Manila' : 'Red',
        'Jakarta' : 'Red',
        'Washington' : 'Blue',
        'Sydney' : 'Red',
        'Hong Kong' : 'Red',
        'Taipei' : 'Red',
        'St. Petersburg' : 'Blue',
        'Santiago' : 'Yellow',
        'Kinsasha' : 'Yellow',
        'Kolkata' : 'Black',
        'Paris' : 'Blue',
        'Karachi' : 'Black',
        'Mumbai' : 'Black',
        'Osaka' : 'Red',
        'Miami' : 'Yellow',
        'Bogota' : 'Yellow',
        'Seoul' : 'Red',
        'Cairo' : 'Black',
        'New York' : 'Blue',
        'London' : 'Blue',
        'Tokyo' : 'Blue',
        'Atlanta' : 'Blue',
        'Khartoum' : 'Yellow',
        'Beijing' : 'Red',
        'Sao Paulo' : 'Yellow'
    }
    global city_card_stack
    city_card_stack = list(city_color_dict.keys())
    random.shuffle(city_card_stack)
    global discard
    discard = []

    def startup():

        #startup, ask for player count, ask starting cards, so that we are able to properly put in epidemics and understand what cards are left
        #cards in player hands are considered the same as in discard (no implementation of player strategy yet)

        #COMMENT FOR DEBUG PURPOSES
        #player_count = int(input("Welcome to Pandemic! How many players will be in this game? "))
        player_count = 3
        #COMMENT FOR DEBUG PURPOSES
        #epi_count = int(input("How many EPIDEMIC cards will you be playing with? "))
        epi_count = 4
        if player_count < 2:
            print('Player count invalid! Restarting')
            return
        elif player_count > 4:
            print('Player count invalid! Restarting')
            return
        else:
            if player_count == 3:
                player_data[3] = True, []
            elif player_count == 4:
                player_data[3] = True, []
                player_data[4] = True, []
        
        for player_num in player_data:
            if player_data.get(player_num)[0] == True:
                temp_hand = []
                
                temp_hand.append(input(f'What cards did player {player_num} draw? Enter one at a time, then press ENTER '))
                temp_hand.append(input(f'What cards did player {player_num} draw? Enter one at a time, then press ENTER '))
                for j in temp_hand:
                    city_card_stack.remove(j)                                        
                    discard.append(j)
                player_data[player_num] = True, temp_hand
        
    def epidemic_insert():
        #divide the city card deck into however many depending on # of epidemic cards, insert the epidemic card, shuffle, and put a list into the list of chunks of X cards
        city_card_stack_shuffled = []
        import random
        left = 0 
        right = len(city_card_stack) // epi_count
        for j in range(epi_count):
            temp_portion = city_card_stack[left:right]
            temp_portion.append('EPIDEMIC')
            random.shuffle(temp_portion)               
            city_card_stack_shuffled.append(temp_portion)
            left = right + 1
            right += len(city_card_stack) // epi_count
        
        print(city_card_stack_shuffled)

    def play():
        for i in range(i, -1, -1):

    startup()
    epidemic_insert()
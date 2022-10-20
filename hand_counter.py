from cribbage_objects import Card

def print_count(points, count_messages):
    for message in count_messages:
        print(message)
    
    print("\n" + str(points) + " total points")
    
def sort_by_rank(hand):
    temp_list = []
    for x in range(1, 14):
        temp_list.append([])
    for card in hand:
        temp_list[card.rank - 1].append(card)
    new_hand = []
    for card_list in temp_list:
        for card in card_list:
            new_hand.append(card)
    return new_hand

def find_fifteen(hand, x, count_message, curr_count, points, count_messages):
    while x < 5:
        if (curr_count + hand[x].value) == 15:
            points += 2
            count_messages.append("Fifteen " + str(points) + ": " + count_message + " " + hand[x].data)
        elif (curr_count + hand[x].value) < 15:
            points = find_fifteen(hand, x+1, (count_message + " " + hand[x].data), curr_count + hand[x].value, points , count_messages)
        x+=1
    return points

def count_fifteens(hand, count_messages):
    points = 0
    
    #only checks with first 4 cards, 5th card can not be 15 on its own
    for x in range(0, 4):
        points = find_fifteen(hand, x+1, hand[x].data, hand[x].value, points, count_messages)
        
    return points

def find_next_in_run(hand, prev_index, count_message, curr_count, points, count_messages):
    recurse_called = False
    #The maximum index worth checking is 2+curr_count
    #this is because if there are less than 5-(2+curr_count) cards left, there is not enough for a run
    x = prev_index+1
    while x < (3 + curr_count) and x < 5:
        if hand[x].rank == hand[prev_index].rank+1:
            hand[x].is_usable = False
            points = find_next_in_run(hand, x, count_message + " " + hand[x].data, curr_count + 1, points, count_messages)
            recurse_called = True
        x+=1
    if recurse_called == False and curr_count > 2:
        points += curr_count
        count_messages.append(count_message + " for " + str(points))
    return points
        
#The starting points are the only ones that cant be used twice.
#If a card is in a run, it can't be used to start a run
def count_runs(hand, total_points, count_messages):
    for x in range(0, 3):
        if hand[x].is_usable:
            total_points = find_next_in_run(hand, x, hand[x].data, 1, total_points, count_messages)
    return total_points

def count_hand(hand):
    total_points = 0
    count_messages = []
    
    total_points += count_fifteens(hand, count_messages)
    hand = sort_by_rank(hand)
    total_points = count_runs(hand, total_points, count_messages)
    
    
    return total_points, count_messages
    
def main():
    hand_data = []
    #get card data from user
    for x in range(1, 6):
        hand_data.append(input("Input card " + str(x) + ": "))
    
    hand = []
    #turn card data into card objects
    for data in hand_data:
        hand.append(Card(data))
    points, count_messages = count_hand(hand)
    print_count(points, count_messages)
    
if __name__ == "__main__":
    main()

"""
CP 1404 Assignment 1 Ron Kang 13668385
"""
import csv

def main_menu(song_num):
    """Main Menu"""
    print("{} songs loaded".format(song_num))
    print("Menu:\nL - List Songs\nA - Add new song\nC - Complete a song\nQ - Quit")


def full_song_list(check_list):
    """Print out the whole list
        row_count - used to check how many songs there are
        song_learn - Used to check how many songs are learned
        song_not_learn - USed to check how many songs are not learned
    """
    row_count = 1
    song_learn = 0
    song_not_learn = 0
    for row in check_list:
        if row[-1] == 'n':
            row[-1] = '*'
            song_not_learn += 1
        else:
            row[-1] = ' '
            song_learn += 1
        print("{}. {} {:<30} - {:<30} ({})".format(row_count, row[-1], row[0], row[1], row[2]))
        if row[-1] == '*':
            row[-1] = 'n'
        else:
            row[-1] = 'y'
        row_count += 1
    if song_not_learn == 0:
        print("No more songs to learn")
    else:
        print("{} songs learned, {} songs still to learn".format(song_learn, song_not_learn))


def invalid_input_number(input):
    if input <= 0:
        print("Number must be > 0")
        return False
    else:
        return True

def invalid_input_char(input):
    if input == '':
        print("Input can not be blank")
        return False
    else:
        return True

def learn_song(song_list):
    """Used for learning songs
    song_choice - which song to learn
    """
    song_choice = 0
    song_choice = int(input("Enter the number of a song to mark as learned\n"))
    while(invalid_input_number(song_choice) == False):
        song_choice = int(input("Enter the number of a song to mark as learned\n"))

    return song_choice


def add_song():
    new_song = []
    add = str(input("Title: "))
    while(invalid_input_char(add) == False):
        add = str(input("Title: "))
    new_song.append(add)
    add = str(input("Artist: "))
    while(invalid_input_char(add) == False):
        add = str(input("Artist: "))
    new_song.append(add)
    add = int(input("Year: "))
    while(invalid_input_number(add) == False):
        add = int(input("Year: "))
    new_song.append(add)
    add = 'n'
    new_song.append(add)
    print("{} by {} ({}) added to the song list".format(new_song[0], new_song[1], new_song[2]))
    return new_song


def main():
    """
    song_num - Total number of songs
    choice_menu - user menu choice
    song_to_learn - Which song on the list to convert from n to y
    """
    song_num = 0
    song_to_learn = 0
    choice_menu = ""
    song_list = []
    song_file = open('songs.csv', 'r')
    for line in song_file:
        song_list.append(line.split(','))
        song_num += 1
    for row in song_list:
        row[-1] = row[-1].strip('\n')
    song_file.close()

    print("Songs To Learn 1.0 - by Ron Kang")

    while(choice_menu.upper() != "Q"):
        main_menu(song_num)
        print(song_list)
        choice_menu = str(input(">>> "))
        if choice_menu.upper() == "L":
            full_song_list(song_list)
        elif choice_menu.upper() == "A":
            song_list.append(add_song())
            song_num += 1
        elif choice_menu.upper() == "C":
            song_to_learn = learn_song(song_list)
            song_list[song_to_learn - 1][-1] = 'y'
            print("{} by {} learned".format(song_list[song_to_learn - 1][0],song_list[song_to_learn - 1][1]))


main()

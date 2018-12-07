"""
CP 1404 Assignment 1 Ron Kang 13668385
"""
import csv


def menu(song_num, menu_type, song_list):
    if menu_type == 1:
        """Main Menu"""
        print("{} songs loaded".format(song_num))
        print("Menu:\nL - List Songs\nC - Complete a song\nQ - Quit")
    elif menu_type == 2:
        """Print out the whole list
            row_count - used to check how many songs there are
            song_learn - Used to check how many songs are learned
            song_not_learn - USed to check how many songs are not learned
        """
        row_count = 1
        song_learn = 0
        song_not_learn = 0
        for row in song_list:
            if row[-1] == 'n':
                row[-1] = '*'
                song_not_learn += 1
            else:
                row[-1] = ' '
                song_learn += 1
            print("{}. {} {:<30} - {:<30} ({})".format(row_count, row[-1], row[0], row[1], row[2]))
            row_count += 1
        if song_not_learn == 0:
            print("No more songs to learn")
        else:
            print("{} songs learned, {} songs still to learn".format(song_learn, song_not_learn))
        print(song_list)

def main():
    """
    menu_type - Used to check which menu to show
    song_num - Total number of songs
    choice_menu - user menu choice
    """
    menu_type = 1
    song_num = 0
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
        menu(song_num, menu_type, song_list)
        choice_menu = str(input(">>> "))
        if choice_menu.upper() == "L":
            menu_type = 2
        elif choice_menu.upper() == "A":
            print("Test A Choice")
        elif choice_menu.upper() == "C":
            print("Test C Choice")


main()

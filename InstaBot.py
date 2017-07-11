# MAIN FILE

from Like_A_Post import like_a_post

from Post_A_Comment import post_a_comment

from Get_User_Post import get_users_post

from GetOwnPost import get_own_post

from Get_User_Info import get_user_info

from Negative_Comment import delete_negative_comment

from Get_Comment_List import get_comment_list

from Get_Like_List import get_like_list

from SelfInfo import self_info

from colorama import *

init()

show_menu = True

# Main Function Starts From Here

while show_menu:

    print "Before Starting This Application Get Certain Help From Us..\n "
    print "\nFor Testing Purpose royal_khann,vishavgupta97 Are Some Valid insta_username"
    print "\n"

    print Fore.BLUE+Style.BRIGHT+"Here are your menu options:"
    print "1.Get your own details\n"
    print "2.Get details of a user by username\n"
    print "3.Get your own recent post\n"
    print "4.Get the recent post of a user by username\n"
    print "5.Get a list of people who have liked the recent post of a user\n"
    print "6.Like the recent post of a user\n"
    print "7.Get a list of comments on the recent post of a user\n"
    print "8.Make a comment on the recent post of a user\n"
    print "9.Delete negative comments from the recent post of a user\n"
    print "10.Exit"
    print (Style.RESET_ALL)

    # Asking value from the user until they give the valid response

    while (True):

            try:
                menu_choice = int(raw_input("Now Kindly Enter Your Choice\n"))

            except ValueError:
                print "\nPlease Enter a valid value..!!"
                continue

            if (menu_choice) <0:
                print "\nValue cannot be negative..!!"
                continue
            elif menu_choice >0 and menu_choice <=10:
                break
            else:
                print "\nEnter a valid number...!!"
                continue



    if menu_choice == 1:
            print "You Have Chosen option To Get Your Information\n"
            print "Following Are Your Details"
            self_info()


    elif menu_choice == 2:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"wait work under process.......")
            get_user_info(insta_username)
            print (Style.RESET_ALL)
            print("\n")


    elif menu_choice == 3:
            print (Fore.GREEN+Style.BRIGHT+"WAit Getting ur post.......\n")
            get_own_post()
            print "Your image has been downloaded!....to.....C:\Users\GUPTA\PycharmProjects\instabot\\"
            print (Style.RESET_ALL)
            print("\n")


    elif menu_choice == 4:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait Downloading user post......")
            get_users_post(insta_username)
            print "Your image has been downloaded!....to.....C:\Users\DELL\PycharmProjects\instabot\\"
            print (Style.RESET_ALL)
            print("\n")


    elif menu_choice == 5:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print(Fore.GREEN+Style.BRIGHT+"Wait getting information.....")
            get_like_list(insta_username)
            print (Style.RESET_ALL)
            print("\n")


    elif menu_choice ==6:
            insta_username = raw_input(Fore.RED + Style.BRIGHT + "Enter Username.........\n")
            print(Fore.GREEN + Style.BRIGHT + "Wait liking Ur POst......")
            like_a_post(insta_username)
            print(Style.RESET_ALL)
            print("\n")


    elif menu_choice ==7:
            insta_username = raw_input(Fore.RED+Style.BRIGHT+"Enter Username.........\n")
            print("\n"+Fore.GREEN+Style.BRIGHT+"Wait getting information.....\n")
            get_comment_list(insta_username)


    elif menu_choice == 8:
            insta_username = raw_input(Fore.BLUE+Style.BRIGHT+"Enter the username of the user: ")
            print(Fore.GREEN+Style.BRIGHT+"Wait Posting A Comment Is Under PROCESS")
            post_a_comment(insta_username)



    elif menu_choice == 9:
            insta_username = raw_input(Fore.RED + Style.BRIGHT + "Enter Username.........\n")
            print("\n" + Fore.GREEN + Style.BRIGHT + "Progress Is In Deletion.\n")
            delete_negative_comment(insta_username)
            print (Style.RESET_ALL)
            print("\n")



    elif menu_choice==10 :
            exit()


    else:
        print "Wrong choice"




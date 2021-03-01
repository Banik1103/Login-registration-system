using System;
using System.Collections.Generic;
using System.IO;

namespace loginsys
{
    class Program
    {
        static void Main(string[] args)
        {
            var userdata = new Dictionary<string, string>()
            {
                {"brian", "hello"},
                {"kenny", "12f"},
                {"bella", "mai"}
            };
            Start(userdata);
        }

        static void Start(Dictionary<string, string> userdata)
        {
            Console.WriteLine("\nHello and welcome to Banik's Login-Registration System.\n");
            Console.Write(
                "If you have an account and want to log in, enter '1'." +
                "\nIf you don't have an account and want to register one, enter '2'." +
                "\nIf you want to quit the application, enter '3': ");
            String user_choice = Console.ReadLine();

            if (user_choice == "1")
            {
                Login(userdata);
            }

            else if (user_choice == "2")
            {
                Registration(userdata);
            }

            else if (user_choice == "3")
            {
                Environment.Exit(0);
            }

            else
            {
                Console.WriteLine("\nUnknown input!");
                Start(userdata);
            }
        }

        static void Login(Dictionary<string, string> userdata)
        {
            Console.Write("\nEnter your username: ");
            String user_name_login = Console.ReadLine();

            Console.Write("\nEnter your password: ");
            String user_password_login = Console.ReadLine();

            if (userdata.ContainsKey(user_name_login))
            {
                if (userdata[user_name_login] == user_password_login)
                {
                    Console.WriteLine("\nSuccessful Login!");
                    LoggedIn(userdata, user_name_login);
                }

                else
                {
                    Console.WriteLine("\nThe username or password is wrong!");
                    Login(userdata);
                }
            }

            else
            {
                Console.WriteLine("\nThe username or password is wrong!");
                Login(userdata);
            }
        }

        static void LoggedIn(Dictionary<string, string> userdata, String username)
        {
            Console.Write("\nOptions:\n" +
                          "Enter 'settings' to edit your account.\n" +
                          "Enter 'quit' to go back to the start: ");

            String user_input = Console.ReadLine();

            if (user_input == "quit")
            {
                Start(userdata);
            }

            else if (user_input == "settings")
            {
                Settings(userdata, username);
            }

            else
            {
                Console.WriteLine("\nUnknown input!");
                LoggedIn(userdata, username);
            }
        }

        static void Settings(Dictionary<string, string> userdata, String username)
        {
            Console.Write("\nEnter 'delete' to delete your account.\n" +
                          "Enter 'name' to change the username of your account.\n" +
                          "Enter 'password' to change the password of your account.\n" +
                          "Enter 'quit' to back to the start section: ");

            String user_input = Console.ReadLine();

            if (user_input == "quit")
            {
                Start(userdata);
            }

            else if (user_input == "delete")
            {
                Delete(userdata, username);
            }

            else if (user_input == "name")
            {
                Name(userdata, username);
            }

            else if (user_input == "password")
            {
                Password(userdata, username);
            }

            else
            {
                Console.WriteLine("\nUnknown input!");
                Settings(userdata, username);
            }
        }

        static void Delete(Dictionary<string, string> userdata, String username)
        {
            Console.Write("\nDo you really want to delete your account?\n" +
                          "If yes, enter 'DELETE'.\n" +
                          "If not, enter 'quit' to go back to the settings menu: ");

            String user_input = Console.ReadLine();

            if (user_input == "quit")
            {
                Settings(userdata, username);
            }

            else if (user_input == "DELETE")
            {
                userdata.Remove(username);
                Console.WriteLine("\nYour account has been deleted.\n" +
                                  "Thank you for using my login/registration system." +
                                  "The program will close itself automatically in five seconds.\n");
                Environment.Exit(0);
            }

            else
            {
                Console.WriteLine("\nUnknown input!");
                Delete(userdata, username);
            }
        }

        static void Name(Dictionary<string, string> userdata, String username)
        {
            Console.Write("\nEnter your new username: ");
            String new_user_name = Console.ReadLine();

            Console.Write("\nEnter your new username again: ");
            String new_user_name2 = Console.ReadLine();

            if (new_user_name == new_user_name2)
            {
                userdata.Add(new_user_name, userdata[username]);
                userdata.Remove(username);
                username = new_user_name;

                Console.WriteLine("\nYour username was updated successfully!");
                Settings(userdata, username);
            }

            else
            {
                Console.WriteLine("\nThe usernames don't match!");
                Name(userdata, username);
            }
        }

        static void Password(Dictionary<string, string> userdata, String username)
        {
            Console.Write("\nEnter your new password: ");
            String new_user_password = Console.ReadLine();

            Console.Write("\nEnter your new password again: ");
            String new_user_password2 = Console.ReadLine();

            if (new_user_password == new_user_password2)
            {
                userdata[username] = new_user_password;

                Console.WriteLine("\nYour password was changed successfully!");
                Settings(userdata, username);
            }

            else
            {
                Console.WriteLine("\nThe passwords don't match!");
                Password(userdata, username);
            }
        }

        static void Registration(Dictionary<string, string> userdata)
        {
            Console.Write("\nTo register a new account, enter a username: ");
            String new_user_user_name = Console.ReadLine();

            Console.Write("Enter a password: ");
            String new_user_user_password = Console.ReadLine();

            Console.Write("Enter the password again: ");
            String new_user_confirm_password = Console.ReadLine();

            if (userdata.ContainsKey(new_user_user_name))
            {
                Console.WriteLine("\nAn account associated with your username is already registered!");
                Registration(userdata);
            }
            
            else
            {
                if (new_user_user_password == new_user_confirm_password)
                {
                    Console.WriteLine("\nSuccesful registration!");

                    userdata.Add(new_user_user_name, new_user_user_password);

                    Start(userdata);
                }

                else
                {
                    Console.WriteLine("\nThe passwords are not matching! Try again!");
                    Registration(userdata);
                }
            }
        }
    }
}
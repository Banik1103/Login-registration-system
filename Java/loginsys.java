package com.company;
import java.io.*;
import java.util.Hashtable;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static Map<String, String> user_information_dict = new HashMap<>();

    public static void main(String[] args) {
        start();
    }

    public static void start() {
        System.out.println("\nHello and welcome to Banik's loginsys.\nIf you already have an account and want to log in, enter '1'.");
        System.out.println("If you don't have an account and want to create one, enter '2'.\nIn order to exit the program, enter '3'.\n");

        Scanner myScanner = new Scanner(System.in);
        String user_input = myScanner.nextLine();

        switch (user_input) {
            case "1" -> login();
            case "2" -> registration();
            case "3" -> System.out.close();
            default -> {
                System.out.println("\nUnknown Input!");
                start();
            }
        }
    }

    public static void login() {
        System.out.println("\nEnter your username: ");
        Scanner myScanner_1 = new Scanner(System.in);
        String username = myScanner_1.nextLine();

        System.out.println("\nEnter your password: ");
        Scanner myScanner_2 = new Scanner(System.in);
        String password = myScanner_2.nextLine();

        if (password.equals(user_information_dict.get(username))) {
            System.out.println("\nThe login was successful!");
            logged_in(username);
        }

        else {
            System.out.println("\nThe username or password is incorrect.");
            login();
        }
    }

    public static void logged_in(String username) {
        System.out.println("\nEnter 'settings' to visit the settings.\nEnter 'quit' to go back to the start.\n");

        Scanner my_Scanner = new Scanner(System.in);
        String user_input = my_Scanner.nextLine();

        if (user_input.equals("settings")) {
            settings(username);
        }

        else if (user_input.equals("back")) {
            start();
        }

        else {
            System.out.println("Unknown input!");
            logged_in(username);
        }
    }

    public static void settings(String username) {
        System.out.println("\nEnter 'delete' to delete your account.\nEnter 'name' to change your username.\nEnter 'password' to change the password of your account.");
        System.out.println("Enter 'quit' to go back to the start.\n");

        Scanner myScanner = new Scanner(System.in);
        String user_input = myScanner.nextLine();

        switch (user_input) {
            case "delete" -> delete(username);
            case "name" -> name(username);
            case "password" -> password(username);
            case "quit" -> start();
            default -> {
                System.out.println("\nUnknown Input!");
                settings(username);
            }
        }
    }

    public static void delete(String username) {
        System.out.println("\nDo you really want to delete your account?\nIf yes, enter 'DELETE', if not, enter 'quit'.\n");
        Scanner myScanner = new Scanner(System.in);
        String user_input = myScanner.nextLine();

        if (user_input.equals("DELETE")) {
            user_information_dict.remove(username);
        }

        else if (user_input.equals("quit")) {
            settings(username);
        }

        else {
            System.out.println("\nUnknown Input!");
            delete(username);
        }
    }

    public static void name(String username) {
        System.out.println("\nTo go back to the settings, enter '1'.\nIn order to change your username, enter '2'.\n");
        Scanner myScanner = new Scanner(System.in);
        String user_input = myScanner.nextLine();

        if (user_input.equals("1")) {
            settings(username);

        }

        else if (user_input.equals("2")) {
            System.out.println("\nEnter your new username:");
            Scanner myScanner2 = new Scanner(System.in);
            String new_username = myScanner2.nextLine();

            System.out.println("\nEnter your new username again:");
            Scanner myScanner3 = new Scanner(System.in);
            String new_username2 = myScanner3.nextLine();

            if (new_username.equals(new_username2)) {
                System.out.println("\nYour username was updated successfully!");

                user_information_dict.put(new_username, user_information_dict.get(username));
                user_information_dict.remove(username);

                String user_name = new_username;
                settings(username);
            }

            else {
                System.out.println("\nThe usernames don't match!");
                name(username);
            }
        }
    }

    public static void password(String username) {
        System.out.println("\nTo go back to the settings, enter '1'.\nTo change your password, enter '2'.\n");
        Scanner myScanner = new Scanner(System.in);
        String user_input = myScanner.nextLine();

        if (user_input.equals("1")) {
            settings(username);
        }

        else if (user_input.equals("2")) {
            System.out.println("\nEnter your new password:");
            Scanner myScanner2 = new Scanner(System.in);
            String new_password = myScanner2.nextLine();

            System.out.println("\nEnter your new password again:");
            Scanner myScanner3 = new Scanner(System.in);
            String new_password2 = myScanner3.nextLine();

            if (new_password.equals(new_password2)) {
                System.out.println("\nYour password was updated successfully!");

                user_information_dict.replace(username, new_password);
                System.out.println(user_information_dict);
                settings(username);
            }

            else {
                System.out.println("\nThe passwords don't match!");
                password(username);
            }
        }
    }

    public static void registration() {
        System.out.println("\nEnter the username you want to choose:");
        Scanner myScanner = new Scanner(System.in);
        String username = myScanner.nextLine();

        System.out.println("\nEnter the password you want to choose:");
        Scanner myScanner2 = new Scanner(System.in);
        String password = myScanner2.nextLine();

        if (user_information_dict.containsKey(username)) {
            System.out.println("\nAn account associated with your username is already registered.\nPlease choose a new username.");
            registration();
        }

        else {
            user_information_dict.put(username, password);
            System.out.println("\nSuccessful registration!");
            start();
        }
    }
}
import 'dart:io';

void main() {
  var userdata = {"brian": "hello"};
  Start(userdata);
}

void Start(var userdata) {
  print("\nHello and welcome to a loginsys, created by Banik.\n\nOptions:\n");
  print("Enter 'login' to log into your account.");
  print("Enter 'register' to create a new account.");
  print("Enter 'quit' to exit the programm.\n");

  String user_input = stdin.readLineSync();

  switch (user_input) {
    case "login":
      {
        Login(userdata);
      }
      break;

    case "register":
      {
        Registration(userdata);
      }
      break;

    case "quit":
      {
        exit(0);
      }
      break;

    default:
      {
        print("\nUnknown Input!");
        Start(userdata);
      }
  }
}

void Login(var userdata) {
  print("\nEnter your username:");
  String username_login_input = stdin.readLineSync();

  print("\nEnter your password:");
  String password_login_input = stdin.readLineSync();

  if (userdata.containsKey(username_login_input)) {
    if (userdata[username_login_input] == password_login_input) {
      print("\nSuccessful login!");
      Logged_in(userdata, username_login_input);
    } else {
      print("\nUsername or password is incorrect!");
      Login(userdata);
    }
  } else {
    print("\nUsername or password is incorrect!");
    print(
        "\nDou you want to proceed or go back to the Start?\nEnter '1' if yes, else enter '2':");

    String user_input = stdin.readLineSync();

    if (user_input == "1") {
      Start(userdata);
    } else if (user_input == "2") {
      Login(userdata);
    } else {
      print("\nUnknown Input!");
      Login(userdata);
    }
  }
}

void Logged_in(var userdata, String username) {
  print("\nOptions:\n");
  print("Enter 'settings' to edit your account.");
  print("Enter 'quit' to go back to the start.\n");

  String user_input = stdin.readLineSync();

  if (user_input == "settings") {
    Settings(userdata, username);
  } else if (user_input == "quit") {
    Start(userdata);
  } else {
    print("\nUnknown input!");
    Logged_in(userdata, username);
  }
}

void Settings(var userdata, String username) {
  print("\nEnter 'delete' to delete your account.");
  print("Enter 'name' to change the username of your account.");
  print("Enter 'password' to change the password of your account.");
  print("Enter 'quit' to back to the start section.\n");

  String user_input = stdin.readLineSync();

  switch (user_input) {
    case "delete":
      {
        Delete(userdata, username);
      }
      break;

    case "name":
      {
        Name(userdata, username);
      }
      break;

    case "password":
      {
        Password(userdata, username);
      }
      break;

    case "quit":
      {
        Start(userdata);
      }
      break;

    default:
      {
        print("\nUnknown input!");
        Settings(userdata, username);
      }
      break;
  }
}

void Delete(var userdata, String username) {
  print("\nDo you really want to delete your account?\n");
  print("If yes, enter 'DELETE'.\n");
  print("If not, enter 'quit' to go back to the settings menu.\n");

  String user_input = stdin.readLineSync();

  if (user_input == "DELETE") {
    userdata.remove(username);
    print("\nYour account was deleted successfully!");
    Start(userdata);
  } else if (user_input == "quit") {
    Settings(userdata, username);
  } else {
    print("\nUnknown input!");
    Delete(userdata, username);
  }
}

void Name(var userdata, String username) {
  print("\nEnter your new username:");
  String new_username1 = stdin.readLineSync();

  print("\nEnter your new username again:");
  String new_username2 = stdin.readLineSync();

  if (new_username1 == new_username2) {
    if (userdata.containsKey(new_username1)) {
      print(
          "\nAn account associated with your username is already registered.");
      Name(userdata, username);
    } else {
      print("\nYour username was updated successfully!");
      userdata[new_username1] = userdata[username];
      userdata.remove(username);
      Settings(userdata, new_username1);
    }
  } else {
    print("\nThe usernames don't match!");
    Name(userdata, username);
  }
}

void Password(var userdata, String username) {
  print("\nEnter your new password:");
  String new_password1 = stdin.readLineSync();

  print("\nEnter your new password again:");
  String new_password2 = stdin.readLineSync();

  if (new_password1 == new_password2) {
    print("\nYour password was updated successfully!");
    userdata[username] = new_password1;
    Settings(userdata, username);
  } else {
    print("\nThe passwords don't match!");
    Password(userdata, username);
  }
}

void Registration(var userdata) {
  print("\nEnter your username:");
  String new_username = stdin.readLineSync();

  print("\nEnter your password:");
  String new_password = stdin.readLineSync();

  if (userdata.containsKey(new_username)) {
    print(
        "\nAn account associated with your username is already registered. Please try again.");
    Registration(userdata);
  } else {
    print("\nYour account was registered successfully!");
    userdata[new_username] = new_password;
    Start(userdata);
  }
}

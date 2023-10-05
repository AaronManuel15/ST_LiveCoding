#!/usr/bin/env python3
import cmd
import pickle

class CensusDataConsole(cmd.Cmd):
    intro = "\033[1mCensus Data Storage Console. Type 'help' to see available commands.\033[0m"
    prompt = "\033[1mHow may I help you -____-: \033[0m"

    def __init__(self):
        """Bit self explanatory __init__???"""
        super().__init__()
        self.census_data = []

    def preloop(self):
        """EXAMPLE OF POLYMORPHISM
        Execute before entering the command loop."""
        print("\033[1mWelcome to the Census Data Storage Console\033[0m")
        self.load_from_pickle("census_data.pickle")

    def postloop(self):
        """EXAMPLE OF POLYMORPHISM
        Execute after leaving the command loop."""
        self.do_save_to_pickle("census_data")
        print("\033[1mExiting... Data saved to census_data.pickle\033[0m")

    def load_from_pickle(self, filename):
        """Load data from a pickle file if it exists."""
        try:
            with open(filename, 'rb') as file:
                self.census_data = pickle.load(file)
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty dataset.")
        except Exception as e:
            print(f"Error loading data from {filename}: {e}")

    def do_add_data(self, line):
        """
        Adds census data to the storage. Format: add_data name, age, city
        """
        data = line.split(", ")
        if len(data) == 3:
            name, age, city = data
            self.census_data.append((name, age, city))
            print(f"Added data: {name}, {age}, {city}")
        else:
            print("Invalid input. Format: add_data name, age, city")

    def do_save_to_pickle(self, line):
        """
        Saves census data to a pickle file.
        """
        try:
            with open('census_data.pickle', 'wb') as file:
                pickle.dump(self.census_data, file)
            print(f"Data saved to census_data.pickle")
        except Exception as e:
            print(f"Error saving data to census_data.pickle: {e}")

    def do_show_data(self, line):
        """Show all census data."""
        print("\n\033[32mFrom list:\033[0m \n" + str(self.census_data))

        print("\n\033[32mFrom pickle file:\033[0m")
        try:
            with open('census_data.pickle', 'rb') as file:
                data = pickle.load(file)
                for item in data:
                    print(item)
                print()
        except FileNotFoundError:
            print(f"File census_data.pickle not found.")
        except Exception as e:
            print(f"Error reading data from census_data.pickle: {e}")


    def do_quit(self, line):
        """Too legit to quit."""
        print("Exiting...")
        return True

if __name__ == '__main__':
    console = CensusDataConsole()
    console.doc_header = "\033[1mHeyooooo this is pretty cool....\nAvailable commands (type help <command>):\033[0m"
    console.cmdloop()

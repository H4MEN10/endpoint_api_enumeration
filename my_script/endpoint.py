#!/usr/bin/env python

import argparse
import requests

#base_url = input("Enter the base URL: ").strip()
#file_path = "api.txt"
def main():
    parser = argparse.ArgumentParser(description='Check the existence of URLs formed by appending words from a file to a base URL.')
    parser.add_argument('-u', '--url', required=True, help='Identify target')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file')
    args = parser.parse_args()
    
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    base_url = args.url.rstrip("/") + ""

    # Read words from the file
    with open(args.wordlist, "r") as file:
         words = file.read().splitlines()

    # Make requests for each URL
    print(f"------------------------------------------------^_^------------------------------------------------------------")
    for word in words:
           url = base_url + word
           
           try:
              response = requests.get(url)
              status_code = response.status_code
              colored_status = f"{GREEN} URL exit {status_code}{RESET}"
              red_status = f"{RED} URL does not exist {status_code}{RESET}" 
              if status_code == 200:
                 print(f" {colored_status}: {url}")
              else:
                 print(f" {red_status}: {url}")
           except requests.ConnectionError:
              print(f"Failed to connect to: {url}")
    		
if __name__ == "__main__":
    main()

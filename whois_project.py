# This script will use domains and IP addresses to obtain whois information
# pip install python-whois
# pip install futures
# pip install IPy

import whois
import dns.resolver, dns.reversename
import os
import pyfiglet

def ip_lookup():
    while True:
        ip = input("Enter the IP: ")
        try:
            reverse_lookup = dns.reversename.from_address(ip)
            reverse_lookup = str(dns.resolver.resolve(reverse_lookup,"PTR")[0])
            if reverse_lookup.endswith("."):
                reverse_lookup = reverse_lookup[:-1]
            return reverse_lookup
        except:
            print("Please enter an acceptable IP. IPv4 or IPv6 works.")

def domain_lookup(domain):
    while True:
        domain_lookup = whois.whois(domain)
        if domain_lookup.text == "":
            print("Something went wrong. Try again.")
            domain = input("What domain are you trying to look up? ")
        else:
            return domain_lookup.text

def file_output(result):
    file_path = input("What file path would you like to save this under? If left blank it will be assigned to your current working directory. ")
    file_name = input("What file name would you like to use? If left blank it will be assigned to 'whois'. ")

    while True:
        if file_path == "":
            file_path = os.getcwd()
    
        if file_name == "":
            file_name = "whois"
    
        if " " in file_name:
            file_name.replace(" ", "_")

        full_path = os.path.join(file_path, file_name + ".txt")

        try:
            with open(full_path, "x") as f:
               f.write(result) 
               print("File named " + file_name + " was saved under " + file_path)
               break
        except FileExistsError:
            print("That file already exists")
            file_name = input("What file name would you like to use? If left blank it will be assigned to 'whois'. ")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("WHOIS")
    print("-" * 70)
    print(ascii_banner)
    print("-" * 70)
    keep_going = True
    while keep_going == True:
        choice = input("Are you supplying an IP or a domain? ").capitalize()
        output_to_file = input("Would you like to output the results to a .txt file? ").capitalize()
        if choice == "Ip":
            reverse_lookup = ip_lookup()
            result = domain_lookup(reverse_lookup)
        elif choice == "Domain":
            domain = input("What domain are you trying to look up? ")
            result = domain_lookup(domain)
        else:
            print("You entered an incorrect option.")
            continue

        if output_to_file == "Yes":
            file_output(result)
        else:
            print(result)

        while True:
            again = input("Would you like to look up another domain or IP address (yes or no)? ").capitalize()
            if again == "Yes":
                break
            elif again == "No":
                keep_going = False
                print("Thanks for using my script. I hope it helped")
                break
            else:
                print("Please enter a valid response.")
                continue
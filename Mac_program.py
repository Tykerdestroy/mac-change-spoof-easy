import subprocess 
import argparse 
import sys 
import re 
  
  
def get_arguments(): 
    # This will give user a neat CLI 
    parser = argparse.ArgumentParser() 
    # We need the interface name 
    parser.add_argument("-i", "--interface", 
                dest="interface", 
                help="Name of the interface. " 
                "Type ifconfig for more details.") 
    options = parser.parse_args() 
    # Check if interface was given 
    if options.interface: 
        return options.interface 
    else: 
        parser.error("[!] Invalid Syntax. " 
                     "Use --help for more details.") 
  
def change_mac(interface, new_mac_address): 
    subprocess.call(["sudo", "ifconfig", interface, "down"])

    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_address])

    subprocess.call(["sudo", "ifconfig", interface, "up"])
  
def get_current_mac(interface): 
    output = subprocess.check_output(["ifconfig", 
                                      interface]) 
    return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", 
                  str(output)).group(0) 
   
if name == "main": 
    print("[* Welcome to MAC ADDRESS Changer *]") 
    print("[*] Press CTRL-C to QUIT") 
    # Change it to required value(in sec) 
    TIME_TO_WAIT = 60 
    interface = get_arguments() 
    current_mac = get_current_mac(interface)

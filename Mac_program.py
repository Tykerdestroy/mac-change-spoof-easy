import subprocess 
import argparse 
import sys 
import re 
  
  
def get_arguments(): 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-i", "--interface", 
                dest="interface", 
                help="Name of the interface. " 
                "Type ifconfig for more details.") 
    options = parser.parse_args() 
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
    TIME_TO_WAIT = 60 
    interface = get_arguments() 
    current_mac = get_current_mac(interface)

    try: 
        while True: 
            random_mac = get_random_mac_address() 
            change_mac(interface, random_mac) 
            new_mac_summary = subprocess.check_output( 
                ["ifconfig", interface]) 
            if random_mac in str(new_mac_summary): 
                print("\r[*] MAC Address Changed to", 
                      random_mac, 
                      end=" ") 
                sys.stdout.flush() 
            time.sleep(TIME_TO_WAIT) 
  
    except KeyboardInterrupt: 
        change_mac(interface, current_mac) 
        print("\n[+] Quitting Program...")
    KeyboardInterrupt()
    print()
    get-current-mac()

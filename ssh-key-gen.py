# python file to generate ssh keys with a lot of options
# so cooool
# this is probably gonna turn out to be garbage, but whatever it's totally fine
## after making this for a while, i realized how garbage i am at coding :)
## at least it works!!
from os import system as x
from re import X
import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: print("\nuh, okay, bye") & sys.exit(1))
print("hi, we're gonna make an ssh key! :D\n")
print("""options for key types:
[1] dsa
[2] ecdsa
[3] ecdsa-sk
[4] ed25519
[5] ed25519-sk
[6] rsa
(p.s. names that end in \"sk\" are for use with fido2 keys)
""")

while True:
    key_type = str(input("choose a key type [1-6]: "))
    if key_type not in ["1", "2", "3", "4", "5", "6"]:
        print("uh, try choosing a number between 1 and 6?")
        continue
    break
if key_type == "6":
    # doing it this way this time because of some weird visual glitch
    print("rsa key sizes: ")
    print("[1] 1024")
    print("[2] 2048")
    print("[3] 3072")
    print("[4] 4096")
    while True:
        rsa_key_size = str(input("choose the number of bits in your rsa key: "))
        if rsa_key_size not in ["1", "2", "3", "4"]:
            print("choose a number between 1 and 4 please")
            continue
        break
comment_temp = str(input("add a comment to your key (if left empty there will be no comment): "))

if comment_temp == "" or comment_temp == " ":
    print("okay, your key will not have a comment")
    comment = False
else:
    print(f"okay, your key's comment will be: \"{comment_temp}\"")
    comment = comment_temp

print("let's start")
if comment == False:
    if key_type == "1":
        x("ssh-keygen -t dsa")
    elif key_type == "2":
        x("ssh-keygen -t ecdsa")
    elif key_type == "3":
        x("ssh-keygen -t ecdsa-sk")
    elif key_type == "4":
        x("ssh-keygen -t ed25519")
    elif key_type == "5":
        x("ssh-keygen -t ed25519-sk")
    if key_type == "6" and rsa_key_size == "1":
        x("ssh-keygen -t rsa -b 1024")
    elif key_type == "6" and rsa_key_size == "2":
        x("ssh-keygen -t rsa -b 2048")
    elif key_type == "6" and rsa_key_size == "3":
        x("ssh-keygen -t rsa -b 3072")
    elif key_type == "6" and rsa_key_size == "4":
        x("ssh-keygen -t rsa -b 4096")
else:
    if key_type == "1":
        x(f"ssh-keygen -t dsa -C \"{comment}\"")
    elif key_type == "2":
        x(f"ssh-keygen -t ecdsa -C \"{comment}\"")
    elif key_type == "3":
        x(f"ssh-keygen -t ecdsa-sk -C \"{comment}\"")
    elif key_type == "4":
        x(f"ssh-keygen -t ed25519 -C \"{comment}\"")
    elif key_type == "5":
        x(f"ssh-keygen -t ed25519-sk -C \"{comment}\"")
    if key_type == "6" and rsa_key_size == "1":
        x(f"ssh-keygen -t rsa -b 1024 -C \"{comment}\"")
    elif key_type == "6" and rsa_key_size == "2":
        x(f"ssh-keygen -t rsa -b 2048 -C \"{comment}\"")
    elif key_type == "6" and rsa_key_size == "3":
        x(f"ssh-keygen -t rsa -b 3072 -C \"{comment}\"")
    elif key_type == "6" and rsa_key_size == "4":
        x(f"ssh-keygen -t rsa -b 4096 -C \"{comment}\"")

print("yay, we made your key!")
print("bye now")

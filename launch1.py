import subprocess

def open_firefox():
    try:
        subprocess.run(["firefox"])
    except FileNotFoundError:
        print("Firefox not found. Make sure it is installed or provide the correct path.")

if __name__ == "__main__":
    open_firefox()

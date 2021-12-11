import sys, json

f = open('config.json')
config = json.load(f)
f.close()

if __name__ == "__main__":
    sys.exit(f"Not created to be executed")
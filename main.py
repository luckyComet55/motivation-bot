from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print(os.getenv('API_KEY'))

if __name__ == '__main__':
    main()
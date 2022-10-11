import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ["HELLO"])

# this doesn't need dotenv, because this is my systems variable
print(os.environ["HOME"])
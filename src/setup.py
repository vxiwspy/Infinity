import os

os.system("clear || cls")

modules = ["discord", "aiohttp", "aiolimiter", "colorama", "requests", "datetime", "colored", "pystyle"] # more to come

for i in modules: os.system(f"pip install -q {i}");

os.system("python main.py")
exit()
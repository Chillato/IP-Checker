from colorama import Fore as colore
import requests, sys, os, sqlite3

try:
    conn = sqlite3.connect("database.db")
    conn.cursor().execute("CREATE TABLE IF NOT EXISTS ip (ipsend INT)")
except sqlite3.OperationalError:
    pass

class inzio():
    check = int(input(f"""
{colore.YELLOW}ooooo oooooooooo             oooooooo8 ooooo ooooo ooooooooooo  oooooooo8 oooo   oooo ooooooooooo oooooooooo  
{colore.YELLOW} 888   888    888          o888     88  888   888   888    88 o888     88  888  o88    888    88   888    888 
{colore.YELLOW} 888   888oooo88 ooooooooo 888          888ooo888   888ooo8   888          888888      888ooo8     888oooo88  
{colore.YELLOW} 888   888                 888o     oo  888   888   888    oo 888o     oo  888  88o    888    oo   888  88o   
{colore.YELLOW}o888o o888o                 888oooo88  o888o o888o o888ooo8888 888oooo88  o888o o888o o888ooo8888 o888o  88o8 

{colore.RED}Script by {colore.BLUE}ChillatoDev

{colore.GREEN}1 - Check ip
{colore.GREEN}2 - List ip 

{colore.GREEN}Choose:  """))


    if check == 1:
        ip = input(f"""
{colore.YELLOW}ooooo oooooooooo             oooooooo8 ooooo ooooo ooooooooooo  oooooooo8 oooo   oooo ooooooooooo oooooooooo  
{colore.YELLOW} 888   888    888          o888     88  888   888   888    88 o888     88  888  o88    888    88   888    888 
{colore.YELLOW} 888   888oooo88 ooooooooo 888          888ooo888   888ooo8   888          888888      888ooo8     888oooo88  
{colore.YELLOW} 888   888                 888o     oo  888   888   888    oo 888o     oo  888  88o    888    oo   888  88o   
{colore.YELLOW}o888o o888o                 888oooo88  o888o o888o o888ooo8888 888oooo88  o888o o888o o888ooo8888 o888o  88o8 

{colore.CYAN} send ip: """)
        checker = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        continente = checker["continent"]
        city = checker["city"]
        country = checker["country"]
        proxy = checker["proxy"]
        host = checker["hosting"]
        print(f"""
{colore.GREEN}IP: {colore.BLUE}{ip}
{colore.GREEN}Continent: {colore.BLUE}{continente}
{colore.GREEN}City: {colore.BLUE}{city}
{colore.GREEN}Country: {colore.BLUE}{country}
{colore.GREEN}Proxy: {colore.BLUE}{proxy}
{colore.GREEN}Host: {colore.BLUE}{host}
""")
        conn.cursor().execute("INSERT INTO ip (ipsend) VALUES(?)", [ip])
        conn.commit()

    if check == 2:
        iplist = ""
        count = conn.cursor().execute("SELECT COUNT(ipsend) FROM ip").fetchone()[0]
        if count == 0:
            print("Lista ip vuota...")
        else:
            for ip, in conn.cursor().execute("SELECT ipsend FROM ip").fetchall():
                checker = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
                continente = checker["continent"]
                iplist += f"➥ {ip} - {continente}\n"
            print(iplist)

import time
from database import init_db, insert_data
from image_processor import get_gold
from api_request import get_current_time

def main():
    conn = init_db()

    while True:
        blue_gold = get_gold(22,52, 1065,1139)
        red_gold = get_gold(22,52,  1470,1540)
        if blue_gold and red_gold:
            game_time =  get_current_time() 
            insert_data(conn, game_time, blue_gold, red_gold)

            print(f"{game_time}: BLUE: {blue_gold}, RED: {red_gold}")
            time.sleep(5)
        else:
            print("No se detectó ningún número en la imagen recortada.")
            time.sleep(1)
if __name__ == "__main__":
    main()

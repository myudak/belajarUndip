import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "kelompok-2/undip"


awal_ascii_art = r"""
 ____  __.     .__                                __     ________  
|    |/ _|____ |  |   ____   _____ ______   ____ |  | __ \_____  \ 
|      <_/ __ \|  |  /  _ \ /     \\____ \ /  _ \|  |/ /  /  ____/ 
|    |  \  ___/|  |_(  <_> )  Y Y  \  |_> >  <_> )    <  /       \ 
|____|__ \___  >____/\____/|__|_|  /   __/ \____/|__|_ \ \_______ \
        \/   \/                  \/|__|               \/         \/
"""


def pub(c, msg):
    print("→", msg)
    c.publish(TOPIC, msg, qos=0, retain=False)


def menu():
    print("\n=== Lampu Merah ===")
    print("[1] Mode: AUTOMATIC")
    print("[2] Mode: DARURAT (Lampu merah terus)")
    print("[3] Mode: MALEM (Lampu kuning kedap kedip)")
    print("[4] Mode: RUSUH (Lampu hijau kedap kedip)")
    print("[5] Manual: send digit (0-9)")
    print("[6] Manual: control lampu merah (merah/kuning/hijau on/off)")
    print("[7] Quick test: countdown 9→0 (manual)")
    print("[0] Exit")


def main():
    c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    c.connect(BROKER, 1883, 60)
    c.loop_start()

    print(awal_ascii_art)

    try:
        while True:
            menu()
            choice = input("Prompt: ").strip()

            if choice == "1":
                pub(c, "mode:automatic")

            elif choice == "2":
                pub(c, "mode:darurat")

            elif choice == "3":
                pub(c, "mode:malem")

            elif choice == "4":
                pub(c, "mode:rusuh")

            elif choice == "5":
                d = input("Digit (0-9): ").strip()
                if d.isdigit() and 0 <= int(d) <= 9:
                    pub(c, f"digit:{d}")
                else:
                    print("Invalid digit.")

            elif choice == "6":
                color = input("Color [red|yellow|green]: ").strip().lower()
                state = input("State [on|off]: ").strip().lower()
                if color in ("red", "yellow", "green") and state in ("on", "off"):
                    pub(c, f"tl:{color}:{state}")
                else:
                    print("Invalid color/state.")

            elif choice == "7":
                for d in range(9, -1, -1):
                    pub(c, f"digit:{d}")
                    time.sleep(0.7)

            elif choice == "0":
                break

            else:
                print("Unknown choice.")

    except KeyboardInterrupt:
        pass
    finally:
        c.loop_stop()
        c.disconnect()
        print("Bye!")


if __name__ == "__main__":
    main()

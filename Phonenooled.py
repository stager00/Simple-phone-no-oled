from picrawler import Picrawler
from robot_hat import TTS, Music
from bleak import BleakScanner
import asyncio
import time

crawler = Picrawler()
tts = TTS()
music = Music()

# Bluetooth MAC address of your phone
phone_mac_address = "20:20:08:59:27:13"

async def find_phone():
    devices = await BleakScanner.discover()
    return any(device.address == phone_mac_address for device in devices)

async def main():
    speed = 80
    while True:
        try:
            phone_detected = await find_phone()
            if phone_detected:
                print("Phone detected! Moving towards it.")
                tts.say("Phone detected! Moving towards it.")
                crawler.do_action('forward', 1, speed)
            else:
                print("Phone not detected. Scanning...")
                tts.say("Phone not detected. Scanning...")
                crawler.do_action('turn left', 1, speed)
        except Exception as e:
            print(f"An error occurred: {e}")
            tts.say("An error occurred.")
        time.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())

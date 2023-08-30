import asyncio
import websockets
    

async def main():
    async with websockets.connect("ws://localhost:7007") as websocket:
        name = input("Name: ")
        await websocket.send(name)
        reply = await websocket.recv()
        print(f"Name: {name}")
        while True:
            msg = input(f"{name}: ")

            if(msg.__eq__('quit') == True):
                break
            await websocket.send(msg)
            reply = await websocket.recv()
            print(f"{name}: {reply}")

asyncio.run(main())
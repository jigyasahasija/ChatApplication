import asyncio
from websockets.server import serve

HOST = "127.0.0.1"
PORT = 7007

async def echo(websocket):
    while(True):
        data = await websocket.recv()

        if(data.__eq__('quit') == True):
            break
        reply = f"{data}!"
        await websocket.send(reply)

async def main():
    print(f"Listening on {HOST}, {PORT}")
    async with serve(echo, HOST, PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())
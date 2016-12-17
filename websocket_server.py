import asyncio
import datetime
import websockets
import sqlite3

async def sendNames(websocket, path):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    # c.execute("CREATE TABLE person (firstname text, lastname text)")
    # c.execute("INSERT INTO person VALUES ('gery', 'bieli')")
    #
    # conn.commit()

    for row in c.execute('SELECT * FROM person'):
        for d in row:
            await websocket.send(d)
    conn.close()

start_server = websockets.serve(sendNames, '10.10.10.5', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
from telethon import TelegramClient, events


api_id = 21340180
api_hash = 'c9f2ebb3b8619dc3ae88991b33f833c8'



client = TelegramClient("TestSession", api_id, api_hash)


target_can =  -1002404770941


key_words = ["Тривога", "тривоги", "Суми", "Повітряна", "Сумська", "Сумщині"]



@client.on(events.NewMessage(chats=[-1001766138888,  -1001679424866, -1001765605498,  -1002404802004 ]))  # Канали для пошуку
async def normal_handler(event):

    for word in key_words:

        if word in event.message.message:
            print(f"Знайдено повідомлення: {event.message.message}")
            print(f"ID чату/групи: {event.message.peer_id}")


            await client.send_message(target_can, event.message)
            break



client.start()
client.run_until_disconnected()
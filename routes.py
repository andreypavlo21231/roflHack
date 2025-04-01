import asyncio
import websockets
import json
import sys
import asyncio
from database import TextDatabase
from pdf_gen import generate_python_pdf
import random
db_юзеры = TextDatabase("юзеры.txt")
db_имена = TextDatabase("имена.txt")
db_балансы = TextDatabase("балансы.txt")

# if sys.platform.startswith('win'):
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class Сокет_НЕ_ФЛАСКОПОДОБИЕ:
    def __init__(self, хост_ебать_копать_локалке_пизда="localhost", порт_тоже_ахуенный=8765):
        self.хост_ебать_копать_локалке_пизда = хост_ебать_копать_локалке_пизда
        self.порт_тоже_ахуенный = порт_тоже_ахуенный
        self.routes = {}

    def route(self, путь):
        def decorator(func):
            self.routes[путь] = func
            return func
        return decorator

    async def хандлер_вообще_кайфарика_поймал(self, websocket, путь):
        if путь in self.routes:
            try:
                data = await websocket.recv()
                request = json.loads(data) if data else {}
                response = await self.routes[путь](request)
                await websocket.send(json.dumps(response))
            except Exception as e:
                await websocket.send(json.dumps({"error": str(e)}))
        else:
            await websocket.send(json.dumps({"error": "Route not found"}))

    def run(self):
        print(f"Server running on ws://{self.хост_ебать_копать_локалке_пизда}:{self.порт_тоже_ахуенный}")
        сервер_старт = websockets.serve(self.хандлер_вообще_кайфарика_поймал, self.хост_ебать_копать_локалке_пизда, self.порт_тоже_ахуенный)
        asyncio.get_event_loop().run_until_complete(сервер_старт)
        asyncio.get_event_loop().run_forever()

апп = Сокет_НЕ_ФЛАСКОПОДОБИЕ()


@апп.route("/привет")
async def привет(request):
    print('got request')
    name = request.get("name", "Гость")
    return {"message": f"Привет, {name}!"}

@апп.route("/sum")
async def add_numbers(request):
    a, b = request.get("a", 0), request.get("b", 0)
    return {"result": a + b}
@апп.route("/гет_балансе")
async def гет_балансе(request):
    print('got request')
    a, b = request.get("a", 0), request.get("b", 0)
    return 0

@апп.route("/login")
async def login(request):
    try:
        email = request.get("email")
        password = request.get("password")
        stored_password = db_юзеры.get(email)
        name = db_имена.get(email)
        баланс = db_балансы.get(email)
        if stored_password is None:
            return {"error": "Неверные учетные данные"}
        if stored_password == password:
            print({"name": name, "balance":баланс, 'email':email})
            return {"name": name, "balance":баланс, 'email':email}
        else:
            return {"error": "Неверные учетные данные"}
    except Exception as e:
        import traceback
        print("Произошла ошибка:")
        traceback.print_exc()
@апп.route("/change_balance")
async def чендж_балансе(request):
    # balance = request.get("balance", "").strip()
    email = request.get("email", "").strip()
    print(email)
    balance = random.randint(-200,200)
    db_балансы.update(email, int(db_балансы.get(email))+balance)
    return {"message":int(db_балансы.get(email))}

@апп.route("/register")
async def регистрация(request):
    name = request.get("fio", "").strip()
    email = request.get("email", "").strip()
    password = request.get("password", "").strip()
    print(request)
    if not name:
        return {"error": "Имя не может быть пустым, пёс позорный"}
    if not email or not password:
        return {"error": "Email и пароль не могут быть пустыми"}
    if db_юзеры.get(email):
        return {"error": "Этот email уже занят"}
    db_юзеры.insert(email, password)
    db_имена.insert(email, name)
    db_балансы.insert(email, 1000)
    
    return {"message": f"Новая псина зарегистрирована", "account": email}

# @апп.route("/documents")
# async def документы_ебать(request):
    # name = request.get("name", "").strip()
    # if name == 'Лицензия на телепортацию':
        
if __name__ == "__main__":
    апп.run()

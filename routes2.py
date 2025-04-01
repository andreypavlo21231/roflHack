import asyncio
import json
import os
from aiohttp import web
from database import TextDatabase
from pdf_gen import generate_python_pdf,generate_fizra_pdf  # Импорт генерации PDF

db_юзеры = TextDatabase("юзеры.txt")
db_имена = TextDatabase("имена.txt")
db_балансы = TextDatabase("балансы.txt")

async def cors_middleware(app, handler):
    async def middleware_handler(request):
        response = await handler(request)
        response.headers.update({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })
        return response
    return middleware_handler

async def документы_ебать(request):
    if request.method == "OPTIONS":
        return web.Response(status=200, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })

    try:
        data = await request.json()
        name = data.get("name", "").strip()
        fio = data.get("fio", "").strip()

        if not name:
            return web.json_response({"error": "Название документа не указано"}, status=400)

        filename = f"{name}.pdf"
        file_path = f"./generated_docs/{filename}"

        if not os.path.exists("./generated_docs"):
            os.makedirs("./generated_docs")
        if name=="Справка о недееспособности по причине питонист":
            generate_python_pdf(fio, file_path)
        elif name=="Справка от физкультуры":
            generate_fizra_pdf(fio, file_path)
        elif name=="Лицензия на телепортацию":
            generate_python_pdf(fio, file_path)
        elif name=="Диплом Гарварда":
            generate_fizra_pdf(fio, file_path)
        elif name=="Паспорт гражданина Луны":
            generate_python_pdf(fio, file_path)
        elif name=="Разрешение на безделье":
            generate_fizra_pdf(fio, file_path)
        elif name=="Справка о недееспособности по причине питонист":
            generate_python_pdf(fio, file_path)
        
        # elif name==
        if not os.path.exists(file_path):
            return web.json_response({"error": "Ошибка генерации документа"}, status=500)
        elif not os.path.exists(file_path):
            return web.json_response({"error": "Ошибка генерации документа"}, status=500)
        
        return web.FileResponse(file_path, headers={
            "Access-Control-Allow-Origin": "*",
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Content-Type": "application/pdf"
        })

    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application(middlewares=[cors_middleware])
app.router.add_post("/documents", документы_ебать)
app.router.add_options("/documents", документы_ебать)  # Добавляем OPTIONS для CORS

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=8766)

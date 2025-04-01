from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader

def generate_python_pdf(name, filename='output.pdf'):
    data = {
        'name': name,
        'date': '01.04.2025',
        'comment': '''Признаки недееспособности: бессмысленные дебаги, зависания в бесконечных 
циклах и панический страх перед отладчиком. Также наблюдается возможное 
влияние SCP[данные удалены] класса кетор, требуется освидетельствование 
сотрудником фонда''',
    }
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    font_path = 'FreeSerif.ttf'
    pdfmetrics.registerFont(TTFont('FreeSerif', font_path))
    c.setFont("FreeSerif", 12)
    c.setFont("FreeSerif", 16)
    after_line = 100
    c.drawString(100, height - after_line, "Справка о недееспособности по причине питонист")
    after_line += 30
    c.setFont("FreeSerif", 12)
    c.drawString(100, height - after_line, f"Имя: {data['name']}")
    after_line += 30
    c.drawString(100, height - after_line, f"Дата: {data['date']}")
    after_line += 30
    c.drawString(100, height - after_line, "Комментарий:")
    after_line += 30
    for comment in data['comment'].split('\n'):
        c.drawString(100, height - after_line, comment)
        after_line += 15
    c.setStrokeColorRGB(0, 0, 0)
    c.line(100, height - after_line, width - 100, height - after_line)
    after_line += 30
    c.drawString(100, height - after_line, "Рекомендуемые меры: Временно исключить использование Python, а также назначить")
    after_line += 12
    c.drawString(100, height - after_line, "оздоровительные процедуры, а также седативные вещества и дозу амнезиака")
    after_line += 30
    c.drawString(100, height - after_line, "А также, настоятельно рекомендуется пройти курс восстановления продуктивности!")
    
    # Добавление изображений в нижние углы
    try:
        img_a = ImageReader("a.png")
        img_b = ImageReader("b.png")
        img_size = 250  # Размер изображений
        c.drawImage(img_a, width - img_size - 10, 10, img_size, img_size)
        c.drawImage(img_b, 10, 10, img_size, img_size)
    except Exception as e:
        print(f"Ошибка при загрузке изображений: {e}")
    
    c.save()
def generate_fizra_pdf(name, filename='output.pdf'):
    data = {
        'name': name,
        'date': '01.04.2025',
        'comment': '''Не твое собачье дело''',
    }
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    font_path = 'FreeSerif.ttf'
    pdfmetrics.registerFont(TTFont('FreeSerif', font_path))
    c.setFont("FreeSerif", 12)
    c.setFont("FreeSerif", 16)
    after_line = 100
    c.drawString(100, height - after_line, "Справка от физкультуры")
    after_line += 30
    c.setFont("FreeSerif", 12)
    c.drawString(100, height - after_line, f"Имя: {data['name']}")
    after_line += 30
    c.drawString(100, height - after_line, f"Дата: {data['date']}")
    after_line += 30
    c.drawString(100, height - after_line, "Комментарий:")
    after_line += 30
    for comment in data['comment'].split('\n'):
        c.drawString(100, height - after_line, comment)
        after_line += 15
    c.setStrokeColorRGB(0, 0, 0)
    c.line(100, height - after_line, width - 100, height - after_line)
    after_line += 30
    c.drawString(100, height - after_line, "Рекомендуемые меры: Временно убрать нахуй физкультуру.")
    after_line += 12
    c.drawString(100, height - after_line, "ФИЗРУК, ЕПТА, ТЕБЕ ТРЫНДА")
    after_line += 30
    c.drawString(100, height - after_line, "<3!")
    
    # Добавление изображений в нижние углы
    try:
        img_a = ImageReader("a.png")
        img_b = ImageReader("b.png")
        img_size = 250  # Размер изображений
        c.drawImage(img_a, width - img_size - 10, 10, img_size, img_size)
        c.drawImage(img_b, 10, 10, img_size, img_size)
    except Exception as e:
        print(f"Ошибка при загрузке изображений: {e}")
    
    c.save()

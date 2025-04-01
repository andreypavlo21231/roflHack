#А? ЛОБОТОМИЯ!!!!!!
def IF(condition, true_value, false_value):
    return {True: true_value, False: false_value}[bool(condition)]
#А схуяли оно работает? Ну похуй, пусть работает
def DEF(name, params, code):
    func_definition = f"def {name}({params}):\n"
    func_body = "\n".join(f"    {line}" for line in code.split("\n"))
    full_code = func_definition + func_body
    exec(full_code, globals())


#Ахуенно, просто заебись, а теперь иди нахуй
# DEF("hello", "name", "print(f'Привет, {name}!')")
# hello("Мир")

import ollama
from time import sleep

def main():
    print("Вас приветствует...")
    sleep(0.5)
    print("  _                   _____                _ ")
    sleep(0.5)
    print(" | |                 |  __ \              | |")
    sleep(0.5)
    print(" | |     ___  ___ ___| |__) |___  __ _  __| |")
    sleep(0.5)
    print(" | |    / _ \/ __/ __|  _  // _ \/ _` |/ _` |")
    sleep(0.5)
    print(" | |___|  __/\__ \__ \ | \ \  __/ (_| | (_| |")
    sleep(0.5)
    print(" |______\___||___/___/_|  \_\___|\__,_|\__,_|")
    sleep(0.5)
    print("Сначала проверю конфигурацию...")

    llm_list = ollama.list()
    if len(llm_list) < 1:
        print("Ой-ёй! Вы не установили LLM модель для Ollama!")
        print("Попытаюсь это сделать за вас...")
        try:
            ollama.pull('llama3.1:8b')
        except Exception as error:
            print(f"У меня не получилось... Вот ошибка: {error}")
            return
        else:
            print("Успешно скачал llama3.1:8b!")
    print("Всё хорошо!")
    step_2()

def step_2():
    print("=========================================================================")
    print("Какой режим сокращения пожелаете? Для выбора впишите ТОЛЬКО нужную цифру!")
    print("[1]. До двух предложений")
    print("[2]. Сократить до абзаца")
    mode = input("Ваш выбор: ")
    if str(mode) == "1" or mode == "2":
        step_3(mode)
    else:
        print("Извините, вы ввели не цифру. Введите ТОЛЬКО цифру режима!")
        step_2()
        return

def step_3(mode):
    print("=========================================================================")
    print("Отлично! Теперь введите текст, который хотите сократить.")
    text = input("Ваш текст: ")
    if len(text) < 5:
        print("Это слишком маленький текст! Нужен текст по объёмнее.")
        step_3(mode)
        return
    else:
        print("Начинаю генерацию текста!")
        shorten_text(mode, text)

def shorten_text(mode, text):
    print("=========================================================================")
    prompt = ""
    if mode == "1":
        prompt = ("Task: Shorten this text to two sentences using the language of the text. Don't output anything, but shorten text\n"
                  f"Text: {text}")
    elif mode == "2":
        prompt = ("Task: Shorten this text using the language of the text. Don't output anything, but shorten text\n"
                  f"Text: {text}")
    else:
        print("Выбран неправильный режим...")
    stream = ollama.chat(
        model='llama3.1:8b',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    print("\n=========================================================================")
    print("Желаете повторить? Да/Нет")
    restart = input("Ваш ответ: ")
    if restart.lower() == 'да':
        step_2()
    elif restart.lower() == 'нет':
        print("Спасибо что воспользовались LessRead™!")
        return
    else:
        return

if __name__ == '__main__':
    main()
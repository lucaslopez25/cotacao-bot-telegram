from datetime import datetime

def generic_answers(input_text):
    user_message = str(input_text).lower()

    if user_message in ("start", "inicie", "inicio"):
        return "O bot está iniciando..."

    if user_message in ("Que horas são?", "que horas são?", "que horas sao", "que horas sao?", "Que horas são", "que horas são", "horas", "horario"):
        agora = datetime.now()
        horario = agora.strftime("Agora: %H:%M \n" + "%d/%m/%y")

        return str(horario)

    return "Não entendi... Tente novamente!"

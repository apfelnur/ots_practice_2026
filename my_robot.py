import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":

        if True:
            state = "RIGHT"
            t.setheading(0)  # Разворот вправо
            turn = 1  # Старт с первого прохода
            num_turns = 5  # Задать число проходов
            return state, turn
        return state, turn
    if state == "RIGHT":
        t.forward(10)  # Перемещение

        if x >= 3 and turn < num_turns:
            state = "DOWN_R"
            t.setheading(270)  # Разворот вниз
            return state, turn
        if x >= 3 and turn >= num_turns:
            state = "STOP"
            return state, turn
        return state, turn
    if state == "DOWN_R":
        t.forward(10)  # Перемещение

        if y <= 1 - turn:
            state = "LEFT"
            t.setheading(180)  # Разворот влево
            turn = turn + 1  # Следующая строка
            return state, turn
        return state, turn
    if state == "LEFT":
        t.forward(10)  # Перемещение

        if x <= 1:
            state = "DOWN_L"
            t.setheading(270)  # Разворот вниз
            return state, turn
        return state, turn
    if state == "DOWN_L":
        t.forward(10)  # Перемещение

        if y <= 1 - turn:
            state = "RIGHT"
            t.setheading(0)  # Разворот вправо
            turn = turn + 1  # Следующая строка
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()
from bakery import assert_equal
from dataclasses import dataclass
from drafter import *

@dataclass
class State:
    """
    The current state of the calculator.
    """
    first_digit: str
    second_digit: str
    answer_history: list[str]
    valid_input: bool
    result: str
    
@route
def index(state: State) -> Page:
    """
    This is the home page of the calculator where the user can choose the type of operator
    they would like to use
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: a varying page depending on the type of operator chosen
    """
    return Page(state, [
        "Welcome to Colin's Calculator!",
        Image("Math Operations.png"),
        "Input your first number",
        TextBox("first", state.first_digit),
        "Input your second number",
        TextBox("second", state.second_digit),
        "What operator would you like to use?",
        Button("Addition", add_page),
        Button("Subtraction", subtraction_page),
        Button("Multiplication", multiply_page),
        Button("Division", division_page),
        Button("Modulo", modulo_page),
        Button("Exponential", exponent_page)
        ])

@route
def add_page(state: State, first: str, second: str) -> Page:
    """
    The add page will appear when the user clicks the addition button on the index page
    and it will add together 2 numbers that the user inputs. If the user does not input a
    number, it will bring the user to the invalid input page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) + int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])

@route
def subtraction_page(state: State, first: str, second: str) -> Page:
    """
    The subtraction page will appear when the user clicks the subtraction button on the
    index page and it will subtract the 2 numbers that the user inputs. If the user does not
    input a number, it will bring the user to the invalid input page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) - int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])

@route
def multiply_page(state: State, first: str, second: str) -> Page:
    """
    The multiply page will appear when the user clicks the multiplication button on the
    index page and it will multiply the 2 numbers that the user inputs. If the user does not
    input a number, it will bring the user to the invalid input page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) * int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])

@route
def division_page(state: State, first: str, second: str) -> Page:
    """
    The division page will appear when the user clicks the division button on the
    index page and it will divide the 2 numbers that the user inputs. If the user does not
    input a number, it will bring the user to the invalid input page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) / int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])
    
@route
def modulo_page(state: State, first: str, second: str) -> Page:
    """
    The modulo page will appear when the user clicks the modulo button on the
    index page and it take the first number input modulo the second number input.
    If the user does not input a number, it will bring the user to the invalid input page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) % int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])
    
@route
def exponent_page(state: State, first: str, second: str) -> Page:
    """
    The exponent page will appear when the user clicks the exponetial button on the
    index page and it will take the first number input to the power of the second number
    input. If the user does not input a number, it will bring the user to the invalid input
    page.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem, the
        invalid input page if the user does not input numbers, or the get_history page
        if the user clicks the answer history button
    """
    if first.isdigit() and second.isdigit():
        state.result = str(int(first) ** int(second))
        state.answer_history.append(state.result)
    else:
        state.valid_input = False
        return invalid(state)
    return Page(state, [
        "The answer is: " + state.result,
        Button("View Answer History", get_history),
        Button("Restart here", index)
        ])

@route
def get_history(state: State) -> Page:
    """
    The get_history page will appear when the user clicks the answer history button
    after completing a math problem and shows the user all of their past answers that
    they had computed.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem
    """
    history = ""
    for answer in state.answer_history:
        history += answer + ", "
    return Page(state, [
        "Your answer history is: " + history,
        Button("Restart here", index)
        ])

@route
def invalid(state: State) -> Page:
    """
    The invalid page will appear with an error message when the user inputs anything
    other than numbers into the first or second number of the state and remind the
    user that they can only input numbers.
    
    Args:
        state (State): the current state of the calculator
    Returns:
        Page: returns the user to the index page to compute another math problem
    """
    return Page(state, [
        "Invalid Input! You may only input numbers. Try Again.",
        Image("error.png"),
        Button("Retry", index)
        ])

start_server(State("", "", [], True, ""))

assert_equal(
 get_history(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2'], valid_input=True, result='0.2')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2'],
                 valid_input=True,
                 result='0.2'),
     content=['Your answer history is: 9, 1, 72, 0.2, ', Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1'], valid_input=True, result='1')),
 Page(state=State(first_digit='', second_digit='', answer_history=['9', '1'], valid_input=True, result='1'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=[], valid_input=True, result='')),
 Page(state=State(first_digit='', second_digit='', answer_history=[], valid_input=True, result=''),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2'], valid_input=True, result='0.2')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2'],
                 valid_input=True,
                 result='0.2'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 get_history(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0', '1156'], valid_input=True, result='1156')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0', '1156'],
                 valid_input=True,
                 result='1156'),
     content=['Your answer history is: 9, 1, 72, 0.2, 0, 1156, ', Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0', '1156'], valid_input=True, result='1156')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0', '1156'],
                 valid_input=True,
                 result='1156'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 add_page(State(first_digit='', second_digit='', answer_history=[], valid_input=True, result=''), '4', '5'),
 Page(state=State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9'),
     content=['The answer is: 9',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))

assert_equal(
 division_page(State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72'), '3', '15'),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2'],
                 valid_input=True,
                 result='0.2'),
     content=['The answer is: 0.2',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0', '1156'], valid_input=False, result='1156')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0', '1156'],
                 valid_input=False,
                 result='1156'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 exponent_page(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0'], valid_input=True, result='0'), '34', '2'),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0', '1156'],
                 valid_input=True,
                 result='1156'),
     content=['The answer is: 1156',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))

assert_equal(
 add_page(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0', '1156'], valid_input=True, result='1156'), 'number', '2'),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0', '1156'],
                 valid_input=False,
                 result='1156'),
     content=['Invalid Input! You may only input numbers. Try Again.',
              Image(url='error.png', width=None, height=None),
              Button(text='Retry', url='/')]))

assert_equal(
 get_history(State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9')),
 Page(state=State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9'),
     content=['Your answer history is: 9, ', Button(text='Restart here', url='/')]))

assert_equal(
 modulo_page(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2'], valid_input=True, result='0.2'), '9', '9'),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0'],
                 valid_input=True,
                 result='0'),
     content=['The answer is: 0',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1', '72', '0.2', '0'], valid_input=True, result='0')),
 Page(state=State(first_digit='',
                 second_digit='',
                 answer_history=['9', '1', '72', '0.2', '0'],
                 valid_input=True,
                 result='0'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 multiply_page(State(first_digit='', second_digit='', answer_history=['9', '1'], valid_input=True, result='1'), '8', '9'),
 Page(state=State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72'),
     content=['The answer is: 72',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9')),
 Page(state=State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 get_history(State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72')),
 Page(state=State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72'),
     content=['Your answer history is: 9, 1, 72, ', Button(text='Restart here', url='/')]))

assert_equal(
 index(State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72')),
 Page(state=State(first_digit='', second_digit='', answer_history=['9', '1', '72'], valid_input=True, result='72'),
     content=["Welcome to Colin's Calculator!",
              Image(url='Math Operations.png', width=None, height=None),
              'Input your first number',
              TextBox(name='first', kind='text', default_value=''),
              'Input your second number',
              TextBox(name='second', kind='text', default_value=''),
              'What operator would you like to use?',
              Button(text='Addition', url='/add_page'),
              Button(text='Subtraction', url='/subtraction_page'),
              Button(text='Multiplication', url='/multiply_page'),
              Button(text='Division', url='/division_page'),
              Button(text='Modulo', url='/modulo_page'),
              Button(text='Exponential', url='/exponent_page')]))

assert_equal(
 subtraction_page(State(first_digit='', second_digit='', answer_history=['9'], valid_input=True, result='9'), '5', '4'),
 Page(state=State(first_digit='', second_digit='', answer_history=['9', '1'], valid_input=True, result='1'),
     content=['The answer is: 1',
              Button(text='View Answer History', url='/get_history'),
              Button(text='Restart here', url='/')]))
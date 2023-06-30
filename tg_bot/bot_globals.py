'''
Various globals
'''
import datetime as dt

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


# some constants
CURRENT_STATE, INPUT_STEP, LAST_STEP, INPUT_DATA = range(100, 104)


# only stages
WAIT_FOR_BUTTONS, INPUT_USER_INFO = map(chr, range(2))


# callback button data base name (and some of them are stages also - see main())
SEE_EVENTS, SEE_FUTURE_EVENTS, BOT_INFO, NEW_EVENT, BROADCAST, \
QUESTIONS, SEE_PROGRAM, WHO_DONATED, NEW_CONTACT, NEXT_PERSON, IM_HERE, OTHER_EVENTS, \
NOTIFY, WANT_TO_SPEAK, ACCEPT_SPEAKER, DECLINE_SPEAKER, CHANGE_PROGRAM, \
ASK_QUESTION, SPEAKER_INFO, ADD_SPEAKER, CANCEL_INPUT, ANSWER_QUESTION, DONATE, \
DO_NOT_DONATE, SEE_QUESTIONS, FURTHER_EVENT_ACTIONS, CANCEL_INPUT, _ = map(chr, range(2, 30))


# input steps for handling user input step by step with type checking
input_steps = {
    NEW_EVENT:{
        'last_step':3,
        0:('Введите тему митапа', str),
        1:('Введите описание бота', str),
        2:('Введите дату начала', dt.date.fromisoformat),
        3:('Введите дату окончания', dt.date.fromisoformat)
    }
}

# keyboards with static callback data
KEYBOARD_START_ORGANIZER =[
    [
        InlineKeyboardButton("Мероприятия", callback_data=SEE_EVENTS),
        InlineKeyboardButton("О боте", callback_data=BOT_INFO),
    ],
    [
        InlineKeyboardButton("Новый митап", callback_data=NEW_EVENT),
        InlineKeyboardButton("Рассылка", callback_data=BROADCAST),
    ],
    [InlineKeyboardButton("Вопросы к докладу", callback_data=SEE_QUESTIONS)]
]

KEYBOARD_START_USUAL =[
    [
        InlineKeyboardButton("Мероприятия", callback_data=SEE_EVENTS),
        InlineKeyboardButton("О боте", callback_data=BOT_INFO),
    ],
    [InlineKeyboardButton("Вопросы к докладу", callback_data=SEE_QUESTIONS)]
]

# Cancel button for cancelling input
CANCEL_MARKUP = InlineKeyboardMarkup.from_button(InlineKeyboardButton('Отмена', callback_data=CANCEL_INPUT))


# help inforamtion (now used as a plug for not finished functions)
help_info ={
    SEE_QUESTIONS: 'Показываем вопросы к докладу пользователя',
}

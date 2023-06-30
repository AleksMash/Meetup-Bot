from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext,
                          ConversationHandler, CallbackQueryHandler)

# import alex_db as db
# from avm_env import BOT_TOKEN
import db
import bot_globals as bg


def plug_function(update: Update, context: CallbackContext):
    pass


def start(update: Update, context: CallbackContext):
    '''starting procedure: shows main menu'''
    if db.user_is_organizer(update.message.from_user.id):
        reply_markup = InlineKeyboardMarkup(bg.KEYBOARD_START_ORGANIZER)
    else:
        reply_markup = InlineKeyboardMarkup(bg.KEYBOARD_START_USUAL)

    update.message.reply_text("Главное меню", reply_markup=reply_markup)
    return bg.WAIT_FOR_BUTTONS


def about_bot(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.reply_text('Информация о боте')


def show_current_events(update: Update, context: CallbackContext):
    """
    Показывает список мероприятий отдельными сообщениями.
    В первую очередь показывает текущие мероприятия, если они есть и последним сообщением дается вохможность
    также посмотреть запланированные
    """
    query = update.callback_query
    query.answer()
    current_events = db.get_current_events()
    keyboard = [[InlineKeyboardButton("Показать", callback_data=bg.SEE_FUTURE_EVENTS)]]
    reply_markup_upcoming = InlineKeyboardMarkup(keyboard)
    if current_events:
        update.message.reply_text('⌚ Текущие события ⌚')

        for event in current_events:
            keyboard = [
                [InlineKeyboardButton('Действия...', callback_data=f'{bg.FURTHER_EVENT_ACTIONS}:{event["id"]}')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(event['description'], reply_markup=reply_markup)
        query.message.reply_text("Можно также посмотреть запланированные", reply_markup=reply_markup_upcoming)

    else:
        query.message.reply_text("Текущих мероприятий нет, но можно посмотреть "
                                  "запланированные ", reply_markup=reply_markup_upcoming)

    return bg.WAIT_FOR_BUTTONS


def show_future_events(update: Update, context: CallbackContext):
    """
    Показывает список мероприятий отдельными сообщениями.
    В первую очередь показывает текущие мероприятия, если они есть и последним сообщением дается вохможность
    также посмотреть запланированные
    """
    query = update.callback_query
    query.answer()
    future_events = db.get_upcoming_events()
    # keyboard = [[InlineKeyboardButton("Показать", callback_data=bg.SEE_FUTURE_EVENTS)]]
    # reply_markup_upcoming = InlineKeyboardMarkup(keyboard)
    if future_events:
        query.message.reply_text('⌚ Запланированные события ⌚')

        for event in future_events:
            keyboard = [
                [InlineKeyboardButton('Действия...', callback_data=f'{bg.FURTHER_EVENT_ACTIONS}:{event["id"]}')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            query.message.reply_text(event['title'], reply_markup=reply_markup)
    else:
        query.message.reply_text("Запланированных мероприятий нет")

    return bg.WAIT_FOR_BUTTONS


def event_actions_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.reply_text('Показываем меню кнопок для мероприятия')
    return bg.WAIT_FOR_BUTTONS


def schedule_new_event(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    context.user_data[bg.CURRENT_STATE] = bg.NEW_EVENT
    context.user_data[bg.INPUT_STEP] = 0
    context.user_data[bg.INPUT_DATA]=[]
    msg_text = bg.input_steps[bg.NEW_EVENT][0][0]
    query.message.reply_text(msg_text, reply_markup=bg.CANCEL_MARKUP)
    return bg.NEW_EVENT


def get_event_input(update: Update, context: CallbackContext):
    msg_text, checker = bg.input_steps[bg.NEW_EVENT][context.user_data[bg.INPUT_STEP]]
    if not checker is str:
        try:
            input_checked = checker(update.message.text)
        except (ValueError, TypeError):
            update.message.reply_text('Вы ввели неверное значение./n' + msg_text, reply_markup=bg.CANCEL_MARKUP)
            return bg.NEW_EVENT
    else:
        input_checked = update.message.text

    context.user_data[bg.INPUT_DATA].append(input_checked)
    cur_step = context.user_data[bg.INPUT_STEP]

    if not cur_step == bg.input_steps[bg.NEW_EVENT]['last_step']:
        cur_step += 1
        context.user_data[bg.INPUT_STEP] = cur_step
        msg_text = bg.input_steps[bg.NEW_EVENT][cur_step][0]
        update.message.reply_text(msg_text, reply_markup=bg.CANCEL_MARKUP)
        return bg.NEW_EVENT

    # we've got all input data. Now we can save it in DB
    # todo saving new event in DB
    reply_murkup = InlineKeyboardMarkup.from_button(InlineKeyboardButton('Оповестить', callback_data=bg.NOTIFY))
    update.message.reply_text('Новый митап создан!.\n/start - главное меню', reply_markup=reply_murkup)
    context.user_data[bg.CURRENT_STATE] = None
    context.user_data[bg.INPUT_STEP] = None
    context.user_data[bg.INPUT_DATA] = None


def cancel_input(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    context.user_data[bg.CURRENT_STATE] = None
    context.user_data[bg.INPUT_STEP] = None
    context.user_data[bg.INPUT_DATA] = None
    query.message.reply_text('Действие отменено. \n /Start - для перехода в главное меню')
    return bg.WAIT_FOR_BUTTONS


def show_questions(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.reply_text('показываем вопросы к докладу пользователя')
    return bg.WAIT_FOR_BUTTONS


def broadcast_meassage(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.message.reply_text('Запрашиваем данные для рассылки и запускаем ее')
    return bg.WAIT_FOR_BUTTONS


def main():
    # current_date = datetime.now().date()
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    cancel_button_handler = CallbackQueryHandler(cancel_input, pattern=bg.CANCEL_INPUT)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            bg.WAIT_FOR_BUTTONS: [
                CallbackQueryHandler(show_current_events, pattern=bg.SEE_EVENTS),
                CallbackQueryHandler(show_future_events, pattern=bg.SEE_FUTURE_EVENTS),
                CallbackQueryHandler(schedule_new_event, pattern=bg.NEW_EVENT),
                CallbackQueryHandler(about_bot, pattern=bg.BOT_INFO),
                CallbackQueryHandler(show_questions, pattern=bg.SEE_QUESTIONS),
                CallbackQueryHandler(event_actions_menu, pattern=bg.FURTHER_EVENT_ACTIONS),
                CallbackQueryHandler(broadcast_meassage, pattern=bg.BROADCAST)
            ],
            bg.NEW_EVENT: [
                MessageHandler(filters=None, callback=get_event_input),
                cancel_button_handler
            ]
        },
        fallbacks=[CommandHandler('start', start)],
        per_user=True
    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()

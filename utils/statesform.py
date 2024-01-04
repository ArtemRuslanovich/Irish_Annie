from aiogram.fsm.state import StatesGroup, State

class StatesForm(StatesGroup):
    get_settings = State()
    get_start = State()
    get_customer = State()
    get_profile = State()
    get_info = State()
    get_bot_settings = State()
    get_credits = State()



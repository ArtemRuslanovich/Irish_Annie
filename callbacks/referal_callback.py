from aiogram.types import CallbackQuery
from utils.dbconnect import Request
from keyboards.inline import info_keyboard


async def generate_referral_link(user_id):
    # Создание уникальной реферальной ссылки для пользователя
    referral_link = f'https://t.me/alisa_test2_bot?start=referral_{user_id}'
    return referral_link

async def referal_system(callback: CallbackQuery, request: Request):
    user_id = callback.from_user.id
    
    # Создание реферальной ссылки
    referral_link = await generate_referral_link(user_id)
    
    # Отправка сообщения с информацией о реферальной системе
    await callback.message.edit_text(
    f'Our personal invitation message ⤵️\n\n'
    f'Your referral link:\n{referral_link}\n\n'
    f'🤝 EARN WITH US\n'
    f'Earn 200 credits for every purchase made by users you invite. '
    f'Earned credits can be exchanged for rewards.\n\n'
    f'Forward your invitation message to your friends – it contains your unique referral code.\n\n'
    f'Do you have a significant reach (community, website with traffic) and want to become an affiliate? '
    f'Contact @irishanniecom.', reply_markup=info_keyboard
)

    # Проверка наличия реферера в ссылке
    if callback.data.startswith('referral_'):
        referral_user_id = int(callback.data.replace('referral_', ''))
        
        # Начисление бонусных кредитов рефереру
        await request.add_bonus_credits(referral_user_id, 200)
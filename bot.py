from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from btn import menu


class ToAdminState(StatesGroup):
    text=State()
    name=State()
    surname=State()
    phone_num=State()
    adres=State()
    photo=State()
    photo_ozi=State()




api = ''
bot = Bot(api)
dp=Dispatcher()



@dp.message(Command('start'))
async def send_salem (sms:types.Message):
    await sms.answer(text=f'salem{sms.from_user.first_name}',
                     reply_markup=menu)


@dp.message(F.text=='registration')
@dp.message(Command('registration'))
async def start_to_admin(sms:types.Message,state:FSMContext):
    await sms.answer(text='''yaxshi endi bizga malumat zazasizba
                     ava dep jazing''')
    await state.set_state(ToAdminState.text)



async def save_text(sms: types.Message, state: FSMContext):
    await sms.answer(text='name:')
    await state.update_data(regis=sms.text)
    await state.set_state(ToAdminState.name)

    await state.clear()



@dp.message(ToAdminState.text)
async def save_text(sms: types.Message, state: FSMContext):
    await sms.answer(text='surname:')
    await state.update_data(regis=sms.text)
    await state.set_state(ToAdminState.surname)

    await state.clear()


@dp.message(ToAdminState.text)
async def save_text(sms: types.Message, state: FSMContext):
    await sms.answer(text='Phone number:')
    await state.update_data(regis=sms.text)
    await state.set_state(ToAdminState.phone_num)

    await state.clear()


@dp.message(ToAdminState.text)
async def save_text(sms: types.Message, state: FSMContext):
    await sms.answer(text='adres:')
    await state.update_data(regis=sms.text)
    await state.set_state(ToAdminState.adres)

    await state.clear()


@dp.message(ToAdminState.text)
async def save_text(sms: types.Message, state: FSMContext):
    await sms.answer(text='photo jibere sizba:')
    await state.update_data(regis=sms.text)
    await state.set_state(ToAdminState.photo)

@dp.message(ToAdminState.photo)
async def video(sms: types.Message, state: FSMContext):
    if sms.text == "Yaq":
        datas = await state.get_data()

        await bot.send_message(
            chat_id=6884134121,
            text=f'''Bu malumot  - @{sms.from_user.username}
tarafindan keldi ----{datas['regis']}'''
        )
        await state.clear()

    elif sms.text == "Awa":
        await sms.answer(text='surat yuboring:')
        await state.set_state(ToAdminState.photo_ozi)

@dp.message(ToAdminState.photo_ozi)
async def send_full(sms: types.Message, state: FSMContext):
    await state.update_data(photo=sms.photo[0].file_id)
    await sms.answer(text='habar yuborildi')
    datas = await state.get_data()


    await state.clear()










async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())    
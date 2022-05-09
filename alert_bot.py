import aiogram.utils.markdown as fmt
import asyncio
import sys

from os import getenv
from typing import List
from loguru import logger
from util.db_loader import load_db, TonPunk
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from purchases_checker_bot import TonPunkPurchaseChecker

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)

TONNFT_DB: List[TonPunk] = load_db()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    """
    Main application
    Streaming new purchases TON PUNKS NFTs
    """
    await message.answer('Start streaming new purchases TON PUNKS NFTs')


async def streaming_of_purchased_nfts() -> None:
    """
    Main application
    Streaming new purchases TON PUNKS NFTs
    """

    checker = TonPunkPurchaseChecker()

    logger.info('Start streaming new purchases TON PUNKS NFTs')

    while True:
        try:
            await checker.gather_data(False) \
                if not checker.previous_ton_punks_state \
                else await checker.gather_data(True)

            if not checker.current_ton_punks_state:
                await checker.gather_data(True)
        except Exception as e:
            logger.error(e)
            logger.info('Reset csrf token')

            checker.config.reset_csrf()

            checker.previous_ton_punks_state = checker.backup_ton_punks_state
            checker.current_ton_punks_state = []

            continue

        checker.previous_ton_punks_state = sorted(checker.previous_ton_punks_state, key=lambda punk: punk.name)
        checker.current_ton_punks_state = sorted(checker.current_ton_punks_state, key=lambda punk: punk.name)

        purchases_ton_punks = checker.get_purchased_nfts()

        checker.previous_ton_punks_state = checker.current_ton_punks_state
        checker.backup_ton_punks_state = checker.previous_ton_punks_state
        checker.current_ton_punks_state = []

        if purchases_ton_punks:
            logger.info(f'Sending {len(purchases_ton_punks)} new purchases TON PUNKS to channel')

            [
                await bot.send_message(
                    getenv('CHAT_ID'),
                    fmt.text(
                        fmt.bold(disintar_punk.name),
                        fmt.text(f'{fmt.bold(disintar_punk.price)} 💎 '
                                 f'{fmt.link("BUY", "https://beta.disintar.io/object/" + disintar_punk.address)}'),
                        fmt.text(f'Rating rank: {fmt.bold(tonnft_punk.rating_rank)} / 5149'),
                        fmt.text(f'Rarity score: {fmt.bold(tonnft_punk.rarity_score)}'),
                        sep='\n'
                    ), parse_mode=types.ParseMode.MARKDOWN_V2)
                for disintar_punk in purchases_ton_punks
                for tonnft_punk in TONNFT_DB
                if disintar_punk.name == tonnft_punk.name
            ]


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(streaming_of_purchased_nfts())
    executor.start_polling(dp, skip_updates=True)

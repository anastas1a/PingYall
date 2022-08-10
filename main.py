from misc import dp, app

import handlers


async def start_up():
    async with app:
        await dp.start_polling()


def cli():
    try:
        app.run(start_up())
    except:
        ...

cli()

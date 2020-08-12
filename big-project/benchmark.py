import time
import random
import asyncio
from string import ascii_letters

import httpx


async def test_app(app):
    async with httpx.AsyncClient(
        app=app, base_url="http://testserver/"
    ) as client:  # type: httpx.AsyncClient
        start_time = time.time_ns()

        for _ in range(10000):
            name = "".join(
                [random.choice(ascii_letters) for _ in range(random.randint(1, 50))]
            )
            resp = await client.get("/hi/" + name)
            assert resp.text == f"hi {name}", (name, resp.text)

        end_time = time.time_ns()
    print(app.__class__.__name__, (end_time - start_time) / 1000 ** 3)


def apps():
    from indexpy_example import app

    yield app
    from fastapi_example import app

    yield app
    from quart_example import app

    yield app


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    for app in apps():
        loop.run_until_complete(test_app(app))

import asyncio

class AsyncTimer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()
        await self._job()

    def cancel(self):
        self._task.cancel()

    @interval.setter
    def interval(self, seconds):
        self._timeout = seconds

    @interval.getter
    def interval(self):
        return self._timeout

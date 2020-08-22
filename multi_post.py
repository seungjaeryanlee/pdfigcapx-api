"""
Send POST requests concurrently to PDFigCapX and save HTML response.

There should be `data/html/` and `data/pdf/` directory created.

Install aiohttp with `pip install aiohttp aiodns cchardet`.
"""
import asyncio
import aiohttp
import time


async def fetch(session, paper_id):
    async with session.post("https://www.eecis.udel.edu/~compbio/PDFigCapX/uploader", data={"file": open(f"data/pdf/{paper_id}.pdf", "rb")}) as resp:
        if resp.status != 200:
            print(f"{paper_id} failed.")
        return paper_id, await resp.text()
        # Catch HTTP errors/exceptions here

async def fetch_concurrent(paper_ids):
    loop = asyncio.get_event_loop()
    connector = aiohttp.TCPConnector(limit=50)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for paper_id in paper_ids:
            tasks.append(loop.create_task(fetch(session, paper_id)))

        for result in asyncio.as_completed(tasks):
            paper_id, page = await result
            with open(f"data/html/{paper_id}.html", "w") as f:
                f.write(page)
            print(f"{paper_id} finished.")


start_time = time.time()
paper_ids = ["1806.01363", "1904.00956"]
asyncio.run(fetch_concurrent(paper_ids))
print(f"Finished in {time.time() - start_time:.2f} seconds.")

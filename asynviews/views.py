from django.http import HttpResponse
import asyncio
import httpx

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

# View assíncrona que será chamada pela URL
async def minha_view(request):
    await http_call_async()
    return HttpResponse("Requisição assíncrona feita.")

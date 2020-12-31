import uasyncio

# async def blink(value):
#     while True:
#         print(value)
#         await uasyncio.sleep_ms(value)

# async def main():
#     await uasyncio.gather(blink(400),blink(700))
# Running on a generic board
uasyncio.run(main())
import asyncio


async def async_hello_name(name):
    print(f"hello {name}")
    await asyncio.sleep(5)
    print(f"Stopped {name} !!")


async def main():
    # await async_hello_name("tom")  # same as async_hello_name("tom").send(None)
    # await async_hello_name("Jerry")  # same as async_hello_name("tom").send(None)
    # await async_hello_name("Max")  # same as async_hello_name("tom").send(None)
    await asyncio.gather(
        async_hello_name("Tom"), async_hello_name("Jerry"), async_hello_name("Max")
    )


# m_obj = main()
# m_obj.send(None)
# k_gen_obj = is_kan()
# k_gen_obj.send(None)

# asyncio.run(async_hello_name("Tom"))
asyncio.run(main())

# k_gen_obj.send("ksdhkfh sjdhfkhsdkh k dskjhfkhkh sdk khjskdjh fhkj ksdhj")

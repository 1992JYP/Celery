import time

def hello():
    time.sleep(1)
    print('hello')

def main():
    for _ in range(3):
        hello()

print(f'start : {time.strftime("%X")}')
main()
print(f'  end : {time.strftime("%X")}')

########
# 내가 그동안 해왔던 코드들의 예시가 위의 것이다. 항상 순차적으로 진행시켰다.



import time
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("hello")


async def main():
    await asyncio.gather(
        hello(),
        hello(),
        hello()
    )

print(f'start : {time.strftime("%X")}')
## asyncio 없이 main()하면
# main이 await 되지 않아서 실행이 안된다고 하고
# 프로그램 종료가 아니고 아래 end는 또 진행됨 이건 신기하네
asyncio.run(main())
print(f'  end : {time.strftime("%X")}')
import simpy


def example_sim():
    env = simpy.Environment()
    env.process(traffic_light(env))
    env.run(until=120)
    print("Simulation ended")


def traffic_light(env):
    while(True):
        print("Light turned GREEN at t= "+str(env.now))
        yield env.timeout(30)
        print("Light turned YELLOW at t= "+str(env.now))
        yield env.timeout(5)
        print("Light turned RED at t= "+str(env.now))
        yield env.timeout(10)

def example_gen():
    for i in range(10):
        yield i
def example_func():
    for i in range(10):
        return i
# output_func=example_func()
# output_gen= example_gen()
print(output_func)

print(next(output_gen))

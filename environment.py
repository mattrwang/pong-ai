import retro

def create_env():
    env = retro.make(game='Pong-Atari2600')
    return env
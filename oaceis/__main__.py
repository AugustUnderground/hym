import sys

from flask import Flask, request, abort

from oaceis import ac
from oaceis import gc

GPL_NOTICE = f"""
PRECEPT Copyright (C) 2021 Electronics & Drives
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""

def handle_response(res):
    if isinstance(res, int):
        abort(res)
    elif res is None:
        abort(400)
    else:
        return res

def gace():
    args = gc.parser.parse_args()
    env_id, pdk, var, num, host, port = \
            [ getattr(args, a) for a in
              ["env", "pdk", "var", "num", "host", "port"]]

    env = gc.make_env(env_id, pdk, var, num)

    route = f'{env_id}-{pdk}-v{var}'

    app = Flask("__main__")

    @app.route(f'/{route}/current_performance', methods=['GET'])
    def current_performance():
        res = gc.current_performance(env)
        return handle_response(res)

    @app.route(f'/{route}/step', methods=['POST'])
    def step():
        res = gc.step(env, request.json)
        return handle_response(res)

    @app.route(f'/{route}/reset', methods=['GET'])
    def reset():
        res = gc.reset(env)
        return handle_response(res)

    @app.route(f'/{route}/target', methods=['GET'])
    def target():
        res = gc.target(env)
        return handle_response(res)

    @app.route(f'/{route}/action_space', methods=['GET'])
    def action_space():
        res = gc.action_space(env)
        return handle_response(res)

    @app.route(f'/{route}/observation_space', methods=['GET'])
    def observation_space():
        res = gc.observation_space(env)
        return handle_response(res)

    @app.route(f'/{route}/observation_keys', methods=['GET'])
    def observation_keys():
        res = gc.observation_keys(env)
        return handle_response(res)

    @app.route(f'/{route}/random_action', methods=['GET'])
    def random_action():
        res = gc.random_action(env)
        return handle_response(res)

    @app.route(f'/{route}/random_step', methods=['GET'])
    def random_step():
        res = gc.random_step(env)
        return handle_response(res)

    print(f"Launching GACE Server. Access at http://{host}:{port}/{route}/")
    return app.run(host = host, port = port)

def ace():
    args = ac.parser.parse_args()

    env_id, pdk, num, host, port = \
            [ getattr(args, a) for a in
              ["env", "pdk", "num", "host", "port"]]

    env = ac.make_env(env_id, pdk, num)

    route = f'{env_id}-{pdk}'

    app = Flask("__main__")

    @app.route(f'/{route}/simulate', methods=['POST'])
    def simulate():
        res = ac.simulate(env, request.json)
        return handle_response(res)

    @app.route(f'/{route}/performance', methods=['GET'])
    def performance():
        res = ac.performance(env)
        return handle_response(res)

    @app.route(f'/{route}/sizing', methods=['GET'])
    def sizing():
        res = ac.sizing(env)
        return handle_response(res)

    @app.route(f'/{route}/p-params', methods=['GET'])
    def performance_parameters():
        res = ac.performance_parameters(env)
        return handle_response(res)

    @app.route(f'/{route}/s-params', methods=['GET'])
    def sizing_parameters():
        res = ac.sizing_parameters(env)
        return handle_response(res)

    @app.route(f'/{route}/init', methods=['GET'])
    def initial_sizing():
        res = ac.initial_sizing(env)
        return handle_response(res)

    @app.route(f'/{route}/rng', methods=['GET'])
    def random_sizing():
        res = ac.random_sizing(env)
        return handle_response(res)

    print(f"Launching HACE Server. Access at http://{host}:{port}/{route}/")
    return app.run(host = host, port = port)

def main():
    print(GPL_NOTICE)
    return 0

if __name__ == '__main__':
    sys.exit(main())

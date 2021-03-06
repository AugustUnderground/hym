import sys

from flask import Flask, request, abort

from hym import ac
from hym import gc
from hym import gm

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

def gym():
    args = gm.parser.parse_args()
    env_id, var, num, host, port = [ getattr(args, a) for a in
                                     ["env", "var", "num", "host", "port"] ]

    env = gm.make_env(env_id, var, num)

    route = f'{env_id}-v{var}'

    app = Flask("__main__")

    @app.route(f'/{route}/step', methods=['POST'])
    def step():
        res = gm.step(env, request.json)
        return handle_response(res)

    @app.route(f'/{route}/reset', methods=['GET'])
    def reset():
        res = gm.reset(env)
        return handle_response(res)

    @app.route(f'/{route}/action_space', methods=['GET'])
    def action_space():
        res = gm.action_space(env)
        return handle_response(res)

    @app.route(f'/{route}/observation_space', methods=['GET'])
    def observation_space():
        res = gm.observation_space(env)
        return handle_response(res)

    @app.route(f'/{route}/random_action', methods=['GET'])
    def random_action():
        res = gm.random_action(env)
        return handle_response(res)

    @app.route(f'/{route}/random_step', methods=['GET'])
    def random_step():
        res = gm.random_step(env)
        return handle_response(res)

    print(f"Launching Gym Server. Access at http://{host}:{port}/{route}/")
    return app.run(host = host, port = port)

def gace():
    args = gc.parser.parse_args()
    env_id, pdk, var, num, host, port = \
            [ getattr(args, a) for a in
              ["env", "pdk", "var", "num", "host", "port"]]

    env = gc.make_env(env_id, pdk, var, num)

    route = f'{env_id}-{pdk}-v{var}'

    app = Flask("__main__")

    @app.route(f'/{route}/num_envs', methods=['GET'])
    def num_envs():
        res = {"num": num}
        return handle_response(res)

    @app.route(f'/{route}/current_performance', methods=['GET'])
    def current_performance():
        res = gc.current_performance(env)
        return handle_response(res)

    @app.route(f'/{route}/current_sizing', methods=['GET'])
    def current_sizing():
        res = gc.current_sizing(env)
        return handle_response(res)

    @app.route(f'/{route}/step', methods=['POST'])
    def step():
        res = gc.step(env, request.json)
        return handle_response(res)

    @app.route(f'/{route}/log_path', methods=['GET'])
    def log_path():
        res = gc.log_path(env)
        return handle_response(res)

    @app.route(f'/{route}/reset', methods=['GET', 'POST'])
    def reset():
        res = gc.reset(env, ** (request.json or {}))
        return handle_response(res)

    @app.route(f'/{route}/target', methods=['GET'])
    def target():
        res = gc.target(env)
        return handle_response(res)

    @app.route(f'/{route}/predicate', methods=['GET'])
    def predicate():
        res = gc.predicate(env)
        return handle_response(res)

    @app.route(f'/{route}/scaler', methods=['GET'])
    def scaler():
        res = gc.scaler(env)
        return handle_response(res)

    @app.route(f'/{route}/action_space', methods=['GET'])
    def action_space():
        res = gc.action_space(env)
        return handle_response(res)

    @app.route(f'/{route}/action_keys', methods=['GET'])
    def action_keys():
        res = gc.action_keys(env)
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

    print(f"Launching GACE Server.")
    print(f"\tURL: http://{host}:{port}/{route}/")
    print(f"\tLog: {gc.log_path(env)['path']}")
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

    print(f"Launching HACE Server")
    print(f"\tURL: http://{host}:{port}/{route}/")
    return app.run(host = host, port = port)

def main():
    print(GPL_NOTICE)
    return 0

if __name__ == '__main__':
    sys.exit(main())

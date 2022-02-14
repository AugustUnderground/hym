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

def gace():
    args = gc.parser.parse_args()
    env  = getattr(args, "env")
    pdk  = getattr(args, "pdk")
    var  = getattr(args, "var")
    num  = getattr(args, "num")

    route = f'{env}-{pdk}-v{var}'

    fun_set = gc.functions(env, pdk, var, n = num)

    app = Flask("__main__")

    @app.route(f'/{route}/step', methods=['POST'])
    def step():
        res = fun_set.step(request.json)

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/reset', methods=['GET'])
    def performance():
        res = fun_set.reset()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/target', methods=['GET'])
    def sizing():
        res = fun_set.target()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/action_space', methods=['GET'])
    def performance_parameters():
        res = fun_set.action_space()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/observation_space', methods=['GET'])
    def sizing_parameters():
        res = fun_set.observation_space()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/random_action', methods=['GET'])
    def initial_sizing():
        res = fun_set.random_action()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/random_step', methods=['GET'])
    def random_sizing():
        res = fun_set.random_step()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    return app.run(host = getattr(args, 'host'), port = getattr(args, 'port'))

def ace():
    args = ac.parser.parse_args()
    env  = getattr(args, "env")
    pdk  = getattr(args, "pdk")
    num  = getattr(args, "num")

    route = f'{env}-{pdk}'

    fun_set = ac.functions(env, pdk, n = num)

    app = Flask("__main__")

    @app.route(f'/{route}/simulate', methods=['POST'])
    def simulate():
        res = fun_set.simulate(request.json)

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/performance', methods=['GET'])
    def performance():
        res = fun_set.performance()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/sizing', methods=['GET'])
    def sizing():
        res = fun_set.sizing()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/p-params', methods=['GET'])
    def performance_parameters():
        res = fun_set.performance_parameters()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/s-params', methods=['GET'])
    def sizing_parameters():
        res = fun_set.sizing_parameters()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/init', methods=['GET'])
    def initial_sizing():
        res = fun_set.initial_sizing()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    @app.route(f'/{route}/rng', methods=['GET'])
    def random_sizing():
        res = fun_set.random_sizing()

        if isinstance(res, int):
            abort(res)
        elif res is None:
            abort(400)
        else:
            return res

    return app.run(host = getattr(args, 'host'), port = getattr(args, 'port'))

def main():
    print(GPL_NOTICE)
    return 0

if __name__ == '__main__':
    sys.exit(main())

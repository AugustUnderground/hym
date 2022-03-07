#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x84b0038c

# Compiled with Coconut version 2.0.0-a_dev33 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

from argparse import ArgumentParser
from collections import namedtuple
if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable

import numpy as np
import gym

#envs = gym.vector.make("BipedalWalker-v3", num_envs = 4)
#envs.reset()
#keys = ["observation", "reward", "done", "info"] 
#o_,r,d,i = envs.action_space.sample() |> envs.step 
#o = o_.tolist()
#res = [o,r,d,i] |*> zip |> list |> map$(dict .. zip$(keys)) |> enumerate |> dict

parser = ArgumentParser()
parser.add_argument("--host", type=str, default="localhost", help="Host address")
parser.add_argument("-p", "--port", type=int, default="6006", help="Server Port")
parser.add_argument("-e", "--env", type=str, default="BipedalWalker", help="Gym Environment ID")
parser.add_argument("-v", "--var", type=int, default="3", help="Gym Environment variant")
parser.add_argument("-n", "--num", type=int, default=1, help="Number of Vectorized Envs")

class Environment(_coconut.typing.NamedTuple("Environment", [("env", '_coconut.typing.Any'), ("env_id", 'str'), ("variant", 'int'), ("num", 'int')]), _coconut.object):
    _coconut_is_data = True
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    __match_args__ = ('env', 'env_id', 'variant', 'num')

_coconut_call_set_names(Environment)
def make_env(env_id,  #type: str
     variant,  #type: int
     num  #type: int
    ):
    env_name = "{_coconut_format_0}-v{_coconut_format_1}".format(_coconut_format_0=(env_id), _coconut_format_1=(variant))
    env = gym.vector.make(env_name, num_envs=num)
    environment = Environment(env, env_id, variant, num)

    return environment

def restart(env):
    _, env_id, variant, num = env
    new_env = make_env(env_id, variant, num)

    return new_env

def random_action(env):
    action = (dict)((enumerate)((map)(_coconut.operator.methodcaller("tolist"), env.env.action_space.sample())))

    return action

def action_space(env):
    space = dict(((i), (dict(((k), ((s.to_jsonable)(getattr(s, k)))) for k in ["high", "low"]))) for i, s in enumerate(env.env.action_space))

    return space

def observation_space(env):
    tj = env.observation_space.to_jsonable
    at = ["high", "low"]
    os = env.observation_space
    hi, lo = [(tj)(getattr(os, k)) for k in at]
    space = (dict)((enumerate)((map)(_coconut_forward_compose(_coconut.functools.partial(zip, at), dict), zip(hi, lo))))

    return space

def close(env):
    closed = env.env.close()

    return closed

def random_step(env):
    keys = ["observation", "reward", "done", "info"]
    o_, r, d_, i = (env.env.step)(env.env.action_space.sample())
    o = o_.tolist()
    d = map(bool, d_)
    res = (dict)((enumerate)((map)(_coconut_forward_compose(_coconut.functools.partial(zip, keys), dict), (list)((zip)(*[o, r, d, i])))))
    print(res)

    return res

def step(env, action):
    keys = ["observation", "reward", "done", "info"]
    o_, r, d_, i = (env.env.step)([(np.array)(action[a]) for a in ((sorted)(action.keys()))])
    o = o_.tolist()
    d = map(bool, d_)
    res = (dict)((enumerate)((map)(_coconut_forward_compose(_coconut.functools.partial(zip, keys), dict), (list)((zip)(*[o, r, d, i])))))

    return res

def reset(env):
    obs = (dict)((zip)((list)(map(str, range(env.num))), (env.env.reset()).tolist()))

    return obs

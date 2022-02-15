#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6824b91f

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
import gace
import gym

parser = ArgumentParser()
parser.add_argument("--host", type=str, default="localhost", help="Host address")
parser.add_argument("-p", "--port", type=int, default="6006", help="Server Port")
parser.add_argument("-e", "--env", type=str, default="op2", help="ACE Environment ID, see GACE doc for what's available")
parser.add_argument("-v", "--var", type=int, default="0", help="GACE Environment variant, see GACE doc for what's available")
parser.add_argument("-n", "--num", type=int, default=1, help="Number of Pooled Envs")
parser.add_argument("--pdk", type=str, default="xh035", help="ACE backend, see GACE doc for what's available")

@_coconut_tco
def isiterable(obj):
    return _coconut_tail_call(isinstance, obj, Iterable)


def target(env):
    tgt = (dict(((str(i)), (e.target)) for i, e in (enumerate)(env)) if isiterable(env) else {"0": env.target})

    return tgt

def random_action(env):
    action = (dict(((str(i)), (e.action_space.sample().tolist())) for i, e in (enumerate)(env)) if isiterable(env) else {"0": env.action_space.sample().tolist()})

    return action

def action_space(env):
    space = (dict(((str(i)), ({"high": (a.to_jsonable)(a.high), "low": (a.to_jsonable)(a.low)})) for i, a in (enumerate)(env.action_space)) if isiterable(env) else {"0": env.action_space})

    return space

def observation_space(env):
    space = (dict(((str(i)), ({"high": (o.to_jsonable)(o.high), "low": (o.to_jsonable)(o.low)})) for i, o in (enumerate)(env.observation_space)) if isiterable(env) else {"0": env.observation_space})

    return space

def close(env):
    env.close()

    return "Closed"

def random_step(env):
    keys = ["observation", "reward", "done", "info"]
    res = (dict(((str(i)), (dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in zip(keys, stp)))) for i, stp in (enumerate)((zip)(*env.random_step()))) if isiterable(env) else {"0": dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in (_coconut_partial(zip, {0: keys}, 2))(env.random_step()))})

    return res

def step(env, action):
    keys = ["observation", "reward", "done", "info"]
    act = ([(np.array)(action[a]) for a in ((sorted)(action.keys()))] if isinstance(action, dict) else (np.array)(action))
    res = (dict(((str(i)), (dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in zip(keys, stp)))) for i, stp in (enumerate)((zip)(*(env.step)(act)))) if isiterable(env) else {"0": dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in (_coconut_partial(zip, {0: keys}, 2))((env.step)(act)))})

    return res

def reset(env):
    obs = (dict(((str(i)), (o.tolist())) for i, o in (enumerate)(env.reset())) if isiterable(env) else {"0": (env.reset()).tolist()})

    return obs

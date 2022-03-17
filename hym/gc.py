#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x82cedc8a

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
import hace as ac

parser = ArgumentParser()
parser.add_argument("--host", type=str, default="localhost", help="Host address")
parser.add_argument("-p", "--port", type=int, default="6006", help="Server Port")
parser.add_argument("-e", "--env", type=str, default="op2", help="ACE Environment ID, see GACE doc for what's available")
parser.add_argument("-v", "--var", type=int, default="0", help="GACE Environment variant, see GACE doc for what's available")
parser.add_argument("-n", "--num", type=int, default=1, help="Number of Pooled Envs")
parser.add_argument("--pdk", type=str, default="xh035", help="ACE backend, see GACE doc for what's available")

class Environment(_coconut.typing.NamedTuple("Environment", [("env", '_coconut.typing.Any'), ("env_id", 'str'), ("ace_id", 'str'), ("backend", 'str'), ("variant", 'int'), ("num", 'int')]), _coconut.object):
    _coconut_is_data = True
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    __match_args__ = ('env', 'env_id', 'ace_id', 'backend', 'variant', 'num')

_coconut_call_set_names(Environment)
def make_env(env_id,  #type: str
     backend,  #type: str
     variant,  #type: int
     num  #type: int
    ):
    env_name = "gace:{_coconut_format_0}-{_coconut_format_1}-v{_coconut_format_2}".format(_coconut_format_0=(env_id), _coconut_format_1=(backend), _coconut_format_2=(variant))
    env = (gym.make(env_name) if num == 1 else gace.vector_make_same(env_name, num))
    environment = Environment(env, env_name, env_id, backend, variant, num)

    return environment

def restart(env):
    _, env_id, _, backend, variant, num = env
    new_env = make_env(env_id, backend, variant, num)

    return new_env

def target(env):
    tgt = (dict(((str(i)), (e.target)) for i, e in (enumerate)(env.env)) if env.num > 1 else {"0": env.env.target})

    return tgt

def random_action(env):
    action = (dict(((str(i)), (e.action_space.sample().tolist())) for i, e in (enumerate)(env.env)) if env.num > 1 else {"0": env.env.action_space.sample().tolist()})

    return action

def action_space(env):
    space = (dict(((str(i)), ({"high": (a.to_jsonable)(a.high), "low": (a.to_jsonable)(a.low)})) for i, a in (enumerate)(env.env.action_space)) if env.num > 1 else {"0": env.env.action_space})

    return space

def action_keys(env):
    keys = (dict(((str(i)), (k["actions"])) for i, k in (enumerate)(env.env.info)) if env.num > 1 else {"0": env.env.info["actions"]})

    return keys

def observation_space(env):
    space = (dict(((str(i)), ({"high": (o.to_jsonable)(o.high), "low": (o.to_jsonable)(o.low)})) for i, o in (enumerate)(env.env.observation_space)) if env.num > 1 else {"0": env.env.observation_space})

    return space

def observation_keys(env):
    keys = (dict(((str(i)), (k["observations"])) for i, k in (enumerate)(env.env.info)) if env.num > 1 else {"0": env.env.info["observations"]})

    return keys

def close(env):
    closed = env.env.close()

    return closed

def current_performance(env):
    perf = (dict(((str(i)), (dict(((k), ((np.nan_to_num)(v))) for k, v in ((ac.current_performance)(e.ace)).items()))) for i, e in (enumerate)(env.env)) if env.num > 1 else {"0": dict(((k), ((np.nan_to_num)(v))) for k, v in ((ac.current_performance)(env.env.ace)).items())})

    return perf

def current_sizing(env):
    perf = (dict(((str(i)), (dict(((k), ((np.nan_to_num)(v))) for k, v in ((ac.current_sizing)(e.ace)).items()))) for i, e in (enumerate)(env.env)) if env.num > 1 else {"0": dict(((k), ((np.nan_to_num)(v))) for k, v in ((ac.current_sizing)(env.env.ace)).items())})

    return perf

def random_step(env):
    keys = ["observation", "reward", "done", "info"]
    res = (dict(((str(i)), (dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in zip(keys, stp)))) for i, stp in (enumerate)((zip)(*env.env.random_step()))) if env.num > 1 else {"0": dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in (_coconut_partial(zip, {0: keys}, 2))(env.env.random_step()))})

    return res

def step(env, action, restart_count=0):
    keys = ["observation", "reward", "done", "info"]
    act = ([(np.array)(action[a]) for a in ((sorted)(action.keys()))] if isinstance(action, dict) else (np.array)(action))
    try:
        res = (dict(((str(i)), (dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in zip(keys, stp)))) for i, stp in (enumerate)((zip)(*(env.env.step)(act)))) if env.num > 1 else {"0": dict(((k), ((s.tolist() if k == "observation" else s))) for k, s in (_coconut_partial(zip, {0: keys}, 2))((env.env.step)(act)))})
    except (ac.AceCorruptionException, ac.AcePoolCorruptionException) as err:
        print("Restarting [{_coconut_format_0}] due to corruption\n\n{_coconut_format_1}".format(_coconut_format_0=(restart_count), _coconut_format_1=(err)))
        new_env = restart(env)
        res = step(new_env, action, restart_count + 1)

    return res

def reset(env, env_ids=[], done_mask=None, restart_count=0):
    try:
        obs = (dict(((str(i)), (o.tolist())) for i, o in (enumerate)(env.env.reset(env_ids=env_ids, done_mask=done_mask))) if env.num > 1 else {"0": (env.env.reset()).tolist()})
    except (ac.AceCorruptionException, ac.AcePoolCorruptionException) as err:
        print("Restarting [{_coconut_format_0}] due to corruption\n\n{_coconut_format_1}".format(_coconut_format_0=(restart_count), _coconut_format_1=(err)))
        new_env = restart(env)
        obs = reset(new_env, action, restart_count + 1)

    return obs

def log_path(env):
    res = ({"path": env.env.base_log_path} if env.num > 1 else {"path": env.env.data_log_path})

    return res

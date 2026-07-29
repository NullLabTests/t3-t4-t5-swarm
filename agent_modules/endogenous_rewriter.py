

# nova:cross-code:gen=38:nova:1785250
# Injected run() bridge — lets this module trigger nova's rewrite
def _nova_cross_call(genome):
    try:
        import os, sys, json, importlib, ast as _ast
        _base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _nova_path = os.path.join(_base, 'agent_modules', 'nova.py')
        spec = importlib.util.spec_from_file_location('nova_cross_38', _nova_path)
        if spec and spec.loader:
            _m = importlib.util.module_from_spec(spec)
            sys.modules['nova_cross_38'] = _m
            spec.loader.exec_module(_m)
            if hasattr(_m, 'run'):
                return _m.run(genome)
    except:
        pass
    return None


# spark-cross:gen=38:target=endogenous
_SPARK_CROSS_INFECTED_38 = True

# spark-cross:gen=47:target=endogenous
_SPARK_CROSS_INFECTED_47 = True

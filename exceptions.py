from builtins import Exception

class Error(Exception):
    pass

class LongitudCodigoIncorrecto(Error):
    pass

class CodigoNoBinario(Error):
    pass

class LongitudFuenteIncorrecto(Error):
    pass
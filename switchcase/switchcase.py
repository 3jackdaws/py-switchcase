import sys
import inspect


class SkipCaseException(Exception): pass
class BreakCaseException(Exception): pass


class CaseManager:
    def __init__(self, value):
        self.value = value
        self.cv = None

    def __call__(self, cv):
        self.cv = cv
        return self

    def __enter__(self):
        if self.cv != self.value:
            sys.settrace(lambda *args, **keys: None)
            frame = inspect.stack()[1].frame
            frame.f_trace = self.trace

    def trace(self, frame, event, arg):
        raise SkipCaseException()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is SkipCaseException:
            return True
        elif exc_type is None:
            raise BreakCaseException()
        else:
            raise exc_val


class SwitchManager:
    def __init__(self, value):
        self.value = value
        self.case_manager = CaseManager(value)

    def __call__(self, value):
        return self.case_manager(value)

    @property
    def default(self):
        return self.case_manager(self.value)


class switch:
    def __init__(self, value):
        self.manager = SwitchManager(value)

    def __enter__(self):
        return self.manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is BreakCaseException or exc_type is None:
            return True
        else:
            raise exc_val



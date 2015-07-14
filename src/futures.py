from concurrent.futures import Future

class OneOrMoreFuturesFailed(Exception):
    pass

class FutureGroup(object):
    """Group of futures. all_completed is a future which is completed when all 
       the futures of the group are completed.
    """
    def __init__(self, futures):
        self.futures = futures #Multiple/Single input(s)
        self.all_completed = Future() #Single output
        if (self.futures==[]): #if no argument was passed
            self.all_completed.set_result([None])
        self.results = {}
        self.exceptions = {}
        self.completed = dict((f,False) for f in futures)
        for f in self.futures:
            f.add_done_callback(self.on_completed)

    def on_completed(self, future):
        self.completed[future] = True
        exception = future.exception() 
        self.exceptions[future] = exception if exception is not None else exception
        if exception is None:
            self.results[future] = future.result() 
        else:
            self.results[future] = exception
        if all(self.completed.values()): #All futures are completed
            exceptions = [e for e in self.exceptions.values() if e]
            if exceptions:
                exceptions_str = ",\n".join(map(str,exceptions))
                self.all_completed.set_exception(OneOrMoreFuturesFailed(exceptions_str))
            else:
                self.all_completed.set_result([self.results[f] for f in self.futures])
            del self.results

def all_completed(futures):
    """ Return a new Future that completes when all the futures in the 'futures' list given as argument 
        are completed.
        The new Futures returns the list of results, or sets 'OneOrMoreFuturesFailed' if one or more futures
        failed.
    """
    group = FutureGroup(futures)
    return group.all_completed

def then(future, success_callback=None, error_callback=None):
    """Equivalent of the javascript $q.then

       Calls either 'success_callback' or 'error_callback' when the 'future' completes with as argument the result or the exception.
       Returns a new future that is set to the result of this callback.
       If this callback raises an exception, the new future is set to this exception.

       Note that this function will not call 'error_callback' when 'success_callback' raises.
       
    """
    #Note: As this function is fairly complex, see unittest before changing it.
    future_result = Future()
    def _done(f):
        exception = f.exception()
        if exception is not None:
            result = exception
            callback = error_callback
            if callback is None:
                future_result.set_exception(result)
                return
        else:
            callback = success_callback
            result = f.result()
            if callback is None:
                future_result.set_result(result)
                return
        try:
            result = callback(result)
        except Exception as e:
            future_result.set_exception(e)
        else:
            future_result.set_result(result)
    future.add_done_callback(_done)
    return future_result

# -*- coding: utf-8 -*-
"""
Properties:
------------

@Autores:
- João Vitor Gutkoski Paes, joao.paes@eac.ufsm.br


PyTTa Default Properties:
-------------------------

    As to provide an user friendly signal measurement package, a few default
    values where assigned to the main classes and functions.

    These values where set using a dict called "default", and are passed to all
    PyTTa functions through the Default class object

        >>> import pytta
        >>> pytta.default()

    The default values can be set differently using both declaring method, or
    the set_default() function

        >>> pytta.default.propertyName = propertyValue
        >>> pytta.default.set_defaults(propertyName1 = propertyValue1,
        >>>                            ... ,
        >>>                            propertyNameN = propertyValueN
        >>>                            )

    The main difference is that using the set_default() function, a list of
    properties can be set at the same time

    The default device start as the one set default at the user's OS. We
    recommend changing it's value to the desired audio in/out device, as it
    can be identified using list_devices() method

        >>> pytta.list_devices()

"""


from __future__ import annotations
import json
import sounddevice as sd
from typing import Optional
from threading import Lock


__default_device = [sd.default.device[0], sd.default.device[1]]
""" Used only to hold the default audio I/O device at pytta import time"""


default_ = {'samplingRate': 44100,
            'lengthDomain': 'samples',
            'fftDegree': 18,
            'timeLength': 10,
            'integration': 0.125,
            'minFreq': 20,
            'maxFreq': 20000,
            'device': __default_device,
            'inChannel': [1],
            'outChannel': [1],
            'stopMargin': 0.7,
            'startMargin': 0.3,
            'comment': 'No comments.',
            }


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instance: Optional[Properties] = None

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        if not cls._instance:
            # If there is not an instance of Properties already, locks and creates
            with cls._lock:
                # The first thread to acquire the lock creates the Singleton instance.
                # Once it leaves the lock block, a thread that might have been
                # waiting for the lock release may then see it is already initialized,
                # the thread won't create a new object.
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Properties(metaclass=SingletonMeta):
    """
    Properties:
    ------------

        Holds parameter values for all PyTTa objects and functions.


    Attributes:
    -----------

        samplingRate:
            Sampling frequency of the signal;
        lengthDomain:
            Information about the recording length. May be 'time' or 'samples';
        fftDegree:
            Adjusts the total number of samples to a base 2 number (numSamples = 2**fftDegree);
        timeLength:
            Total time duration of the signal (numSamples = samplingRate * timeLength);
        minFreq:
            Smallest signal frequency of interest;
        maxFreq:
            Greatest signal frequency of interest;
        freqLims['min', 'max']:
            Frequencies of interest bandwidth limits;
        device:
            Devices used for input and output streaming of signals (Measurements only);
        inputChannels:
            Stream input channels of the input device in use (Measurements only);
        outputChannels:
            Stream output channels of the output device in use (Measurements only);
        startMargin:
            Amount of silence time at signal's beginning (Signals only);
        stopMargin:
            Amount of silence time at signal's ending (Signals only);
        margins['start', 'stop']:
            Beginning and ending's amount of time left for silence (Signals only);
        comments:
            Any commentary about the signal or measurement the user wants to add.


    Methods:
    --------

        set_values(property1 = value1, property2 = value2, ... , propertyN = valueN):
            Changes attributes values to the ones assigned at the function call.
            Useful for changing several attributes at once.

        reset():
            Attributes goes back to "factory default".

    """

    _samplingRate = []
    _lengthDomain = []
    _fftDegree = []
    _timeLength = []
    _integration = []
    _minFreq = []
    _maxFreq = []
    _device = []
    _inChannel = []
    _outChannel = []
    _stopMargin = []
    _startMargin = []
    _comment = []

    def __init__(self):
        """
        Changing "factory" default preferences:
        ========================================

            If wanted, the user can set different "factory default" values by changing
            the properties.default dictionary which is used to hold the values that
            the __init__() method loads into the class object at import time
        """

        for name, value in default_.items():
            vars(self)['_'+name] = value

    def __setattr__(self,name,value):
        if name in dir(self) and name!= 'device':
            vars(self)['_'+name] = value
        elif name in ['device','devices']:
            self.set_values(device = value)
        else:
            raise AttributeError ('There is no default settings for '+repr(name))


    def view(self):
        for name, value in vars(self).items():
            if len(name)<=8:
                print(name[1:]+'\t\t =',value)
            else:
                print(name[1:]+'\t =',value)


    def set_values(self,**namevalues):
        """
    	Change the values of the "Properties"

    	>>> pytta.properties.set_values(property1 = value1,
    	...                          property2 = value2,
    	...                          propertyN = valueN)

        The default values can be set differently using both declaring method, or
        the set_values() function
    	"""

        for name, value in namevalues.items(): # iterate over the (propertyName = propertyValue) pairs
            try:
                if vars(self)['_'+name] != value: # Check if user value are different from the ones already set up
                    if name in ['device','devices']: # Check if user is changing default audio IO device
                        sd.default.device = value    # If True, changes the sounddevice default audio IO device
                        vars(self)['_'+name] = sd.default.device # Then loads to PyTTa default device
                    else:
                        vars(self)['_'+name] = value # otherwise, just assign the new value to the desired property
            except KeyError:
                print('You\'ve probably mispelled something.\n' + 'Checkout the property names:\n')
                self.__call__()

    def reset(self):
        vars(self).clear()
        self.__init__()


    @property
    def samplingRate(self):
        return self._samplingRate

    @property
    def lengthDomain(self):
        return self._lengthDomain

    @property
    def fftDegree(self):
        return self._fftDegree

    @property
    def timeLength(self):
        return self._timeLength

    @property
    def integration(self):
        return self._integration

    @property
    def minFreq(self):
        return self._minFreq

    @property
    def maxFreq(self):
        return self._maxFreq

    @property
    def freqLims(self):
        return {'min': self._minFreq, 'max': self._maxFreq}

    @property
    def device(self):
        return self._device

    @property
    def inChannel(self):
        return self._inChannel

    @property
    def outChannel(self):
        return self._outChannel

    @property
    def startMargin(self):
        return self._startMargin

    @property
    def stopMargin(self):
        return self._stopMargin

    @property
    def margins(self):
        return {'start': self._startMargin, 'stop': self._stopMargin}

    @property
    def comment(self):
        return self._comment

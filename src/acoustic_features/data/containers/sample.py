import numpy
import functools
from acoustic_features.data.exceptions.sample import *


class AcousticSampleWrapper(object):
    """Class implementing the acoustic sample wrapper"""

    def __init__(self, sample):
        """Constructor method"""

        # Set the sample
        self.sample = sample

    # ------------------------------- #
    # Alternative constructor methods #
    # ------------------------------- #

    @classmethod
    def from_list(cls, values, fs=None):
        """
        Initializes AcousticSampleWrapper object from a list.

        :param values: data values
        :type values: list
        :param fs: sampling frequency
        :type fs: int, optional
        :return: AcousticSampleWrapper object
        :rtype: AcousticSampleWrapper
        """
        # return cls(AcousticSample.from_list(values, fs=fs))

    @classmethod
    def from_numpy_array(cls, values, fs=None):
        """
        Initializes AcousticSampleWrapper object from a numpy array.

        :param values: data values
        :type values: numpy.ndarray
        :param fs: sampling frequency
        :type fs: int, optional
        :return: AcousticSampleWrapper object
        :rtype: AcousticSampleWrapper
        """
        # return cls(AcousticSample.from_numpy_array(values, fs=fs))

    @classmethod
    def from_pandas_dataframe(cls, values, fs=None):
        """
        Initializes AcousticSampleWrapper object from a pandas DataFrame.

        :param values: data values
        :type values: pandas.DataFrame
        :param fs: sampling frequency
        :type fs: int, optional
        :return: AcousticSampleWrapper object
        :rtype: AcousticSampleWrapper
        """
        # return cls(AcousticSample.from_pandas_dataframe(values, fs=fs))

    # ------------------------- #
    # Sample acoustic variables #
    # ------------------------- #

    # @functools.cached_property
    # def xyz(self):
    #     return ...

    # -------------------------- #
    # Sample validation routines #
    # -------------------------- #

    # @classmethod
    # def validate_xyz(cls, xyz):
    #     """Validates the xyz"""
    #     if something_wrong:
    #         raise SomeException(f"explanation")

    # ---------------------- #
    # Computational routines #
    # ---------------------- #

    # @functools.lru_cache(maxsize=some_number)
    # def compute_xyz(self, args, **kwargs):
    #     """
    #     Computes the xyz.
    #
    #     :param ...: ...
    #     :type ...: ..., [optional]
    #     ...
    #     :return: xyz
    #     :rtype: [type(s)]
    #     """
    #
    #     # Validate the input arguments
    #     self.validate_xyz(arg)
    #     # ...
    #
    #     # Compute the xyz
    #     # ...
    #
    #     # Return the xyz
    #     # return ...

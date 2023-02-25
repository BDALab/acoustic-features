from acoustic_features.features.base import AcousticFeaturesBase
from acoustic_features.features.implementation import *


class AcousticFeatures(AcousticFeaturesBase):
    """Class implementing interface for computation of acoustic features"""

    # ----------------- #
    # Acoustic features #
    # ----------------- #

    # def xyz(self, statistics=()):
    #     """
    #     Extracts the xyz feature.
    #
    #     :param statistics: statistics to compute, defaults to ()
    #     :type statistics: Any[list, tuple], optional
    #     :return: velocity
    #     :rtype: numpy.ndarray or numpy.NaN
    #     """
    #     return self.compute(self.wrapper, xyz, statistics=statistics)

    # ...

from acoustic_features.features.exceptions.mapping import *


class AcousticFeaturesMapping(object):
    """Class implementing the acoustic features mapping"""

    def __init__(self, features):
        """Constructor method"""
        self.features = features

    def map(self, feature_name):
        """Map the feature name to the actual feature computation method"""

        # Prepare the mapping (feature name: feature computation method)
        mapping = {
            # "xyz": self.features.xyz,
        }

        # Map the feature name to the feature computation method
        try:
            return mapping[feature_name]
        except KeyError:
            raise FeatureNameNotInMappingError(f"No mapping available for feature {feature_name}")

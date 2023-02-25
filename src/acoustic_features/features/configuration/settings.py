from acoustic_features.data.containers.sample import AcousticSampleWrapper
from acoustic_features.data.descriptors.statistics import Statistics


class AcousticFeaturesSettings(object):
    """Class implementing the acoustic features settings"""

    # Acoustic features statistics
    statistics = Statistics.mapping.keys()

    # Acoustic features settings
    settings = {

        # Feature name
        # "feature_name": {
        #     "properties": {
        #         "is_multi_valued": True / False
        #     },
        #     "arguments": {
        #         "statistics": {
        #             "mandatory": False,
        #             "type": [str, list, tuple],
        #             "options": statistics
        #         }  # <- statistics should be used here only for multivalued features (i.e. is_multi_valued = True)
        #     }
        # },

        # ...
    }

    @classmethod
    def get_feature_argument_type(cls, feature_name, argument_name):
        """
        Gets the feature argument's supported type(s).

        :param feature_name: feature name
        :type feature_name: str
        :param argument_name: argument name
        :type argument_name: str
        :return: argument's type(s)
        :rtype: iterable
        """
        return cls.settings.get(feature_name, {}).get("arguments").get(argument_name, {}).get("type", [])

    @classmethod
    def get_feature_argument_options(cls, feature_name, argument_name):
        """
        Gets the feature argument's option(s).

        :param feature_name: feature name
        :type feature_name: str
        :param argument_name: argument name
        :type argument_name: str
        :return: argument's option(s)
        :rtype: iterable
        """
        return cls.settings.get(feature_name, {}).get("arguments").get(argument_name, {}).get("options", [])

    @classmethod
    def get_feature_argument_default(cls, feature_name, argument_name):
        """
        Gets the feature argument's default value(s).

        :param feature_name: feature name
        :type feature_name: str
        :param argument_name: argument name
        :type argument_name: str
        :return: argument's default value(s)
        :rtype: Any
        """
        return cls.settings.get(feature_name, {}).get("arguments").get(argument_name, {}).get("default")

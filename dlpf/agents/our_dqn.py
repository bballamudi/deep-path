import keras, logging, itertools
import keras.backend as K
from keras.layers import Dense, Flatten, Dropout, Reshape, \
    Convolution2D, MaxPooling2D, AveragePooling2D, \
    BatchNormalization, Activation

from .base import BaseStandaloneKerasAgent
from .ranking import BasePointwiseRankingAgent, BasePairwiseRankingAgent, \
    SimpleMaxValueRankingAgent
from .architectures import OneLayer, TwoLayer, ConvAndDense


logger = logging.getLogger()


###############################################################################
############################# Standalone agents ###############################
###############################################################################
class OneLayerAgent(OneLayer, BaseStandaloneKerasAgent):
    pass


class TwoLayerAgent(TwoLayer, BaseStandaloneKerasAgent):
    pass


class ConvAndDenseAgent(ConvAndDense, BaseStandaloneKerasAgent):
    pass


###############################################################################
########################## Pointwise ranking agents ###########################
###############################################################################
class TwoLayerPointwiseAgent(TwoLayer, BasePointwiseRankingAgent):
    pass


class ConvAndDensePointwiseAgent(ConvAndDense, BasePointwiseRankingAgent):
    pass


###############################################################################
########################### Pairwise ranking agents ###########################
###############################################################################
class TwoLayerPairwiseAgent(TwoLayer, BasePairwiseRankingAgent):
    pass


class ConvAndDensePairwiseAgent(ConvAndDense, BasePairwiseRankingAgent):
    pass


###############################################################################
######################## Greedy agents without learning #######################
###############################################################################
class SimpleMaxValueRankingNoLearningAgent(OneLayer, SimpleMaxValueRankingAgent):
    pass

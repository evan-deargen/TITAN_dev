from .knn import knn
from .bimodal_mca import BimodalMCA

# More models could follow
MODEL_FACTORY = {
    'bimodal_mca': BimodalMCA,
    'knn': knn
}

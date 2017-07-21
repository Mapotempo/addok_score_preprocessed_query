from addok.config import config
from addok.helpers import iter_pipe

def score_preprocessed_query(helper, result):
    helper.query = list(iter_pipe(helper.query, config.QUERY_PROCESSORS))[0]

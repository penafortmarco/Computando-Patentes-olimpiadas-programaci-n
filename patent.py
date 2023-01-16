from old_patent import get_old_patent_format
from new_patent import get_new_patent_format

def next_patent(patent, k):
    """Validates the right format for the patent. It also manage error cases.
    Then call the functions that are needed to return the next "k" patent."""
    if len(patent) < 6 or len(patent) > 7:
            error_message = 'Not a valid patent.'
            return error_message
    if k <= 0 or type(k) != int:
        error_message = 'K is not a valid argument.'
        return error_message
    
    try:
        if len(patent) == 6:
            return get_old_patent_format(patent, k)
        if len(patent) == 7:
            return get_new_patent_format(patent, k)
    except Exception as e:
        print(e)


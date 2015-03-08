def transpose(mat):
    R, C = len(mat), len(mat[0])
    return [[ mat[i][j] for i in range(R)] for j in range(C)]

def intercalate(wrds):
    return " ".join(wrds)

def stringPaste(strs):
    """
    Pastes several strings together side-by-side
    For strings without newlines, this is a simple string join
    For strings with new-lines, it does the intuitive thing

    Note: strings must all have the same number of newlines
    """
    lns = [ s.split("\n") for s in strs ]
    rows = transpose(lns)
    return "\n".join( intercalate(row) for row in rows )

def matrixPrint(mat):
    """
    Takes in a matrix of strings
    Returns a string that, when printed, is what you would want out of
    printing a matrix

    Example:
    matrixPrint([["1", "2", "3"], ["4", "5", "6"]]) would yield
        1 2 3
        4 5 6
    """
    return "\n".join( stringPaste(row) for row in mat )

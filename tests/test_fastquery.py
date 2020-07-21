# VS Code pytest fix
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# real imports
import dffastquery

def test_fastquery():
    import pandas as pd
    import numpy as np

    testdata = {"a":["A", "B", "A", "B"], "b":["Q", "W", "R", "R"], "c":["a", "b", "c", "d"]}
    testresult = np.array([['A','R', 'c']])
    df = pd.DataFrame(testdata)
    dfff = dffastquery.FastQuery(df)

    df_res = dfff.querydf({"a":"A", "b":"R"})
    assert (df_res.values == testresult).all()
import pandas as pd
import numpy as np
import typing

__version__ = "0.1.0"

ColumnName = typing.NewType("ColumnName", str)

UniqueColumnValue = typing.NewType("UniqueColumnValue", str)
QueryDict = typing.Dict[ColumnName, UniqueColumnValue]
DataFrameIndex = typing.NewType("DataFrameIndex", int)
DfIndexSet = typing.Set[DataFrameIndex]
IndexDict = typing.Dict[ColumnName, typing.Dict[UniqueColumnValue, DfIndexSet]]


class FastQuery:
    def __init__(self, df: pd.DataFrame):
        """Init for FastQuery class. Creates the query index when called. 
        The index is only created for string columns.

        Args:
            df (pd.DataFrame): Pandas DataFrame with string columns.
        """
        self._df = df
        self._indexdict: IndexDict = {}

        self._create_index()

    def _create_index(self):
        """ Creates the index for queries. Do not call this directly.
        """
        # Iterate throug columns
        cname: ColumnName
        for _, cname in enumerate(self._df):
            if self._df[cname].dtype == np.object:

                self._indexdict[cname] = {}
                uniquevals = self._df[cname].unique()
                for uval in uniquevals:
                    self._indexdict[cname][uval] = set(
                        self._df[self._df[cname] == uval].index
                    )

    def queryindex(self, valuedict: QueryDict):
        indexset: DfIndexSet
        emptyindex = True
        indexset = set()
        cname: ColumnName
        cval: UniqueColumnValue
        for cname, cval in valuedict.items():
            if emptyindex:
                indexset = self._indexdict[cname][cval]
                emptyindex = False
            else:
                indexset = indexset & self._indexdict[cname][cval]

        return list(indexset)

    def querydf(self, valuedict: QueryDict):
        return self._df.loc[self.queryindex(valuedict)]

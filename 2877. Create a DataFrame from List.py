import pandas as pd
import numpy as np
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column=["student_id","age"]
    result=pd.DataFrame(student_data,columns=column)
    return result

import pandas as pd

def load_and_expand_minute(csv_path: str, tag: str | None = None) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="cp949")
    if tag is not None and 'tag_name' in df.columns:
        df = df[df['tag_name']==tag]
    hour = pd.to_datetime(df['yyyymmddhh'].astype(str), format="%Y%m%d%H")
    mins = [c for c in df.columns if c.endswith("_minute_value")]
    wide = df.set_index(hour)[mins].rename(columns=lambda c:int(c.split("_")[0]))
    ts = wide.stack().rename("value").reset_index().rename(columns={"level_1":"minute"})
    ts["timestamp"] = ts["yyyymmddhh"] + pd.to_timedelta(ts["minute"], unit="m")
    return ts[["timestamp","value"]].set_index("timestamp").sort_index()

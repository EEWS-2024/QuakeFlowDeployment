# %%
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# %%
result_path = Path("./results")

gamma_file = result_path / "gamma_catalog.csv"
gamma_catalog = pd.read_csv(gamma_file)

# %%
hypodd_file = result_path / "hypodd_catalog.txt"
columns = ["ID", "LAT", "LON", "DEPTH", "X", "Y", "Z", "EX", "EY", "EZ", "YR", "MO", "DY", "HR", "MI", "SC", "MAG", "NCCP", "NCCS", "NCTP", "NCTS", "RCC", "RCT", "CID"]
catalog_hypodd = pd.read_csv(hypodd_file, delim_whitespace=True, header=None, names=columns, )
catalog_hypodd["time"] = catalog_hypodd.apply(lambda x: f'{x["YR"]:04.0f}-{x["MO"]:02.0f}-{x["DY"]:02.0f}T{x["HR"]:02.0f}:{x["MI"]:02.0f}:{min(x["SC"], 59.999):05.3f}',axis=1)
catalog_hypodd["time"] = catalog_hypodd["time"].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f"))

# %%
growclust_file = result_path / "growclust_catalog.txt"
columns = ["yr", "mon", "day", "hr", "min", "sec", "evid", "latR", "lonR", "depR", "mag", "qID", "cID", "nbranch", "qnpair", "qndiffP", "qndiffS", "rmsP", "rmsS", "eh", "ez", "et", "latC", "lonC", "depC"]
growclust_catalog = pd.read_csv(growclust_file, delim_whitespace=True, header=None, names=columns)
growclust_catalog["time"] = growclust_catalog.apply(lambda x: f'{x["yr"]:04.0f}-{x["mon"]:02.0f}-{x["day"]:02.0f}T{x["hr"]:02.0f}:{x["min"]:02.0f}:{min(x["sec"], 59.999):05.3f}',axis=1)
growclust_catalog["time"] = growclust_catalog["time"].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f"))

# %%
fig, ax = plt.subplots(1, 3, squeeze=False, figsize=(15,5))
ax[0, 0].scatter(gamma_catalog["longitude"], gamma_catalog["latitude"], s=2, alpha=1.0)
xlim = ax[0, 0].get_xlim()
ylim = ax[0, 0].get_ylim()
ax[0, 1].scatter(catalog_hypodd["LON"], catalog_hypodd["LAT"], s=2, alpha=1.0)
ax[0, 1].set_xlim(xlim)
ax[0, 1].set_ylim(ylim)
ax[0, 2].scatter(growclust_catalog["lonR"], growclust_catalog["latR"], s=2, alpha=1.0)
ax[0, 2].set_xlim(xlim)
ax[0, 2].set_ylim(ylim)
plt.show()
# %%
# spec2mol-preview

De novo structure elucidation from MS/MS spectra. We design a new decoder and reuse the same MIST encoder checkpoints shared by FRIGID.

## Results

| Model          | Version                                                                                           | Top-1 Acc (%) ↑ | MCES@1 ↓ | Tanimoto@1 ↑ | Top-10 Acc (%) ↑ | MCES@10 ↓ | Tanimoto@10 ↑ |
| -------------- | ------------------------------------------------------------------------------------------------- | --------------: | -------: | -----------: | ---------------: | --------: | ------------: |
| FRIGID-base    | [v2026.08.20](https://github.com/coleygroup/FRIGID/tree/d242a2c06d671e0fb6fbc1a5b31f0e19e24b456d) |            16.1 |     15.0 |         0.41 |             18.2 |      12.0 |          0.46 |
| FRIGID-refined | [v2026.08.20](https://github.com/coleygroup/FRIGID/tree/d242a2c06d671e0fb6fbc1a5b31f0e19e24b456d) |            18.3 |     13.5 |         0.43 |             22.0 |      11.7 |          0.47 |
| Ours-base      | v2026.10.16                                                                                       |            28.5 |      8.0 |         0.58 |             38.6 |       6.5 |          0.64 |

In October 2026, FRIGID switched to retrained MIST encoder checkpoints ([coleygroup/FRIGID#12](https://github.com/coleygroup/FRIGID/pull/12)) to avoid molecule leakage on the MassSpecGym benchmark.
With the new checkpoints, top-1 accuracy drops by about half for FRIGID (16.1 → 8.2 base, 18.3 → 9.1 refined) and from 28.5 to 11.7 for our model, which remains the best on all six metrics.

| Model          | Version                                                                                           | Top-1 Acc (%) ↑ | MCES@1 ↓ | Tanimoto@1 ↑ | Top-10 Acc (%) ↑ | MCES@10 ↓ | Tanimoto@10 ↑ |
| -------------- | ------------------------------------------------------------------------------------------------- | --------------: | -------: | -----------: | ---------------: | --------: | ------------: |
| FRIGID-base    | [v2026.10.21](https://github.com/coleygroup/FRIGID/tree/5adba44b643e444b5b28e54645ce8dde11df2437) |             8.2 |     13.2 |         0.38 |              9.8 |      11.7 |          0.43 |
| FRIGID-refined | [v2026.10.21](https://github.com/coleygroup/FRIGID/tree/5adba44b643e444b5b28e54645ce8dde11df2437) |             9.1 |     12.6 |         0.39 |             12.2 |      11.4 |          0.43 |
| Ours-base      | v2026.10.30                                                                                       |            11.7 |     11.1 |         0.41 |             18.5 |       9.7 |          0.49 |

## Code Release

Paper is under review. We will release the full implementation soon.

# spec2mol-preview

De novo structure elucidation from MS/MS spectra. We design a new decoder and reuse the same MIST encoder checkpoints shared by FRIGID.

## Results

| Model          | Version                                                                                           | Acc%@1 ↑ | MCES@1 ↓ | Tanimoto@1 ↑ | Acc%@10 ↑ | MCES@10 ↓ | Tanimoto@10 ↑ |
| -------------- | ------------------------------------------------------------------------------------------------- | -------: | -------: | -----------: | --------: | --------: | ------------: |
| FRIGID-base    | [v2026.08.20](https://github.com/coleygroup/FRIGID/tree/d242a2c06d671e0fb6fbc1a5b31f0e19e24b456d) |     16.1 |     15.0 |         0.41 |      18.2 |      12.0 |          0.46 |
| FRIGID-refined | [v2026.08.20](https://github.com/coleygroup/FRIGID/tree/d242a2c06d671e0fb6fbc1a5b31f0e19e24b456d) |     18.3 |     13.5 |         0.43 |      22.0 |      11.7 |          0.47 |
| MS-GPT         | [v2026.07.26](https://arxiv.org/pdf/2607.23607v1)                                                 |     23.9 |     15.5 |         0.52 |      28.7 |      11.7 |          0.54 |
| Ours-base      | v2026.10.16                                                                                       |     28.5 |      8.0 |         0.58 |      38.6 |       6.5 |          0.64 |
| GEMS           | [v2026.10.16](https://arxiv.org/pdf/2610.23617v1)                                                 |     30.2 |      9.7 |         0.55 |      41.3 |       8.3 |          0.61 |
| Ours-base      | v2026.11.12                                                                                       |     32.4 |      7.3 |         0.62 |      44.5 |       6.0 |          0.69 |

In October 2026, FRIGID switched to retrained MIST encoder checkpoints ([coleygroup/FRIGID#12](https://github.com/coleygroup/FRIGID/pull/12)) to avoid molecule leakage on the MassSpecGym benchmark.
With the new checkpoints, Acc@1uracy drops by about half for FRIGID (16.1 → 8.2 base, 18.3 → 9.1 refined) and from 28.5 to 11.7 for our model, which remains the best on all six metrics.

| Model          | Version                                                                                           | Acc%@1 ↑ | MCES@1 ↓ | Tanimoto@1 ↑ | Acc%@10 ↑ | MCES@10 ↓ | Tanimoto@10 ↑ |
| -------------- | ------------------------------------------------------------------------------------------------- | -------: | -------: | -----------: | --------: | --------: | ------------: |
| FRIGID-base    | [v2026.10.21](https://github.com/coleygroup/FRIGID/tree/5adba44b643e444b5b28e54645ce8dde11df2437) |      8.2 |     13.2 |         0.38 |       9.8 |      11.7 |          0.43 |
| FRIGID-refined | [v2026.10.21](https://github.com/coleygroup/FRIGID/tree/5adba44b643e444b5b28e54645ce8dde11df2437) |      9.1 |     12.6 |         0.39 |      12.2 |      11.4 |          0.43 |
| MS-GPT         | [v2026.10.29](https://arxiv.org/pdf/2607.23607v2)                                                 |     10.2 |     12.1 |         0.39 |      13.2 |      10.6 |          0.45 |
| Ours-base      | v2026.10.30                                                                                       |     11.7 |     11.1 |         0.41 |      18.5 |       9.7 |          0.49 |
| Ours-base      | v2026.11.12                                                                                       |     12.3 |     11.0 |         0.43 |      21.4 |       9.4 |          0.51 |

## Code Release

Paper is under review. We will release the full implementation soon.

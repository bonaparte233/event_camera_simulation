# Contributing

Contributions should improve the accuracy of this event-camera simulation resource index. The repository includes papers, public code, project pages, and platform documentation related to event-camera simulation. Please keep new entries aligned with the category structure used in the README.

## Add Or Update An Entry

Please include:

- for papers: authors, title, venue or publication status, year, and DOI or arXiv identifier;
- for public resources: project or platform name, documentation link, code link when available, and the related paper if there is one;
- official project page, code link, or documentation link when available;
- the category path where the entry should be placed in the README.

In an issue or pull request, briefly explain why the entry fits that category.

Do not upload or redistribute publisher PDFs, copied tables from papers, or third-party code.

Do not describe a general-purpose platform as an event-camera simulator unless the entry clearly identifies the DVS-style interface or plugin.

## README Entry Format

Only correctly formatted README entries are included in the project page. Use one bullet under the right category. Links should use the `[[label](url)]` style, but link labels are not fixed; add as many resource links as are useful and publicly accessible.

```markdown
- **Authors**, *Paper or resource title*, Venue or status Year. [[paper](https://...)] [[project](https://...)] [[code](https://github.com/...)] [[supplement](https://...)]
```

For platform resources without a paper title, a shorter entry is fine:

```markdown
- **Platform or resource name**. [[documentation](https://...)] [[repository](https://github.com/...)] [[demo](https://...)]
```

The link labels above are examples, not required types. The script parses any number of `[[label](url)]` links and displays the labels as written.

After editing the README locally, run:

```bash
python scripts/sync_page.py
python scripts/check_site.py
```

The GitHub workflow checks pull requests and synchronizes generated page blocks after direct updates to `main`.

## Category Labels

Choose one category path from the hierarchy below. The categories follow the review's mechanism-based framing: methods are grouped by how events are generated, not by the downstream task they support.

- `Physics- and Rule-Based Event-Camera Simulators`

  Event generation is governed by an explicit sensing or rendering mechanism, so the assumptions behind the generated events remain inspectable.

  - `Threshold-Based Simulators`: the event trigger rule is the core model.
  - `Sensor-Level Simulators`: the sensor process around the trigger is the core model.
  - `Scene-Level Simulators`: the scene or world that drives the event stream is the core model.
  - `Differentiable / Trainable Extensions`: an explicit simulator core is kept, but made differentiable, trainable, calibratable, or optimization-ready.

- `Learning-Based Event Generation`

  Event generation is primarily learned from data, so realism comes from the learned mapping rather than an inspectable sensing chain.

  - `Direct Event Generation`: the model learns events directly from images or video.
  - `Conditional Event Generation`: the model learns events under explicit controls such as parameters, prompts, target-domain events, or other conditioning signals.

- `Evaluation and Sim-to-Real Analysis`

  The resource mainly measures, compares, or diagnoses simulation realism, calibration, benchmark behavior, downstream utility, or transfer to real event-camera data.

For mixed papers or public resources, classify by the main reusable contribution, not by every component that appears in the pipeline. If the category still depends on an interpretation, open an issue with evidence from the paper or official resource page before adding it to the main list.

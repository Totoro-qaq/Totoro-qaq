# Contribution icon credits

The icon and project-name portions form one visual badge. Icons link to the official project websites; names link to merged pull requests authored by Totoro-qaq. The artwork retains its original colors and geometry and is scaled into the icon portion.

| Project | Source | License and attribution |
| --- | --- | --- |
| systemd | [Official favicon](https://github.com/systemd/brand.systemd.io/blob/main/favicon.svg), [brand guidelines](https://brand.systemd.io/) | Tobias Bernard, [CC BY-SA 4.0](./licenses/systemd-license.txt). The scaled `systemd-icon.svg` badge is distributed under the same license. |
| Apache Maka | [Official icon generator](https://github.com/apache/maka/blob/492ff80f0f4abf3a917ce8f2c41b32fa9e3fc60c/scripts/generate-app-icons.py), sky variant | Copyright 2026 The Apache Software Foundation. [Apache-2.0](./licenses/maka-LICENSE.txt), [NOTICE](./licenses/maka-NOTICE.txt). The official generator's unmodified SVG output is included in `sources/maka-icon.svg`. The icon links to the [official project website](https://maka.apache.org/en/) under the [ASF logo-link policy](https://www.apache.org/foundation/marks/index.html). Apache and Apache Maka are trademarks of The Apache Software Foundation. |
| CopilotKit | [Official mark](https://github.com/CopilotKit/CopilotKit/blob/078260605a2ccfa0042fb4d835f36f0c4960fdc6/examples/integrations/claude-sdk-python/public/copilotkit-logo-mark.svg) | Copyright (c) Atai Barkai. [MIT](./licenses/copilotkit-LICENSE.txt). |
| Cherry Studio | [Official application icon](https://github.com/CherryHQ/cherry-studio/blob/e85d13ca8469c0e1d61ac8d575d50691305fd4a2/build/icon.png) | Source: Cherry Studio project / CherryHQ. Repository [AGPL-3.0](./licenses/cherry-studio-LICENSE.txt). The adapted icon badge is distributed under AGPL-3.0; the original PNG and rendering source are included in `sources/`. No artwork copyright year has been inferred from the license text. |

## Source and modifications

Modified on 2026-09-07 to create the contribution badges described below.

Original SVGs and the original Cherry Studio PNG are included in `sources/`. SVG artwork is unmodified apart from scaling, viewport/identifier normalization, and placement on the badge background. Cherry Studio's PNG is resized to 40 by 40 pixels and placed on a 64 by 64 transparent badge canvas, displayed at 32 pixels high.

To regenerate the Cherry Studio badge, install `sharp` in a scratch Node.js project and run `sources/render-cherry-badge.mjs` with that dependency available. The script contains the exact rendering parameters. These component licenses do not change the license of unrelated profile text or assets.

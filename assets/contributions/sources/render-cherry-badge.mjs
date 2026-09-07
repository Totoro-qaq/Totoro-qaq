// SPDX-License-Identifier: AGPL-3.0-only
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const input = fileURLToPath(new URL('./cherry-studio-icon.png', import.meta.url));
const output = fileURLToPath(new URL('../cherry-studio-icon.png', import.meta.url));
const icon = await sharp(input).resize(40, 40).png().toBuffer();
const background = Buffer.from(
  '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64"><path d="M6 0H64V64H6Q0 64 0 58V6Q0 0 6 0Z" fill="#30363d"/></svg>',
);

await sharp(background)
  .composite([{ input: icon, left: 16, top: 12 }])
  .png()
  .toFile(output);

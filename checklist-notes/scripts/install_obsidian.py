#!/usr/bin/env python3
"""Install this Skill's scoped CSS into one explicitly chosen Obsidian vault."""
import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

NAME = 'checklist-notes'
ROOT = Path(__file__).resolve().parents[1]
CSS = ROOT / 'assets' / f'{NAME}.css'
SAMPLE = ROOT / 'assets' / '样例笔记.md'


def main():
    parser = argparse.ArgumentParser(description='Install and verify checklist-notes styling in an Obsidian vault')
    parser.add_argument('--vault', required=True, help='Exact path to the target Obsidian vault')
    args = parser.parse_args()
    vault = Path(args.vault).expanduser().resolve()
    config = vault / '.obsidian'
    appearance = config / 'appearance.json'
    if not vault.is_dir() or not config.is_dir():
        sys.exit('STOP: path is not an existing Obsidian vault; confirm the exact vault with the user.')
    if not CSS.is_file() or not SAMPLE.is_file():
        sys.exit('STOP: Skill package is incomplete; CSS or sample is missing.')
    if appearance.exists():
        try:
            settings = json.loads(appearance.read_text(encoding='utf-8'))
        except (ValueError, OSError) as exc:
            sys.exit(f'STOP: cannot safely read appearance.json: {exc}')
        if not isinstance(settings, dict):
            sys.exit('STOP: appearance.json is not a JSON object.')
    else:
        settings = {}
    enabled = settings.get('enabledCssSnippets', [])
    if not isinstance(enabled, list) or any(not isinstance(x, str) for x in enabled):
        sys.exit('STOP: enabledCssSnippets has an unexpected format; inspect manually.')
    snippets = config / 'snippets'
    target = snippets / CSS.name
    sample_target = vault / '清单体笔记_样式验收.md'
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    snippets.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() != CSS.read_bytes():
        backup = snippets / f'{NAME}.backup-{stamp}.css'
        shutil.copy2(target, backup)
        print(f'Existing CSS backed up: {backup}')
    if not target.exists() or target.read_bytes() != CSS.read_bytes():
        shutil.copy2(CSS, target)
    if NAME not in enabled:
        settings['enabledCssSnippets'] = enabled + [NAME]
        if appearance.exists():
            backup = config / f'appearance.backup-{stamp}.json'
            shutil.copy2(appearance, backup)
            print(f'Appearance settings backed up: {backup}')
        tmp = config / f'appearance.{stamp}.tmp'
        tmp.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        tmp.replace(appearance)
    if not sample_target.exists():
        shutil.copy2(SAMPLE, sample_target)
    elif sample_target.read_bytes() != SAMPLE.read_bytes():
        sample_target = vault / f'清单体笔记_样式验收_{stamp}.md'
        shutil.copy2(SAMPLE, sample_target)
    assert target.read_bytes() == CSS.read_bytes()
    loaded = json.loads(appearance.read_text(encoding='utf-8'))
    assert NAME in loaded.get('enabledCssSnippets', [])
    assert 'checklist-notes' in sample_target.read_text(encoding='utf-8')
    print(f'CONFIGURED vault={vault}')
    print(f'CSS={target}')
    print(f'SAMPLE={sample_target}')
    print('FILE_CHECK=PASS; VISUAL_CHECK=REQUIRED in Obsidian reading and live-preview views')


if __name__ == '__main__':
    main()

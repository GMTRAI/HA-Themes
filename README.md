# HA Themes

A growing collection of Home Assistant themes by GMTRAI. Starting with **Drift Home**, an Apple-inspired design with rounded cards, calm surfaces and blue accents.

## Install through Marketplace

1. Open **Settings → Marketplace → Add from link**.
2. Enter **https://github.com/GMTRAI/HA-Themes**. Connect GitHub if prompted.
3. Choose **Theme** if asked, then install **HA Themes**.
4. Open your profile and choose **Drift Home**, **Drift Home Light**, or **Drift Home Dark**.

Drift Home supports both light and dark appearance; choose Auto in your profile to follow your device. The explicit Light and Dark variants stay in their respective mode.

This is a custom repository, not a listing in the default Marketplace catalog. Adding it from its link is required the first time. Installation changes the Home Assistant interface, not your Mac Dock or mobile app icon.

If themes do not appear, check that your `configuration.yaml` includes this under its existing `frontend` key:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Do not duplicate an existing `frontend` key. Reload themes after changing an existing theme configuration; check configuration and restart if enabling themes for the first time.

## Collection

| Theme | Appearance | Dependencies |
| --- | --- | --- |
| Drift Home | Automatic light/dark | None |
| Drift Home Light | Light | None |
| Drift Home Dark | Dark | None |

All theme definitions live in **themes/ha-themes.yaml**. Keeping multiple named themes in one file supports a shared collection and older HACS packaging conventions. Installing this repository installs the collection; your profile determines which theme is active.

## Optional dashboards

[Drift Home dashboard package](extras/drift-home/START-HERE.txt) includes responsive kitchen iPad and mobile dashboards, floor navigation and reusable examples. These are optional, manually installed templates: Marketplace theme installation does not install dashboards or map devices.

Every entity is marked `replace_me`. Map it to your actual entity or remove its card. Room names are examples. No real device IDs, credentials or household data are included.

## Adding future themes

Add each new theme as a uniquely named top-level mapping in `themes/ha-themes.yaml`. Keep light/dark variants under `modes`, and keep all theme values strings. Do not use YAML tags such as `!include` or `!secret`. Add the theme to the table above and describe changes in CHANGELOG.md. Keep dashboard examples outside `themes/`.

## Validation

YAML and dashboard navigation were checked locally. The theme has not yet been visually verified in a live Home Assistant installation. Frontend styling variables can change between releases; verify cards, settings, dialogs and mobile views after upgrades. No live-home screenshots are claimed or included.

## References

- [Home Assistant Marketplace](https://www.home-assistant.io/integrations/marketplace/)
- [Publishing themes](https://contributors.home-assistant.io/marketplace/guides/themes/)
- [Theme configuration](https://www.home-assistant.io/integrations/frontend/)

# Mead & Hunt Delete Unused Materials

![Delete Unused Materials Screenshot](/exts/meadhunt.utility.materials.deleteunused/data/preview_deleteunused.png)

## Inspiration
`Delete Unused Materials` was created based on a request from the [Omniverse forums](https://forums.developer.nvidia.com/t/is-there-a-built-in-way-to-remove-unused-materials/220588).

It also provided me a chance to learning Python, USD, and Kit APIs/workflows.

## About
This tool was created so users can `Delete Unused Materials` from the scene. When new materials are applied to an object the old one remains in the scene. The tool skips materials in `References` and `Payloads` as they can only be deleted in the original file.

## Usage
After installation the dialog can be opened by **Right-Clicking in the `Stage > Delete Unused Materials`**.

## Adding This Extension
To add this extension to your Omniverse app:
1. Go into: Extension Manager -> Gear Icon -> Extension Search Path
2. Add this as a search path: `git://github.com/ericcraft-mh/meadhunt-utility-materials-deleteunused.git?branch=main&dir=exts`

## To-Do List
- Custom Glyph in context menu.
- Confirmation dialog with ability to deselect materials you don't want to remove.

## App Link Setup
If `app` folder link doesn't exist or broken it can be created again. For better developer experience it is recommended to create a folder link named `app` to the *Omniverse Kit* app installed from *Omniverse Launcher*. Convenience script to use is included.

Run:

```
> link_app.bat
```

If successful you should see `app` folder link in the root of this repo.

If multiple Omniverse apps is installed script will select recommended one. Or you can explicitly pass an app:

```
> link_app.bat --app create
```

You can also just pass a path to create link to:

```
> link_app.bat --path "C:/Users/bob/AppData/Local/ov/pkg/create-2021.3.4"
```

## Contributing
The source code for this repository is provided as-is, but I am accepting outside contributions.

Issues, Feature Requests, and Pull Requests are welcomed.

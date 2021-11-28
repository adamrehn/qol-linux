# QoL tools and tweaks for Linux

This repository contains assorted tools and tweaks for Linux that aim to provide small Quality of Life (QoL) improvements to the user experience. Note that these tools and tweaks primarily target distributions that use the **GNOME** desktop environment and may leverage GNOME-specific functionality.

The following tools and tweaks are currently available:

- [**directory-desktop-entry**](./tools/directory-desktop-entry/directory-desktop-entry.py): this is a simple Python script that generates [XDG Desktop Entries](https://specifications.freedesktop.org/desktop-entry-spec/latest/) (`.desktop` files) to open specific directories in the Nautilus file manager, which can then be added to the user's favourites so they appear in the GNOME Shell dash. This provides a roundabout mechanism by which filesystem directories can be added as favourites in the same manner as applications.

# worldgrep
Some utilities for analyzing Minecraft (+FML) world files

## Requirements

This code requires Python 3+, and use of [Twoolie's NBT library](https://github.com/twoolie/NBT),
specifically my fork of it because the original's Chunk class has not been updated to Anvil:

https://github.com/cburschka/NBT

The code is specifically tailored for the Forge Mod Loader, and will mostly fail on worlds that
aren't using it.


## Setup

1. Clone this repository.
2. Copy `helperscripts/git-fat` to `~/bin` or some other directory that's in your path.
3. Make sure you can run it -- run `git fat` and you should have help output.
4. Run `git fat init` -- this just modifies .git/config in this repo to add the `fat` filter.
5. Optional: install `quilt` to be able to easily work with and create rpm patches.  There are spec files and sources for it and the required `diffstat` in this repo if it hasn't made it upstream yet.

## Fetching sources

`git-fat` requires explicit push/pull operations.  If you look at e.g. `packages/xterm/xterm-351.tgz` you'll see that it's a short text file containing a hash.

Run a `git fat pull` to get the actual source:

```
$ git fat pull packages/xterm
[...]
$ ls -l packages/xterm-351.tgz
[ something bigger than 128 bytes ]
```

You can also `git fat pull --all` to fetch all binary files.

## Adding/changing sources

When adding or changing files, git add/commit as normal.  Run `git fat push` to push any changed binary files.

## Working with `rpmbuild`/`quilt`/etc.

For a much better version of this section, see [PatchingRPMsWithQuilt](https://utcc.utoronto.ca/~cks/space/blog/linux/PatchingRPMsWithQuilt)

You really should go read that link instead of this section.

No, really.

Okay, I did tell you to go read that link.  Install `quilt`.

Ensure your `~/.rpmmacros` is configured to point to the sgug-rse repo, and to set sourcedir/specdir to be based on the package name:

```
%_topdir /usr/people/vladimir/proj/sgug-rse
%_sourcedir %{_topdir}/packages/%{name}
%_specdir %{_sourcedir}
```

Then let's do some work with xterm:

```
$ cd packages/xterm
$ quilt setup *.spec
### md5sum: ..g.....
### rpmbuild: tpppp
Unpacking archive xterm-351.tgz
```

`quilt` has unpacked the xterm source (in the current directory under `xterm-351`.  It knows about the patches from the spec file, but hasn't applied any of them yet:

```
$ cd xterm-351
$ quilt series -v
  patches/xterm-defaults.patch
  patches/xterm-desktop.patch
  patches/xterm-man-paths.patch
  patches/xterm.sgifixes.patch
```

Let's apply the existing patches.

```
$ Applying patch patches/xterm-defaults.patch
patching file XTerm.ad

Applying patch patches/xterm-desktop.patch
patching file xterm.desktop

Applying patch patches/xterm-man-paths.patch
patching file minstall.in
Hunk #2 succeeded at 169 (offset 1 line).
patching file xterm.man
Hunk #1 succeeded at 2471 (offset 143 lines).

Applying patch patches/xterm.sgifixes.patch
patching file main.c

Now at patch patches/xterm.sgifixes.patch

[sgugshell vladimir@reality xterm-351]$ quilt series -v
+ patches/xterm-defaults.patch
+ patches/xterm-desktop.patch
+ patches/xterm-man-paths.patch
= patches/xterm.sgifixes.patch
```

The current top/active (=) patch is the sgifixes patch.  Let's edit `main.c`, which is already modified by the sgifixes.patch:

```
$ vi main.c
[...]

$ quilt diff
quilt diff
Index: xterm-351/main.c
===================================================================
--- xterm-351.orig/main.c
+++ xterm-351/main.c

[... shows the changes to main.c from the previous patchlevel, i.e. your new change and whatever the patch did originally]

$ quilt refresh
quilt refresh
Refreshed patch patches/xterm.sgifixes.patch
```

At this point the `sgifixes` patch has been updated, and you're ready to run `rpmbuild` again.

At this point you should go read the the link at the start of this section or the quilt docs, because it's like a mini version control system.  Quilt will manage making the actual patch/diff between the previous version of all the files and new ones.  You do have to manually edit .spec files to add any newly-created patches, but it's a very efficient workflow for iterating on RPMs.

One important thing to remember is if you want to change a file, you have to manually `quilt add` the files you want to change _before_ you change them.  If you don't, you'll have to start over so that you can tell `quilt` what the clean version of the file looked like. 


IMPORTANT: if the spec file does not have any patches at all, you have to manually do this in order to have the `patches` dir point to the right place:

```
$ cd dir-source-was-unpacked-to
$ ln -s .. patches
```

if there are patches, `quilt` does this automatically.  `xterm` has patches, so the `patches` symlink already exists.  If you don't do this, quilt will create patches inside the wrong directory (inside a `patches` dir in the source tree).  If this happens just move `patches` to `..` and make the symlink.


## Other

### Troubleshooting

- Set `GIT_FAT_VERBOSE=1` to see more detail about what it's doing.

### Adding/changing what files are tracked

Add extensions to `.gitattributes`

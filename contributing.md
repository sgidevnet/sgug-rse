# sgug-rse - How To Contribute

Contributions to sgug-rse are more than welcomed - and the following guidelines are here to help you in submitting new toys for everyone to use!

You are free to contribute what/where you feel you can add value. That might be by submitting new packages - but could also be contributions that correct mistakes in our installation guide or new things to this document!

## Initial Setup

This repository is set up make it easy to work on RPMs directly inside the repository, with source management via `git-fat` and patch management via `quilt`.  The repository contains all of the source tarballs needed to build a package, but are stored using `git-fat` (which is a lightweight version of `git-lfs`).

This document does not go into detail about building RPM spec files or using rpmbuild.  See (this documentation) for more info.

### Setting up the reprository and build scripts on IRIX

First, clone the `sgug-rse` git repository.  This document will assume it's cloned at `~/sgug-rse`, but replace that with wherever you place it.

Second, install some prerequisites.  This assumes that you have the SGUG-RSE environment installed.  (If not, installation instructions are here!)

```
$ sudo tdnf install python2 python3-pip python3-wheel quilt
[....]

$ pip3 install awscli
```

Third, make sure the `git-fat` script is in your PATH.  If you have `~/bin` in PATH:

```
$ ln -s ~/sgug-rse/helperscripts/git-fat ~/bin/git-fat
```

Fourth, finally run `git-fat` to initialize things in the repository you cloned:

```
$ cd ~/sgug-rse
$ git-fat init
```

### Setting up `~/.rpmmacros`

Add the following at the start of `~/.rpmmacros`to redirect `rpmbuild` to the `sgug-rse` repository for finding source and spec files, and placing the output there.  Replace `vladimir` with your username.

```
%_topdir /usr/people/vladimir/sgug-rse
%_sourcedir %{_topdir}/packages/%{name}
%_specdir %{_sourcedir}
```

------------------------

## Working With Packages

`git-fat` requires explicit push/pull operations.  If you look at e.g. `packages/xterm/xterm-351.tgz` you'll see that it's a short text file containing a hash.

Run a `git fat pull` to get the actual source:

```
$ cd ~/sgug-rse
$ git fat pull packages/xterm
[...]
$ ls -l packages/xterm/xterm-351.tgz
[ something bigger than 128 bytes ]
```

When adding or changing files, git add/commit as normal.  Run `git fat push` to push any changed binary files.  See (Push Authorization) for authentication information.

### Making modifications to an existing package

(For a much better version of this section, see [PatchingRPMsWithQuilt](https://utcc.utoronto.ca/~cks/space/blog/linux/PatchingRPMsWithQuilt))

Let's do some work with xterm:

```
$ cd packages/xterm
$ git fat pull .
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
$ quilt push -a
Applying patch patches/xterm-defaults.patch
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


### Adding a new package

**If you have a SRPM**, install it; if your `.rpmmacros` is setup, the sources should end up inside `~/sgug-rse/packages/{packagename}`.  (Note: FC31 SRPMs can be searched and downloaded here: <https://koji.fedoraproject.org/koji/packages>).

You should `git add` and `git commit` the original files from the SRPM before making changes to them, to make it easy to diff against the original in the future.  Suggestion is to use the SRPM name as the commit message.

**If you don't have a SRPM**, make a new directory in `~/sgug-rse/packages/` with the package name.  Copy your source file(s) into it.  Make a `.spec` file in this directory.

Do work like the above instructions to modify; note that you'll have to manually symlink the `patches` dir as mentioned earlier if there are no patches by default.

`git add` and `git commit` everything as normal.

### Submitting your package

If you have access to the S3 bucket, you should `git-fat push` when you `git push` your branch upstream.  If you don't, talk to someone on Discord.

Then make a PR as normal.

## Other Notes

* If you can't find the exact version of the package, still try and use the .spec from fc31, we get dependency bonuses with other packages that might depend on it
* For things that don't have equivs in fedora, you can maybe find stuff in other RPM repos, libiconv for example was done this way
* Really there's no hard rules about quality - there's already packages in the rse that fail some tests, so don't be shy about "it has to be perfect"
* If you need to troubleshoot, `git-fat`, set `GIT_FAT_VERBOSE=1` in the environment to see more detail about what it's doing.
* If you need to add additional large file extensions to be tracked by `git-fat`, you can do so by adding them to `.gitattributes`.

## Packages - Preferred Patching / Change Approach

* For "code" things, those are tweaked via the "PACKAGENAME.sgifixes.patch" file
* For things that involve path fixes, it's preferred to do those rewrites in the `.spec` file - in the prep/configure stage
e.g. `perl -pi -e s|/usr/bin/bash|%{_bindir}/bash|g" /some/file/with/hardcoded/bash`
* Deactivation or activation of package options (to configure etc) should preferably be done from the `.spec` - so that if/when we have enough in RSE to enable the option, we can just tweak the `.spec` instead of changing the patch

## Packages - Things To Check For

Having an RPM building is a great step - but it is recommended to perform a "sanity sweep" looking for paths/resources that might obviously trip up use of the package.

* `grep -r "/bin/sh"` inside the BUILD directory, but also maybe in the BUILDROOT (staging) directory too (`rpmbuild -bi blah.spec --nocheck`)
* Some common problems are `/bin/sh /bin/bash /bin/perl /usr/local /etc/`
* Our preference is to do this (the rewriting) in the prep/configure stage so that when we `cd ~/rpmbuild/BUILD/package-XXX/` - the files are already corrected

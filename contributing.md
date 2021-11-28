# sgug-rse - How To Contribute

Contributions to sgug-rse are more than welcomed - and the following guidelines are here to help you in submitting new toys for everyone to use!

## What can I contribute?

You are free to contribute what/where you feel you can add value. That might be by submitting new packages - but could also be contributions that correct mistakes in our installation guide or new things to this document!

## How do I contribute?

The simplest method for us (the sgug-rse team) - is to:

* Clone the sgug-rse repository so you have a personal copy of the repository
* Checkout the `wipnonautomated` branch
* Ensure it is up to date (compared to the sgug-rse `wipnonautomated` branch)
* Make your changes and commit them (more detail about the "what" below)
* Push your changes to your clone on that `wipnonautomated` branch
* Go to github in your browser and you'll get the option to create a pull request
* Ensure the pull request is against the sgug-rse repository `wipnonautomated` branch
* One of our flight attendants will be with you shortly

## Packages - Deeper Detail

Things that are submitted + merged into `wipnonautomated` are in fact not "live" packages yet. It's a wip branch that lets the sgug-rse team work on new/up and coming changes together. Things in this branch don't have to be perfect - so that includes things in a pull request against the branch.

Once a package is reviewed and the sgug-rse team have some confidence in a package (either through internal tests or by having the thing used by another package that is "good enough") - the package is included in the "releasepackages.txt" file that our build automation can use.

At the next point-in-time release of sgug-rse, our tooling then works through the releasepackages.txt file building shiny new versions of the package.

## Packages - Adding/Porting A New Package

1) You may choose to port your package outside of rpmbuild, it can be easier to do the patching there before tackling the `.spec` build file

2) Check fedora fc31 if the package exists and pull the latest source RPM. Fedora source RPMs can be searched and downloaded here: <https://koji.fedoraproject.org/koji/packages>.

3) Install srpm, copy .spec into rse packages/PACKAGENAME/SPECS/PACKAGENAME.spec.origfedora

4) Edit ~/rpmbuild/SPECS/PACKAGENAME.spec until it is happily building (add patches in ~/rpmbuild/SOURCES/packagename.sgifixes.patch etc)

5) Copy back PACKAGENAME.spec to repo PACKAGENAME/SPECS/PACKAGENAME.spec plus any patches or modified sources into PACKAGENAME/SOURCES/

6) If you can't find the exact version of the package, still try and use the .spec from fc31, we get dependency bonuses with other packages that might depend on it

7) For things that don't have equivs in fedora, you can maybe find stuff in other RPM repos, libiconv for example was done this way

8) Really there's no hard rules about quality - there's already packages in the rse that fail some tests, so don't be shy about "it has to be perfect"

9) We prefer to not include large files in the repository, it is nice that this repository remains usable on irix natively

## Packages - Git Snapshots

* On the whole we prefer that packages follow the versioning of fc31 - this makes it easier for others to build the package (install the fc31 SRPM, copy over files from "wipnonautomated", build)
* Not always the case, meson for example is a git snapshot + fixes
* If we _do_ want a git snapshot, the "release" section of the version in the `.spec` should indicate it is a git snapshot. See meson as an example.

## Packages - Original Spec File

* If there is an fc31 package something is built from, we put the original fedora spec file next to the RSE one as "PACKAGENAME.spec.origfedora"
* Let's us easily do a "diff" to see what has been changed

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

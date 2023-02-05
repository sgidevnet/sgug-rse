Name:           git-tools
Version:        2019.11
Release:        1%{?dist}
Summary:        Assorted git-related scripts and tools

License:        GPLv3+
URL:            https://github.com/MestreLion/%{name}
Source0:        https://github.com/MestreLion/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       git

BuildRequires:  python3-devel

%description
Assorted git-related scripts and tools:

git-branches-rename:
Batch renames branches with a matching prefix to another prefix

git-clone-subset:
Clones a subset of a git repository

git-find-uncommitted-repos:
Recursively list repos with uncommitted changes

git-rebase-theirs:
Resolve rebase conflicts and failed cherry-picks by favoring 'theirs' version

git-restore-mtime:
Restore original modification time of files based on the date of the most
recent commit that modified them

git-strip-merge:
A git-merge wrapper that deletes files on a "foreign" branch before merging

%prep
%setup -q

# https://python-rpm-porting.readthedocs.io/en/latest/applications.html#fixing-shebangs
sed -i.bak '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' git-restore-mtime
touch -r git-restore-mtime.bak git-restore-mtime
rm -f git-restore-mtime.bak

perl -pi -e "s|#!/usr/bin/env bash|#!/usr/sgug/bin/bash|g" %{_builddir}/git-tools-2019.11/git-branches-rename
perl -pi -e "s|#!/usr/bin/env bash|#!/usr/sgug/bin/bash|g" %{_builddir}/git-tools-2019.11/git-clone-subset
perl -pi -e "s|#!/usr/bin/env bash|#!/usr/sgug/bin/bash|g" %{_builddir}/git-tools-2019.11/git-find-uncommitted-repos
perl -pi -e "s|#!/usr/bin/env bash|#!/usr/sgug/bin/bash|g" %{_builddir}/git-tools-2019.11/git-rebase-theirs
perl -pi -e "s|#!/usr/bin/env bash|#!/usr/sgug/bin/bash|g" %{_builddir}/git-tools-2019.11/git-strip-merge

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp -p git-branches-rename %{buildroot}%{_bindir}/.
cp -p git-clone-subset %{buildroot}%{_bindir}/.
cp -p git-find-uncommitted-repos %{buildroot}%{_bindir}/.
cp -p git-rebase-theirs %{buildroot}%{_bindir}/.
cp -p git-restore-mtime %{buildroot}%{_bindir}/.
cp -p git-strip-merge %{buildroot}%{_bindir}/.
mkdir -p %{buildroot}%{_mandir}/man1
cp -p man1/git-* %{buildroot}%{_mandir}/man1/.

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue May 04 2021  HAL <notes2@gmx.de> - 2019.11-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Thu Dec 19 2019 Greg Bailey <gbailey@lxpro.com> - 2019.11-1
- New upstream release 2019.11 (#1777999)
- several performance improvements
- use ISO datetime format
- refactor git calls into a convenience class
- improve documentation
- add several TODO and FIXME notes as a roadmap draft
- remove outdated benchmarks

* Mon Nov 18 2019 Greg Bailey <gbailey@lxpro.com> - 2019.10-1
- New upstream release 2019.10 (#1772903)
- Fix python3 incompatibility (#1748462)
- Drop python2 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Greg Bailey <gbailey@lxpro.com> - 2018.10-1
- New upstream release 2018.10
- Modify python shebang to specify explicit python version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2017.10-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Greg Bailey <gbailey@lxpro.com> - 2017.10-1
- New upstream release 2017.10
- Python 3 compatibility
- Rename the license to a standard name

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20160313gitd6d55b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20160313gitd6d55b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 13 2016 Greg Bailey <gbailey@lxpro.com> - 0-0.2.20160313gitd6d55b3
- New upstream snapshot with GPLv3 license file
- Remove unnecessary cleanup of buildroot
- Only copy and package the scripts that have manpages

* Mon Feb 15 2016 Greg Bailey <gbailey@lxpro.com> - 0-0.1.20160215gitea09519
- Initial package

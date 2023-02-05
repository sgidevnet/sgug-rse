%bcond_with tests

Name:           rpmconf
Summary:        Tool to handle rpmnew and rpmsave files
License:        GPLv3
Version:        1.0.21
Release:        1%{?dist}
URL:            http://wiki.github.com/xsuchy/rpmconf
# source is created by:
# git clone https://github.com/xsuchy/rpmconf.git
# cd rpmconf; tito build --tgz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  docbook-utils
BuildRequires:  docbook-dtd31-sgml
BuildRequires:  python3-sphinx
BuildRequires:  python3-devel
Requires:       %{name}-base
Requires:       python3-rpmconf
Requires:       rpm-python3
BuildRequires:  rpm-python3
%if %{with tests}
BuildRequires:  python3-pylint
BuildRequires:  python3-six
%endif
# mergetools
Suggests: diffuse 
Suggests: kdiff3
Suggests: meld
Suggests: vim-X11
Suggests: vim-enhanced
# sdiff
Suggests: diffutils

%description
This tool search for .rpmnew, .rpmsave and .rpmorig files and ask you what to do
with them:
Keep current version, place back old version, watch the diff or merge.

%package -n python3-rpmconf
Summary:        Python interface for %{name}
BuildArch:      noarch

%description -n python3-rpmconf
Python interface for %{name}. Mostly useful for developers only.

%package -n python3-rpmconf-doc
Summary:        Documentation of python interface for %{name}
BuildArch:      noarch

%description -n python3-rpmconf-doc
Documentation generated from code of python3-rpmconf.

%package base
Summary: Filesystem for %{name}
BuildArch: noarch

%description base
Directory hierarchy for installation scripts, which are handled by rpmconf.

%prep
%setup -q

%build
%{__python3} setup.py build
docbook2man rpmconf.sgml
make -C docs html man

%install
%{__python3} setup.py install --skip-build \
    --install-scripts %{_sbindir} \
    --root %{buildroot}
install -D -m 644 rpmconf.8 %{buildroot}%{_mandir}/man8/rpmconf.8
install -D -m 644 docs/build/man/rpmconf.3 %{buildroot}%{_mandir}/man3/rpmconf.3
mkdir -p %{buildroot}%{_datadir}/rpmconf/

%check
%if %{with tests}
pylint-3.6 rpmconf bin/rpmconf || :
%endif

%files
%license LICENSE
%{_sbindir}/rpmconf
%{_mandir}/man8/rpmconf.8*
%doc README.md

%files -n python3-rpmconf
%license LICENSE
%{python3_sitelib}/rpmconf/
%{python3_sitelib}/rpmconf-*.egg-info
%{_mandir}/man3/rpmconf.3*

%files -n python3-rpmconf-doc
%license LICENSE
%doc docs/build/html/

%files base
%dir %{_datadir}/rpmconf

%changelog
* Thu Jan 16 2020 Miroslav Suchý <msuchy@redhat.com> 1.0.21-1
- Drop the deprecated no-op "U" mode for open() to support Python 3.9

* Sun Sep 22 2019 Miroslav Suchý <msuchy@redhat.com> 1.0.20-1
- remove old changelog entries
- better handle message after merging
- do not run pylint by default
- add sdiff support [GH#51]
- rpmconf.sgml: Improve readability
- include README in package

* Wed Apr 05 2017 Miroslav Suchý <msuchy@redhat.com> 1.0.19-1
- implement --test
- 1350249 - correctly pass /dev/null to difflib

* Fri Jun 24 2016 Miroslav Suchý <miroslav@suchy.cz> 1.0.18-1
- add pylintrc

* Fri Jun 24 2016 Miroslav Suchý <miroslav@suchy.cz> 1.0.17-1
- set loglevel only for rpmconf logger
- standard import "import errno" comes before "from rpmconf import rpmconf"
  (wrong-import-order)
- fix a typo in the /usr/bin/ls arguments

* Tue Dec 01 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.16-1
- temporary workaround for BZ 1287055
- 1287034 - local variable 'fromdate' referenced before assignment

* Fri Nov 27 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.15-1
- 1277025 - handle broken symlinks

* Tue Nov 24 2015 Miroslav Suchý <miroslav@suchy.cz> 1.0.14-1
- we use utf8
- call python3 directly
- 1258464 - improve error message
- 1282029 - check for root privileges
- 1283698 - clarify man page

* Fri Nov 13 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.13-1
- 1278134 - do TB when somebody remove file under our hand

* Tue Jun 30 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.12-1
- disable pylint warning

* Tue Jun 30 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.11-1
- disable pylint warning

* Tue Jun 30 2015 Miroslav Suchý <miroslav@suchy.cz> 1.0.10-1
- 1236722 - other method for stdin flush and handle Ctrl+C correctly

* Mon Jun 01 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.9-1
- pylint: let the logger expand params
- use soft deps

* Mon Jun 01 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.8-1
- 1226591 - do not flush stdin, when it is not TTY
- BR python3-six
- minor fixes
- use RPM Python API to get package name of file

* Mon Jan 12 2015 Miroslav Suchý <miroslav@suchy.cz> 1.0.7-1
- correctly reference tar.gz
- add / before usr/bin
- remove superfluous changelog line

* Fri Jan 09 2015 Miroslav Suchý <miroslav@suchy.cz> 1.0.6-1
- let tito bump up version in docs/source/conf.py

* Thu Jan 08 2015 Miroslav Suchý <miroslav@suchy.cz> 1.0.5-1
- add -doc subpackage
- mark LICENSE as %%license
- Split to python class and CLI
- use rpm python api to get version

* Sun Nov 23 2014 Miroslav Suchý <msuchy@redhat.com> 1.0.4-1
- add BR rpm-python3

* Sun Nov 23 2014 Miroslav Suchý <miroslav@suchy.cz> 1.0.3-1
- Allow specification of a custom merge type via an environment variable,
  $MERGE
- do not remove files on those merge tools, which does not return correct exit
  code
- make pylint run mandatory
- skip /var/lib/mock when --clean
- use rpm bindings to find configfiles
- use filecmp instead of subprocessed diff

* Tue Nov 04 2014 Miroslav Suchý <msuchy@redhat.com> 1.0.2-1
- require rpm-python3

* Wed Oct 29 2014 Miroslav Suchý <msuchy@redhat.com> 1.0.1-1
- migrate to python3
- handle symlinks correctly
